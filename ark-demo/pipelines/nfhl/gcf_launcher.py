import os
#import base64
#import json
from flask import Flask, request
from apache_beam.options.pipeline_options import PipelineOptions
from apache_beam.options.pipeline_options import GoogleCloudOptions
from apache_beam.options.pipeline_options import StandardOptions
from apache_beam.options.pipeline_options import WorkerOptions

import nfhl_pipeline

app = Flask(__name__)

@app.route('/', methods=['POST'])
def run():
    message = request.get_json()['message']
    #message = json.loads(base64.b64decode(event['data']).decode('utf-8'))
    gcs_url = 'gs://' + message['bucket'] + '/' + message['name']

    options = PipelineOptions()
    gco = options.view_as(GoogleCloudOptions)
    gco.project = 'geo-solution-demos'
    gco.region = 'us-central1'
    gco.job_name = 'load-nfhl'
    gco.temp_location = 'gs://gsd-pipeline-temp/ladeedaaa'

    so = options.view_as(StandardOptions)
    so.runner = 'DataflowRunner'

    wo = options.view_as(WorkerOptions)
    wo.machine_type = 'c2-standard-4'
    wo.max_num_workers = 8
    wo.sdk_container_image = 'gcr.io/dataflow-geobeam/base'
    #options.view_as(SetupOptions).save_main_session = True

    nfhl_pipeline.run(options, gcs_url)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=int(os.environ.get('PORT', 8080)))
