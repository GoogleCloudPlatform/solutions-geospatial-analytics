# nfhl pipeline

Acquires NFHL data and loads into BigQuery via Dataflow

### Build and deploy

##### Build and Run template directly

```
docker build . -t gcr.io/geo-solution-demos/nfhl_pipeline_template
docker push gcr.io/geo-solution-demos/nfhl_pipeline_template

gcloud dataflow flex-template build gs://geo-demos/ark-demo/templates/nfhl-template.json
  --image gcr.io/geo-solution-demos/nfhl_pipeline_template
  --sdk-language PYTHON
  --metadata-file metadata.json

gcloud dataflow flex-template run "nfhl-import"
  --template-file-gcs-location gs://geo-demos/ark-demo/templates/nfhl-template.json
  --parameters "gcs_url=gs://geo-demos/ark-demo/sources/nfhl/NFHL_09_20220308.zip"
  --parameters "layer=S_FLD_HAZ_AR"
  --parameters "dataset=nfhl_staging"
```

##### Run from GCF




#### bq_create_tables.py

Creates required BigQuery tables from NFHL schemas. Set `GOOGLE_APPLICATION_CREDENTIALS` when running.

#### nfhl_gcs_stage.py

Acquires latest NFHL GDB files from FEMA's website and uploads to GCS

#### nfhl_pipeline.py

Dataflow pipeline to load staged GCS files into BigQuery

