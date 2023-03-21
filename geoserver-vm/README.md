# geoserver-vm

Deploy [geoserver](https://geoserver.org/) as a container with [BigQuery support](https://github.com/GoogleCloudPlatform/bigquery-geotools) pre-installed.

Based on the [official Geoserver docker image](https://github.com/geoserver/docker) with minor modifications to install the `bigquery-geotools` library.

## Deploy

The VM method of deploying geoserver uses a single persistent disk to store the data directoy and GWC cache.

### Deploy using `gcloud`

```
gcloud compute instances create-with-container geoserver-vm --container-image gcr.io/bigquery-geotools/geoserver --tags tomcat-server --zone us-central1-a
gcloud compute firewall-rules create allow-http-8080 --allow tcp:8080 --target-tags tomcat-server
```

### Deploy using terraform

1. Create a terraform state bucket, e.g. 

```
gsutil mb gs://geoserver-vm-tfstate
```

2. Deploy!

```
GOOGLE_APPLICATION_CREDENTIALS=your-key-file.json terraform apply
```

### Deploy using [Cloud Build](https://cloud.google.com/build)

```
# update main.tf with your state bucket name
gcloud builds sbumit --subtitutions _TF_BUCKET=geoserver-vm-tfstate
```


