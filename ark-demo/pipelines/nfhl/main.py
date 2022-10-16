def run(data, context):
    from googleapiclient.discovery import build

    project = 'geo-solution-demos'
    job = 'nfhl-load-' + str(data['name']).split('/')[-1].replace('.', '-').replace('_', '-').lower()
    template = 'gs://geo-demos/ark-demo/templates/nfhl-template.json'
    inputFile = 'gs://' + str(data['bucket']) + '/' + str(data['name'])
    parameters = {
        'gcs_url': inputFile
    }
    environment = {'temp_location': 'gs://gsd-pipeline-temp'}

    service = build('dataflow', 'v1b3', cache_discovery=False)

    request = service.projects().locations().flexTemplates().launch(
        projectId=project,
        location='us-central1',
        body={
            'launchParameter': {
                'jobName': job,
                'parameters': parameters,
                'environment': environment,
                'containerSpecGcsPath': template
            }
        }
    )
    response = request.execute()
    print(str(response))
    return response
