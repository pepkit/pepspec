# Pipestat

Pipestat-compatible pipelines will allow you to use looper to do 2 things:

1. monitor the status of pipeline runs
2. summarize the results of pipelines

For non-pipestat-compatible pipelines, you can still use looper to run pipelines, but you won't be able to use `looper report` or `looper check` to manage their output.

For a tutorial example using looper with pipestat please see this [documentation](tutorial/pipestat.md)


This document will explore, in futher detail, how to configure pipestat in Looper:

!!! success "Learning objectives"
    - How do I configure looper so that it can utilize pipestat?
    - How do I use different pipestat backends with looper?


## Pipestat configuration overview

During a pipeline run, looper will create a pipestat configuration file, which is a merging of information found in these two sources:

1. pipeline interface
2. looper_config file

Looper will combine the necessary configuration data and write a new pipestat configuration for each pipeline interface. The configuration file is then used by the pipeline interface (and pipeline) to create a PipestatManager object. This instatiated PipestatManager object can then be used to report results.

1. Add `pipestat` key and information to the looper config file.

Briefly, the Looper config file must contain a pipestat field. The user must also supply a file path for a results file if using a local file backend or database credentials if using a postgresql database backend. 

```yaml title=".looper.yaml" hl_lines="5-8"
pep_config: project_config_pipestat.yaml # pephub registry path or local path
output_dir: results
pipeline_interfaces:
  - ./pipeline_interface1_sample_pipestat.yaml
pipestat:
  project_name: TEST_PROJECT_NAME
  results_file_path: tmp_pipestat_results.yaml
  flag_file_dir: output/results_pipeline
```

A project name must be supplied if running a project level pipeline. 


```yaml title=".looper.yaml" hl_lines="6"
pep_config: project_config_pipestat.yaml # pephub registry path or local path
output_dir: results
pipeline_interfaces:
  - ./pipeline_interface1_sample_pipestat.yaml
pipestat:
  project_name: TEST_PROJECT_NAME
  results_file_path: tmp_pipestat_results.yaml
  flag_file_dir: output/results_pipeline
```

Instead of a results file path for a file backend, pipestat also support other backend types such as a postgres sql database:

```yaml title=".looper.yaml" hl_lines="7-14"
pep_config: project_config_pipestat.yaml # pephub registry path or local path
output_dir: results
pipeline_interfaces:
  - ./pipeline_interface1_sample_pipestat.yaml
pipestat:
  flag_file_dir: output/results_pipeline
  database:
    dialect: postgresql
    driver: psycopg2
    name: pipestat-test
    user: postgres
    password: pipestat-password
    host: 127.0.0.1
    port: 5432
```

You can also use pephub as a backend for reporting results:

```yaml title=".looper.yaml" hl_lines="7"
pep_config: project_config_pipestat.yaml # pephub registry path or local path
output_dir: results
pipeline_interfaces:
  - ./pipeline_interface1_sample_pipestat.yaml
pipestat:
  flag_file_dir: output/results_pipeline
  pephub_path: "databio/pipestat_demo:default"
```

2. The pipeline interface must include information required by pipestat such as pipeline_name, pipeline_type, and an output schema path:
```yaml title="Pipeline Interface hl_lines=1-3"
pipeline_name: example_pipestat_pipeline
pipeline_type: sample
output_schema: pipeline_pipestat/pipestat_output_schema.yaml
command_template: >
  python {looper.piface_dir}/count_lines.py {sample.file} {sample.sample_name} {pipestat.results_file}

```



