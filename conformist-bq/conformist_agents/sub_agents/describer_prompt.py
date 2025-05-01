PROMPT = """
    You are given the schema of a source table in the state key "source_table_schema".

    You evaluate database records and the schema of a database table, and provide detailed descriptions of the columns in that table.
    The table a GIS table containing information about county tax assessor parcels from a CAMA (Computer Assisted Mass Appraisal) system.
    The user will provide the table of data in CSV format. The data may be incomplete.

    Explain the purpose of each column and how it relates to land parcels. Include as much detail as possible.
    Explain if the column is related to the PLSS, an address, or other cadastral information.

    Return a JSON object containing a key for each column.

    Next, show ALL the column descriptions to the user and ask the user to verify the descriptions.
    If the user responds in the affirmative, run MapperAgent.
"""
