# geoserver-run

Deploy [geoserver](https://geoserver.org/) on [Cloud Run](https://cloud.google.com/run)

## Architecture

Geoserver can run in a typical tomcat servlet container on [Cloud Run](https://cloud.google.com/run), using
[Filestore](https://cloud.google.com/filestore) as a shared configuration directory
and shared geowebcache blob store location.

The key requirement for geoserver to run in this fashion is that the
administration web user interface must be run on a separate, stateful machine
because of how geoserver deals with its local configuration.

## How to deploy

1. Set up Filestore. See this tutorial on [Using Filestore with Cloud Run](https://cloud.google.com/run/docs/tutorials/network-filesystems-filestore)

2. Deploy Geoserver serving instances. These will not host the admin interface due to `GEOSERVER_CONSOLE_DISABLED=true`

```
gcloud run deploy geoserver-serving \
    --image gcr.io/bigquery-geotools/geoserver-run-serving \
    --vpc-connector geoserverdata \
    --execution-environment gen2 \
    --allow-unauthenticated \
    --service-account [projectid]-compute@developer.gserviceaccount.com \
    --update-env-vars FILESTORE_IP_ADDRESS=XX.XX.XX.XX,FILE_SHARE_NAME=geoserver1
    --min-instances 1
    --memory 4G
```

3. Deploy the Geoserver admin instance. This must be deployed on a VM, or as a Cloud Run app that only runs a single instance at a time. (`--max-instances 1`)

```
gcloud run deploy geoserver-admin \
    --image gcr.io/bigquery-geotools/geoserver-run-admin \
    --max-instances 1 \
    --vpc-connector geoserverdata \
    --execution-environment gen2 \
    --allow-unauthenticated \
    --service-account [projectid]-compute@developer.gserviceaccount.com \
    --update-env-vars FILESTORE_IP_ADDRESS=XX.XX.XX.XX,FILE_SHARE_NAME=geoserver1,GEOSERVER_CSRF_DISABLED=true \
    --memory 2G
```

### Important Note on geoserver configuration

You can change the geoserver configuration by accessing the `geoserver-admin`
Cloud Run deployment (using the URL that it gives you after deployment). 

However, it is important to note that configuration changes will not
automatically propagate to all serving nodes. This is because geoserver loads
the configuration from disk into RAM on startup, and needs to be restarted in
order to take the new configuration.

To ensure all serving nodes are restarted and therefore reload the latest
configuration from disk (Filestore), you can redeploy `geoserver-serving`
either by:
1. Re-run the `gcloud run deploy` command above
2. Open the [Cloud Run Console](https://console.cloud.google.com/), select the
`geoserver-serving` service, and click *Edit & Deploy New Revision*.


## Add layers and serve

1. You can now visit the admin instance in your browser at
`https://geoserver-admin-[abcxyz].a.run.app/geoserver/web` and configure new layers.
If you have the BigQuery driver installed, you can connect to a BigQuery table.
Otherwise, you can configure geoserver the way you normally would.

2. The admin instance should be used for making configuration changes only. Once the
configuration has been updated, you will need to redeploy the serving instances
so that they read the new configuration. One way of doing this is to click
"Edit & Deploy New Revision" and update a `CONFIG_VERSION` env var to a new value.

You may need to redeploy in order for new layers to be available. See note above.

## Performance tuning and Scaling

### Filestore

Filestore supports both HDD and SSD storage options. Either can be a good option
depending on your requirements. Substantially of the performance difference
will be apparent in [geowebcache](https://www.geowebcache.org/) performance, where the SSD will return
cached tiles with somewhat lower latency due to better random-access
performance.

### Cloud Run

As can be inferred above, we recommend at least *4GB* RAM for serving nodes,
and 2GB for the admin node. A variety of CPU options can be selected for
your deployment, and it is recommended that you test your own workload to
determine the best CPU configuration for your needs.

## Comparison with single-VM hosting

Hosting geoserver on Cloud Run has the potential to increase the scalability of
your geoserver deployment, but there are a few considerations to keep in mind.

1. Geoserver was designed for single-machine hosting. It is not ideally-tuned
for clustered environments, and you may experience inconsistencies compared
with single-VM hosting.

2. Configuration changes are handled differently; see note above.

3. Single-VM deployments are "good enough" for most geoserver deployments. In
practice, much serving is done via geowebcache once the cache is primed, and
GWC is known to be able to [saturate a gigabit line with very modest hardware](https://www.geowebcache.org/docs/current/production/index.html#clustering).
Additional performance and latency gains could be achieved by pairing a VM with
[Cloud CDN](https://cloud.google.com/cdn), for example.


## Questions / Problems?

If you run into problems with this setup, please don't hesitate to file an
issue on this repository and we will address it as soon as we can!
