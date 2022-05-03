import json
from google.cloud import bigquery
from google.cloud.exceptions import NotFound, BadRequest

bq_tables = [
    'S_BASE_INDEX',
    'S_BFE',
    'S_CST_GAGE',
    'S_CST_TSCT_LN',
    'S_DATUM_CONV_PT',
    'S_FIRM_PAN',
    'S_FLD_HAZ_AR',
    'S_FLD_HAZ_LN',
    'S_GAGE',
    'S_GEN_STRUCT',
    'S_HWM',
    'S_HYDRO_REACH',
    'S_LABEL_LD',
    'S_LABEL_PT',
    'S_LEVEE',
    'S_LIMWA',
    'S_LOMR',
    'S_NODES',
    'S_PFD_LN',
    'S_PLSS_AR',
    'S_POL_AR',
    'S_PROFIL_BASLN',
    'S_RIV_MRK',
    'S_STN_START',
    'S_SUBBASINS',
    'S_SUBMITTAL_INFO',
    'S_TRNSPORT_LN',
    'S_TSCT_BASLN',
    'S_WTR_AR',
    'S_WTR_LN',
    'S_XS'
]
bq_client = bigquery.Client()
project = 'geo-solution-demos'
dataset = 'nfhl'
dataset_id = '{}.{}'.format(project, dataset)

# create dataset
try:
    bq_client.get_dataset(dataset_id)
except NotFound:
    ds = bigquery.Dataset(dataset_id)
    ds = bq_client.create_dataset(ds, timeout=30)

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
