# Defining a looper config file

The looper configuration file contains important information about the looper project. It is named `.looper.yaml` by default and lives at the root of the project. 
It points to the PEP project (via `pep_config`). It allows the user to supply the pipeline interfaces.

Here is an example of a looper config file using local PEP and multiple pipeline interfaces:

```yaml
pep_config: $HOME/hello_looper-master/project/project_config.yaml
output_dir: "$HOME/hello_looper-master/output"
pipeline_interfaces:
    - pipeline/pipestat_pipeline_interface1.yaml
    - pipeline/pipestat_pipeline_interface2.yaml
```

In addition, looper supports projects from [PEPhub](https://pephub.databio.org/). 
Using a PEP from PEPhub allows a user to run a pipeline without downloading the PEP. This allows you to keep the sample table in a centralized, shared location. You need only specify all necessary
environment variables used by the PEP.

Example looper config file using PEPhub project. Note that the `pep_config` is a registry path from [PEPhub](https://pephub.databio.org/pepkit/hello_looper?tag=default):

```yaml
pep_config: pepkit/hello_looper:default
output_dir: "$HOME/hello_looper-master/output"
pipeline_interfaces:
    - pipeline/pipestat_pipeline_interface1.yaml
    - pipeline/pipestat_pipeline_interface2.yaml
```

Where:
- `output_dir` is pipeline output directory, where results will be saved.
- `pep_config` is a local config file or PEPhub registry path. (registry path should be specified in
one of supported ways: `namespace/name`, `namespace/name:tag`)
- `pipeline interfaces` is a local path to project or sample pipelines.

To run pipeline, go to the directory of .looper.config and execute command in your terminal:
`looper run --config {looper_config_path}` or `looper runp --config {looper_config_path}` (project-level pipeline).

## Run `looper init` tutorial to initialize a looper config
Looper contains a built-in guided tutorial for initializing looper configuration files and a generic pipeline interface.

Initialize looper config tutorial via the CLI:

```shell
looper init
```

This guided tutorial will ask you to supply:

    -  path to PEP config (project config)
    -  output directory 
    -  any pipeline interfaces

You can also generate a generic looper configuration file and edit it in a text editor.

Example output:

```shell
Looper initialization 
{
│   'pep_config': 'example/pep/path',
│   'output_dir': '.',
│   'pipeline_interfaces': [
│   │   'pipeline_interface1.yaml',
│   │   'pipeline_interface2.yaml'
│   ]
}
Initialized looper config file: /home/drc/PythonProjects/testing_perofrmance/testingperformance/.looper.yaml

```

## Initialize Generic Pipeline Interface
Each Looper project requires one or more pipeline interfaces that points to sample and/or project pipelines. You can run a command that will generate a generic pipeline interface to get you started:

```shell
looper init_piface
```


```shell
──────────  Pipeline Interface ──────────
{
│   'pipeline_name': 'default_pipeline_name',
│   'output_schema': 'output_schema.yaml',
│   'var_templates': {
│   │   'pipeline': '{looper.piface_dir}/count_lines.sh'
│   },
│   'sample_interface': {
│   │   'command_template': '{pipeline.var_templates.pipeline} {sample.file} --output-parent {looper.sample_output_folder}'
│   }
}
Pipeline interface successfully created at: /home/drc/PythonProjects/testing_perofrmance/testingperformance/pipeline/pipeline_interface.yaml
──────────  Output Schema ──────────
{
│   'pipeline_name': 'default_pipeline_name',
│   'samples': {
│   │   'number_of_lines': {
│   │   │   'type': 'integer',
│   │   │   'description': 'Number of lines in the input file.'
│   │   }
│   }
}
Output schema successfully created at: /home/drc/PythonProjects/testing_perofrmance/testingperformance/pipeline/output_schema.yaml
──────────  Example Pipeline Shell Script ──────────
#!/bin/bash
linecount=`wc -l $1 | sed -E 's/^[[:space:]]+//' | cut -f1 -d' '`
pipestat report -r $2 -i 'number_of_lines' -v $linecount -c $3
echo "Number of lines: $linecount"
    
count_lines.sh successfully created at: /home/drc/PythonProjects/testing_perofrmance/testingperformance/pipeline/count_lines.sh

```

## Customize looper

You can also customize things further. You can provide a `cli` keyword to specify any command line (CLI) options from within the looper config file. The subsections within this section direct the arguments to the respective `looper` subcommands. For example, to specify a sample submission limit for a `looper run` command, use:

```yaml
cli:
    run:
      limit: 2
```

Keys in the `cli.<subcommand>` section *must* match the long argument parser option strings, so `command-extra`, `limit`, `dry-run` and so on. For more CLI options refer to the subcommands [usage](usage.md).
