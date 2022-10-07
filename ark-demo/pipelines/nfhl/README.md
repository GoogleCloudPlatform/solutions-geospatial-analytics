# nfhl pipeline

Acquires NFHL data and loads into BigQuery via Dataflow

##### Deploy

```
docker build -f Dockerfile.run -t gcr.io/geo-solution-demos/nfhl_run_handler .
docker build -f Dockerfile.dataflow -t gcr.io/geo-solution-demos/nfhl_pipeline .

gcloud run deploy nfhl-pipeline-runner \
  --image gcr.io/geo-solution-demos/nfhl_run_handler \
  --timeout 3600 \
  --region us-central1

gcloud eventarc triggers create new-nfhl-file-trigger \
  --destination-run-service=nfhl-pipeline-runner \
  --event-filters="type=google.cloud.storage.object.v1.finalized" \
  --event-filters="bucket=nfhl-uploads" \
  --service-account=111827087946-compute@developer.gserviceaccount.com \
  --location us-central1
```

#### bq_create_tables.py

Creates required BigQuery tables from NFHL schemas. Set `GOOGLE_APPLICATION_CREDENTIALS` when running.

#### nfhl_gcs_stage.py

Acquires latest NFHL GDB files from FEMA's website and uploads to GCS

#### nfhl_pipeline.py

Dataflow pipeline to load staged GCS files into BigQuery

