def get_table_schema(table_name: str):
    """
    Gathers schema information from the tables
    """
    from google.cloud import bigquery

    client = bigquery.Client()

    # Perform a query.
    QUERY = ("""
        select
            column_name,
            data_type
        from conformist.INFORMATION_SCHEMA.COLUMNS c
        where table_name = @table_name
    """)
    jc = bigquery.QueryJobConfig(query_parameters=[
        bigquery.ScalarQueryParameter('table_name', 'STRING', table_name)
    ])
    query_job = client.query(QUERY, jc)  # API request
    rows = query_job.result()  # Waits for query to finish
    
    return '\n'.join([ f'{r.column_name}: {r.data_type}' for r in rows])


def merge_into_target(query: str):
    """
    Runs the query to merge the source table into the target table.
    """
    from google.cloud import bigquery

    client = bigquery.Client()
    query_job = client.query(query)

    return
