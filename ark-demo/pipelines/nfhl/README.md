# nfhl pipeline

Acquires NFHL data and loads into BigQuery via Dataflow

#### gcf_launcher.py

Cloud Function that kicks off the pipeline when file is added to GCS bucket.

```
docker build . -t nfhl_pipeline
PORT=8080 && docker run -p 9090:${PORT} -e PORT=${PORT nfhl_pipeline
```

#### bq_create_tables.py

Creates required BigQuery tables from NFHL schemas. Set `GOOGLE_APPLICATION_CREDENTIALS` when running.

#### nfhl_gcs_stage.py

Acquires latest NFHL GDB files from FEMA's website and uploads to GCS

#### nfhl_pipeline.py

Dataflow pipeline to load staged GCS files into BigQuery

