# Multi Pipelines and Multi Result Files

### Enable writing to a single results file from multiple pipelines
The pipestat API supports writing to one results.yaml file via multiple pipelines. This can be enabled during pipestat initialization by setting `multi_pipelines` to true:

```python
psm = PipestatManager(results_file_path=result_file, schema_path=schema_file, multi_pipelines=True)
```

Example Results file
```yaml
test_pipeline_01:
  project: {}
  sample:
    RECORD1:
      number_of_things: 50000
      pipestat_created_time: '2024-04-04 17:23:56'
      pipestat_modified_time: '2024-04-04 18:28:59'
      name_of_something: Another_Name

test_pipeline_02:
  project:
    RECORD2:
      number_of_things: 42
      pipestat_created_time: '2024-04-04 18:23:56'
      pipestat_modified_time: '2024-04-04 19:28:59'
  sample: {}
```

### Enable writing each record to its own results file

Pipestat also supports writing a record's results to a separate file for every record. This can be achieved by placing the string `{record_identifier}` in the designated `results_file_path` field of the pipestat configuration file.

```yaml
schema_path: sample_output_schema.yaml
results_file_path: "${DATA}/processed/results_pipeline/{record_identifier}/stats.yaml"

```


Here is an example from the PEPATAC pipeline which currently uses this functionality via a `looper` config file:

```yaml
name: PEPATAC_tutorial
pep_config: tutorial_refgenie_project_config.yaml

output_dir: "${TUTORIAL}/processed/"
pipeline_interfaces:
  sample: ["${TUTORIAL}/tools/pepatac/sample_pipeline_interface.yaml"]
  project: ["${TUTORIAL}/tools/pepatac/project_pipeline_interface.yaml"]

pipestat:
  results_file_path: "${TUTORIAL}/processed/results_pipeline/{record_identifier}/stats.yaml"
```