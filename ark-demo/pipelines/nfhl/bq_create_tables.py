import json
from google.cloud import bigquery
from google.cloud.exceptions import NotFound, BadRequest

bq_tables = json.load(open('nfhl_layers.json'))
bq_client = bigquery.Client()
project = 'geo-solution-demos'
dataset = 'nfhl'
dataset_id = '{}.{}'.format(project, dataset)
staging_dataset_id = '{}.{}'.format(project, dataset + '_staging')

# create dataset if not exists
try:
    bq_client.get_dataset(dataset_id)
except NotFound:
    ds = bigquery.Dataset(dataset_id)
    ds = bq_client.create_dataset(ds, timeout=30)

# create staging dataset if not exists
try:
    bq_client.get_dataset(staging_dataset_id)
except NotFound:
    ds = bigquery.Dataset(staging_dataset_id)
    ds = bq_client.create_dataset(ds, timeout=30)

# create tables
for table_name in bq_tables:
    bq_schema = []
    bq_schema_staging = []
    schema_filename = '{}.json'.format(table_name)
    table_ref = '{}.{}'.format(dataset_id, table_name)
    with open(schema_filename) as f:
        bq_columns = json.load(f)
        for col in bq_columns:
            if col['name'] == 'geom':
                bq_schema.append(bigquery.SchemaField(col['name'], col['type']))
                bq_schema_staging.append(bigquery.SchemaField(col['name'], 'STRING'))
            else:
                bq_schema.append(bigquery.SchemaField(col['name'], col['type']))
                bq_schema_staging.append(bigquery.SchemaField(col['name'], col['type']))

    print('creating table {}'.format(table_ref))
    bq_table = bigquery.Table(table_ref, schema=bq_schema)
    bq_table.clustering_fields = ['geom']
    bq_table.time_partitioning = bigquery.TimePartitioning(type_='YEAR')
    try:
        print('skipping')
        #bq_table = bq_client.create_table(bq_table)
    except BadRequest as e:
        print(e)

    staging_table_ref = '{}.{}'.format(staging_dataset_id, table_name)
    print('creating table {}'.format(staging_table_ref))
    bq_table = bigquery.Table(staging_table_ref, schema=bq_schema_staging)
    #bq_table.clustering_fields = ['geom_str']
    #bq_table.time_partitioning = bigquery.TimePartitioning(type_='YEAR')
    try:
        bq_table = bq_client.create_table(bq_table)
    except BadRequest as e:
        print(e)
