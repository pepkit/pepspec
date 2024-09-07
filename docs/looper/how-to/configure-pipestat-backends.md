# How to configure pipestat back-ends

## Introduction

In the basic [pipestat tutorial](tutorial/pipestat.md), we showed how to create a simple pipeline that could use pipestat to report results.
One of the powerful features of pipestat is that you can configure it to store results in different locations.
This document will cover more details about how to configure pipestat in looper:

!!! success "Learning objectives"
    - How do I configure pipestat to use different backends with looper?


## How looper configures pipestat

As looper processes samples and creates a job submission script, if `.looper.yaml` config file contains `pipestat` section, it creates a pipestat configuration file, which merges information found in 1. pipeline interface and 2. looper_config file.

Looper combines the necessary configuration data and writed a pipestat configuration for each pipeline interface. The configuration file is then used by the pipeline interface (and pipeline) to create a PipestatManager object. This instantiated PipestatManager object can then be used to report results.

To configure looper to use pipestat, you must

### 1. Add `pipestat` section to the looper config file.

The looper config file must contain a pipestat section.
This must supply information on where to store results, which is either a file path for a results file, database credentials if using a postgresql database backend, or PEPhub registry path. Here are 3 examples showing how to use configure pipestat to use different back-ends:

### File back-end

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

### Postgres SQL database back-end

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

### PEPhub back-end

```yaml title=".looper.yaml" hl_lines="7"
pep_config: project_config_pipestat.yaml # pephub registry path or local path
output_dir: results
pipeline_interfaces:
  - ./pipeline_interface1_sample_pipestat.yaml
pipestat:
  flag_file_dir: output/results_pipeline
  pephub_path: "databio/pipestat_demo:default"
```

### 2. The pipeline interface must include information required by pipestat such as pipeline_name, pipeline_type, and an output schema path:

```yaml title="pipeline_interface.yaml" hl_lines="1-3"
pipeline_name: example_pipestat_pipeline
pipeline_type: sample
output_schema: pipeline_pipestat/pipestat_output_schema.yaml
command_template: >
  python {looper.piface_dir}/count_lines.py {sample.file} {sample.sample_name} {pipestat.results_file}

```



## Project-level pipelines

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





!!! tip "Summary"
    - Configure pipestat through the `pipestat` section on the looper config.
    - You can control where the results of your pipeline are stored by configuring pipestat's back-end.



