# Schema Harmonizer Agent

This is an agent built using ADK that automates the mapping of multiple disjoint source schemas into a single target schema. 

It contains multiple sub-agents that each perform specific tasks.

### Schema Gatherer

Reads the schema for each of the source and target tables from `information_schema` and queries for example data.

### Describer Agent

Produce a textual description for each source column gathered by the `Schema Gatherer`, and generates an embedding for each of those text descriptions.

### Mapper Agent

Attempts to produce a one-shot source->target column mapping by instructing the LLM directly.

### Deconflicter Agent

In the event that there is disagreement between `Mapper` and `Describer` agents, compare the reasoning and embedding distance values to determine which agent to believe. Then, present the mapping to a human for verification and/or further correction.

### Merger Agent

Generate a SQL query that inserts the data from the source table into the target table, performing the previously-ascertained mapping on-the-fly.
