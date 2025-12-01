# Back-end types


The pipestat specification describes three backend types for storing results: a [YAML-formatted file](https://yaml.org/spec/1.2/spec.html), a [PostgreSQL database](https://www.postgresql.org/) or reporting results to [PEPhub](https://pephub.databio.org/). This flexibility makes pipestat useful for a wide variety of use cases. Some users just need a simple text file for smaller-scale needs, which is convenient and universal, requiring no database infrastructure. For larger-scale systems, a database back-end is necessary. The pipestat specification provides a layer that spans the three possibilities, so that reports can be made in the same way, regardless of which back-end is used in a particular use case.

By using the `pipestat` package to write results, the pipeline author need not be concerned with database connections or dealing with racefree file writing, as these tasks are already implemented. The user who runs the pipeline will simply configure the pipestat backend as required.

Both backends organize the results in a hierarchy which is *always* structured this way:

![Result hierarchy](img/result_hierarchy.svg)



## File

The changes reported using the `report` method of `PipestatManger` will be securely written to the file. Currently only [YAML](https://yaml.org/) format is supported. 

Example:

```python
psm = PipestatManager(results_file_path="result_file.yaml", schema_path=schema_file)
```

For the YAML file backend, each file represents a namespace. The file always begins with a single top-level key which indicates the namespace. Second-level keys correspond to the record identifiers; third-level keys correspond to result identifiers, which point to the reported values. The values can then be any of the allowed pipestat data types, which include both basic and advanced data types.

```yaml
default_pipeline_name:
  project: {}
  sample:
    sample_1:
      meta:
        pipestat_modified_time: '2025-10-01 12:48:58'
        pipestat_created_time: '2025-10-01 12:48:58'
      number_of_things: '12'
```

## PostgreSQL database
This option gives the user the possibility to use a fully fledged database to back `PipestatManager`. 

Example:

```python
psm = PipestatManager(config_file="config_file.yaml", schema_path=schema_file)
```
where the config file has the following (example) values:

```yaml
schema_path: sample_output_schema.yaml
database:
  dialect: postgresql
  driver: psycopg
  name: pipestat-test
  user: postgres
  password: pipestat-password
  host: 127.0.0.1
  port: 5432

```

For the PostgreSQL backend, the name of the database is configurable and defined in the [config file](config.md) in `database.name`. The database is structured like this:

- The namespace corresponds to the name of the table.
- The record identifier is indicated in the *unique* `record_identifier` column in that table.
- Each result is specified as a column in the table, with the column name corresponding to the result identifier
- The values in the cells for a record and result identifier correspond to the actual data values reported for the given result.

![RDB hierarchy](img/db_hierarchy.svg)



## PEP on PEPhub
This option gives the user the possibility to use [PEPhub](https://pephub.databio.org/) as a backend for results. 

```python
psm = PipestatManager(pephub_path=pephubpath, schema_path="sample_output_schema.yaml")
```


All three backends *can* be configured using the config file. However, the PostgreSQL backend *must* use a config file.