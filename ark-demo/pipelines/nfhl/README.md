# nfhl pipeline

Acquires NFHL data and loads into BigQuery via Dataflow


#### bq_create_tables.py

Creates required BigQuery tables from NFHL schemas. Set `GOOGLE_APPLICATION_CREDENTIALS` when running.

#### nfhl_gcs_stage.py

Acquires latest NFHL GDB files from FEMA's website and uploads to GCS

#### nfhl_pipeline.py

Dataflow pipeline to load staged GCS files into BigQuery

