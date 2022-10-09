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
Load NFHL into BigQuery
"""

import datetime
from apache_beam.options.pipeline_options import PipelineOptions
import logging


def parse_gcs_url(gcs_url):
    [full_path, suffix] = gcs_url.split('.')
    basename = full_path.split('/')[-1]
    [prefix, fips, release] = basename.split('_')
    gdb_name = '{}.gdb'.format(basename)

    release_date = datetime.datetime.strptime(release, '%Y%m%d')

    return release_date, gdb_name


"""
Fix GDB datetime fields
see https://desktop.arcgis.com/en/arcmap/latest/manage-data/tables/fundamentals-of-date-fields.htm
"""
def format_gdb_datetime(element, schema):
    from datetime import datetime
    props, geom = element
    dt_fields = []
    for field in schema:
        if field['type'] == 'DATETIME':
            dt_fields.append(field['name'])

    for field in dt_fields:
        if props[field] is not None:
            dt_in = datetime.strptime(props[field], '%Y-%m-%dT%H:%M:%S%z')
            props[field] = dt_in.replace(tzinfo=None).strftime('%Y-%m-%d %H:%M:%S')

    return props, geom


def get_schemas():
    from google.cloud import storage
    import json

    schemas = {}
    client = storage.Client()
    bucket = client.bucket('geo-demos')
    schema_ls = client.list_blobs('geo-demos', prefix='ark-demo/schemas/', delimiter='/')

    for schema_file in schema_ls:
        if not schema_file.name.endswith('.json'):
            continue

        layer_name = schema_file.name.split('/')[-1].split('.json')[0]
        schema_json = json.loads(bucket.blob(schema_file.name).download_as_string())
        schemas[layer_name] = schema_json

    return schemas


def run(pipeline_args, gcs_url, layer=None, dataset=None):
    import apache_beam as beam
    from apache_beam.io.gcp.internal.clients import bigquery as beam_bigquery

    from geobeam.io import GeodatabaseSource
    from geobeam.fn import make_valid, filter_invalid, format_record

    release_date, gdb_name = parse_gcs_url(gcs_url)

    layer_schemas = get_schemas()

    if layer is not None:
        nfhl_layers = [layer]
    else:
        nfhl_layers = layer_schemas.keys()

    pipeline_options = PipelineOptions(
        pipeline_args,
        experiments=['use_runner_v2'],
        temp_location='gs://gsd-pipeline-temp',
        sdk_container_image='gcr.io/dataflow-geobeam/base',
        project='geo-solution-demos',
        region='us-central1',
        worker_machine_type='c2-standard-4',
        max_num_workers=32
    )

    write_method = beam.io.BigQueryDisposition.WRITE_APPEND
    if known_args.truncate:
        write_method = beam.io.BigQueryDisposition.WRITE_TRUNCATE

    with beam.Pipeline(options=pipeline_options) as p:
        for layer in nfhl_layers:
            layer_schema = layer_schemas[layer]
            (p
             | 'Read ' + layer >> beam.io.Read(GeodatabaseSource(gcs_url,
                 layer_name=layer,
                 gdb_name=gdb_name))
             #| 'MakeValid ' + layer >> beam.Map(make_valid)
             #| 'FilterInvalid ' + layer >> beam.Filter(filter_invalid)
             | 'FormatGDBDatetimes ' + layer >> beam.Map(format_gdb_datetime, layer_schema)
             | 'FormatRecord ' + layer >> beam.Map(format_record, output_type='geojson')
             | 'WriteToBigQuery ' + layer >> beam.io.WriteToBigQuery(
                   beam_bigquery.TableReference(projectId='geo-solution-demos', datasetId=dataset, tableId=layer),
                   method=beam.io.WriteToBigQuery.Method.FILE_LOADS,
                   write_disposition=write_method,
                   create_disposition=beam.io.BigQueryDisposition.CREATE_NEVER)
            )

    if known_args.safe_mode:
        from google.cloud import bigquery
        client = bigquery.Client()
        for layer in nfhl_layers:
            sql = (
                'insert into `geo-solution-demos.' + dataset + '.' + layer + '` '
                'select * except(geom), st_geogfromgeojson(geom, make_valid => true) as geom '
                'from `geo-solution-demos.' + dataset + '_staging' + '.' + layer + '` '
            )
            result = client.query(sql)
            print(result)


if __name__ == '__main__':
    import argparse

    logging.getLogger().setLevel(logging.INFO)

    parser = argparse.ArgumentParser()
    parser.add_argument('--gcs_url', type=str)
    parser.add_argument('--layer', type=str, default=None)
    parser.add_argument('--dataset', type=str, default='nfhl_staging')
    parser.add_argument('--safe_mode', type=bool, default=False)
    parser.add_argument('--truncate', type=bool, default=False)

    known_args, pipeline_args = parser.parse_known_args()

    run(pipeline_args, known_args.gcs_url, known_args.layer, known_args.dataset)
