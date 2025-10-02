# Reporting record identifier/sample statuses

Ensure you set a directory to contain the status files if using a file backend:

```python
psm = PipestatManager(results_file_path="results.yaml",schema_path="output_schema.yaml", flag_file_dir="./flags/")

```

Now, when running your pipeline you can simply set the status based of the current record:

```python
psm.set_status(record_identifier="sample1", status_identifier="completed")
```

All statuses are defined in the schemas/status_schema.yaml file:

```yaml
running:
  description: "the pipeline is running"
  color: [30, 144, 255] # dodgerblue
completed:
  description: "the pipeline has completed"
  color: [50, 205, 50] # limegreen
failed:
  description: "the pipeline has failed"
  color: [220, 20, 60] # crimson
waiting:
  description: "the pipeline is waiting"
  color: [240, 230, 140] # khaki
partial:
  description: "the pipeline stopped before completion point"
  color: [169, 169, 169] # darkgray

```


### Coming from Looper? Make sure to set this flag directory in the looper config file:

``` 
pep_config: ./metadata/pep_config.yaml # pephub registry path or local path
output_dir: ./results
pipeline_interfaces:
  - pipeline/pipeline_interface.yaml
pipestat:
  project_name: count_lines
  results_file_path: results.yaml
  flag_file_dir: results/flags

```