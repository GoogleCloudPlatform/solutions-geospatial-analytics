# geoserver-vm

Deploy [geoserver](https://geoserver.org/) as a container with [BigQuery support](https://github.com/GoogleCloudPlatform/bigquery-geotools).

Based on the [official Geoserver docker image](https://github.com/geoserver/docker) with minor modifications to install the `bigquery-geotools` library.

## Deploy

1. Create a terraform state bucket, e.g. 

```
gsutil mb gs://geoserver-vm-tfstate
```

2. Deploy!

```
gcloud builds submit
```


