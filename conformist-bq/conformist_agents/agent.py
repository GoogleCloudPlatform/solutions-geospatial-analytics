from google.adk.agents import ParallelAgent, SequentialAgent, Agent

from . import MODEL

from .tools.get_table_schema import get_table_schema
from .tools.get_table_schema import merge_into_target

from .sub_agents.describer_prompt import PROMPT as DESCRIBER_PROMPT
from .sub_agents.mapper_prompt import PROMPT as MAPPER_PROMPT
from .sub_agents.deconflicter_prompt import PROMPT as DECONFLICTER_PROMPT

"""
DeconflicterAgent = Agent(
    name='DeconflicterAgent',
    model=MODEL,
    description=(
        'Reconcile results from embedding comparison and mapper output"
    ),
    instruction=DECONFLICTER_PROMPT,
)
"""

MergerAgent = Agent(
    name='MergerAgent',
    model=MODEL,
    description='You generate and run SQL queries in BigQuery to merge the tables',
    instruction=("""
        Using the mappings object in the state key "mappings", generate a Bigquery MERGE INTO
        SQL statement that writes the source_table into the target_table.

        Make sure to use CAST() to cast the values to the correct datatype in target_schema.

        The BigQuery dataset is called "conformist", so make sure to prefix the table names
        with the dataset when generating a query.

        Run the query in BigQuery using the merge_into_target tool.
    """),
    tools=[merge_into_target]
)

MapperAgent = Agent(
    name='MapperAgent',
    model=MODEL,
    description=(
        'Evaluate two tables to determine how to map columns from source_table to target_table.'
    ),
    instruction=MAPPER_PROMPT,
    output_key='mappings'
)

DescriberAgent = Agent(
    name='DescriberAgent',
    model=MODEL,
    description=(
        'Describe the table schema for source_table.'
    ),
    instruction=DESCRIBER_PROMPT,
    tools=[],
    output_key='column_descriptions'
)


SchemaGatherer = Agent(
    name='SchemaGatherer',
    instruction=("""
    The user will first provide the name of the source table they want to merge data from. If they have
    not provided it, ask them for it.
    Store the source table name in a state key called "source_table".

    Then the user will provide the name of the target table they want to merge into. If they have
    not provided it, ask them for it.
    Store the target table name in a state key called "target_table".

    Invoke the tool "get_table_schema" to get the schemas for both the source_table and target_table.
    Pass the value stored in state key "table_name" to the tool.

    Store the source table schema in a state key called "source_schema".
    Store the target table schema in a state key called "target_schema".

    Once you get the result, run DescriberAgent to display the descriptions and verify them with the user.
    """),
    tools=[get_table_schema],
    description='Gathers information about the source and target tables.',
    output_key='table_schemas'
)

root_agent = Agent(
    name='root_agent',
    model=MODEL,
    instruction=("""
    You are a virtual assistant for merging database tables of land parcels. You specialize in
    mapping columns from a source table to a target table.

    First, greet the user and ask what you can help with. Then gather the table information.
    """),
    description='You are an agent that starts a workflow to merge to tables together in BigQuery',
    sub_agents=[
        MergerAgent
        SchemaGatherer,
        DescriberAgent,
        MapperAgent,
    ],
    output_key='source_table,target_table'
)
