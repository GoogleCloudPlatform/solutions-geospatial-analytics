import json
from google.cloud import bigquery
from google.cloud.exceptions import NotFound, BadRequest

bq_tables = json.load(open('nfhl_layers.json'))
bq_client = bigquery.Client()
project = 'geo-solution-demos'
dataset = 'nfhl'
dataset_id = '{}.{}'.format(project, dataset)

# create dataset if not exists
try:
    bq_client.get_dataset(dataset_id)
except NotFound:
    ds = bigquery.Dataset(dataset_id)
    ds = bq_client.create_dataset(ds, timeout=30)

# create tables
for table_name in bq_tables:
    bq_schema = []
    schema_filename = '{}.json'.format(table_name)
    table_ref = '{}.{}.{}'.format(project, dataset, table_name)
    with open(schema_filename) as f:
        bq_columns = json.load(f)
        for col in bq_columns:
            bq_schema.append(bigquery.SchemaField(col['name'], col['type']))

    print('creating table {}'.format(table_ref))
    bq_table = bigquery.Table(table_ref, schema=bq_schema)
    bq_table.clustering_fields = ['geom']
    bq_table.time_partitioning = bigquery.TimePartitioning(type_='MONTH')
    try:
        bq_table = bq_client.create_table(bq_table)
    except BadRequest as e:
        print(e)
