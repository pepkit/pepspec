# Pipestat configuration

Pipestat *requires* a few pieces of information to run:

- a **pipeline_name** to write into, usually contained within the schema file (see below).
- a path to the **schema** file that describes results that can be reported, e.g. `"your/path/sample_output_schema.yaml"`:
```yaml
title: An example Pipestat output schema
description: A pipeline that uses pipestat to report sample and project level results.
type: object
properties:
  pipeline_name: "default_pipeline_name"
  samples:
    type: array
    items:
      type: object
      properties:
        result_name:
          type: string
          description: "ResultName"

```
- **backend info**: either path to a YAML-formatted file or pipestat config with PostgreSQL database login credentials. Note that the config file can also contain a path to the yaml-formatted results file:
```yaml
schema_path: sample_output_schema.yaml
#The config can contain either a results_file_path (file backend) or a database connection (database backend)
# results_file_path takes priority and will create a PipestatManager with a file backend
results_file_path: results_file.yaml 
database:
  dialect: postgresql
  driver: psycopg
  name: pipestat-test
  user: postgres
  password: pipestat-password
  host: 127.0.0.1
  port: 5432

```

Apart from that, there are many other *optional* configuration points that have defaults. Please refer to the [environment variables reference](http://pipestat.databio.org/en/dev/env_vars/) to learn about the the optional configuration options and their meaning.

## Configuration sources

Pipestat configuration can come from 3 sources, with the following priority:

1. `PipestatManager` constructor
2. Pipestat configuration file
3. Environment variables
