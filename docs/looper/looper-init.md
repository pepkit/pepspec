# Initializing Looper

Looper contains a built-in guided tutorial for initializing looper configuration files and a generic pipeline interface.


### Initialize looper config


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
Would you like to follow a guided tutorial?  Y / n...

Selection: n
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


### Initialize Generic Pipeline Interface
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

### Setting up your PEP

Looper requires your samples to be in PEP format. Here is a simple example: https://pep.databio.org/spec/simple-example/

#### Example PEP Project Config

```yaml
pep_version: 2.0.0
sample_table: sample_annotation.csv
```
#### Example sample table
```csv
sample_name,library,file,toggle
frog_1,anySampleType,data/frog_1.txt,1
frog_2,anySampleType,data/frog_2.txt,1
```
