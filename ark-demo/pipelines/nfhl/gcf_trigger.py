def run_nfhl_pipeline_job(event, context):
    from googleapiclient.discovery import build

    project = 'geo-solution-demos'
    job = project + '_nfhl_' + str(data['timeCreated'])

