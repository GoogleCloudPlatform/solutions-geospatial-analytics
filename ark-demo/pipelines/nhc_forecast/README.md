# nhc_forecast

Load NHC hurricane forecast cones into BigQuery for analysis

### Make tables

```
bq mk nhc.nhc_5day_pgn nhc_5day_pgn.json
bq mk nhc.nhc_5day_pts nhc_5day_pts.json
bq mk nhc.nhc_5day_lin nhc_5day_lin.json
```

### Build template container

```
docker build . -t gcr.io/geo-solution-demos/nhc_forecast_pipeline_template
docker push gcr.io/geo-solution-demos/nhc_forecast_pipeline_template
```

### Build flex template

```
gcloud dataflow flex-template build gs://geo-demos/ark-demo/templates/nhc-template.json
  --image gcr.io/geo-solution-demos/nhc_forecast_pipeline_template
  --sdk-language PYTHON
  --metadata-file metadata.json

# run manually
gcloud dataflow flex-template run "nhc-import"
  --template-file-gcs-location gs://geo-demos/ark-demo/templates/nhc-template.json
  --parameters "gcs_url=gs://geo-demos/ark-demo/sources/nhc/al092022_5day_025A.zip"
```

### Deploy gcf trigger

```
gcloud functions deploy nhc-pipeline-launcher
  --region us-central1
  --runtime python38
  --entry-point run
  --trigger-bucket nhc-uploads
  --source .

gsutil cp <NHC shp> gs://nhc-uploads
```
