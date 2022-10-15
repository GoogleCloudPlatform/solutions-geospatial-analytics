# Copyright 2022 Google LLC
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     https://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

"""
Load NHC forecast cone into BigQuery
"""

import os
from apache_beam.options.pipeline_options import PipelineOptions
import logging

layer_suffixes = ['lin', 'pgn', 'pts']
tables = {
    'lin': 'nhc_5day_lin',
    'pgn': 'nhc_5day_pgn',
    'pts': 'nhc_5day_pts'
}


def get_layername(gcs_url, suffix):
    filename, ext = os.path.splitext(gcs_url.split('/')[-1])
    [date, dur, incr] = filename.split('_')

    return '{}-{}_{}_{}'.format(date, incr, dur, suffix)


def run(pipeline_args, gcs_url, dataset):
    import apache_beam as beam
    from apache_beam.io.gcp.internal.clients import bigquery as beam_bigquery

    from geobeam.io import ShapefileSource
    from geobeam.fn import make_valid, filter_invalid, format_record

    pipeline_options = PipelineOptions(
        pipeline_args,
        experiments=['use_runner_v2'],
        temp_location='gs://gsd-pipeline-temp',
        sdk_container_image='gcr.io/dataflow-geobeam/base',
        project='geo-solution-demos',
        region='us-central1',
        max_num_workers=1,
        number_of_worker_harness_threads=1
    )

    with beam.Pipeline(options=pipeline_options) as p:
        for suffix in layer_suffixes:
            layer = get_layername(gcs_url, suffix)
            (p
             | 'Read ' + layer >> beam.io.Read(ShapefileSource(gcs_url, layer_name=layer, in_epsg=4326))
             | 'MakeValid ' + layer >> beam.Map(make_valid)
             | 'FilterInvalid ' + layer >> beam.Filter(filter_invalid)
             | 'FormatRecord ' + layer >> beam.Map(format_record, output_type='geojson')
             | 'WriteToBigQuery ' + layer >> beam.io.WriteToBigQuery(
                   beam_bigquery.TableReference(projectId='geo-solution-demos', datasetId=dataset, tableId=tables[suffix]),
                   method=beam.io.WriteToBigQuery.Method.FILE_LOADS,
                   write_disposition=beam.io.BigQueryDisposition.WRITE_TRUNCATE,
                   create_disposition=beam.io.BigQueryDisposition.CREATE_NEVER)
             )


if __name__ == '__main__':
    import argparse

    logging.getLogger().setLevel(logging.INFO)

    parser = argparse.ArgumentParser()
    parser.add_argument('--gcs_url', type=str)
    parser.add_argument('--dataset', type=str, default='nhc')

    known_args, pipeline_args = parser.parse_known_args()

    run(pipeline_args, known_args.gcs_url, known_args.dataset)
