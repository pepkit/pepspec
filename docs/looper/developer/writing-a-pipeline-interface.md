---
title: Pipeline interface specification
---

# Writing a pipeline interface

## Introduction

If you're interested in building a looper-compatible pipeline, or taking an existing pipeline and making it work with looper, the critical point of contact is the pipeline interface.
A pipeline interface *describes how to run a pipeline*.
Here is a basic walkthrough to write a simple interface file. Once you've been through this, you can consult the formal [pipeline interface format specification](pipeline-interface-specification.md) for further details and reference.

!!! success "Learning objectives"
    - What is a looper pipeline interface?
    - How do I write a looper pipeline interface for my custom pipeline?
    - Do I have to write a pipeline interface to have looper just run some command that isn't really a pipeline?


## Example

Let's start with a simple example:

```yaml title="pipeline_interface.yaml"
pipeline_name: count_lines
sample_interface:
  command_template: >
    {looper.piface_dir}/count_lines.sh {sample.file_path}
```

What's going on here?
First, looper needs to know the name of the pipeline so it can keep track of outputs of different pipelines.
In this case, we named the pipeline `count_lines`.
The pipeline name could be anything, as long as it is unique to the pipeline.
It will be used for communication and keeping track of which results belong to which pipeline.
Think of it as a unique identifier label you assign to the pipeline. 

Next, the `sample_interface` key.
This key tells looper (and pipestat) that this is a **sample-level pipeline.**
If this interface were describing a project-level pipeline, it would instead use `project_interface`.

!!! tip "Sample and project interfaces"
    Remember, looper distinguishes sample-level from project-level pipelines.
    This is explained in detail in [Advanced run options](../advanced-guide/advanced-run-options.md).
    Basically, sample-level pipelines run *once per sample*, whereas project-level pipelines run *once per project*.
    You can also write an interface with both a `sample_interface` and a `project_interface`.
    This would make sense to do for a pipeline that had two parts, one that you run independently for each sample, and a second one that aggregates all those sample results at the project level.

Under `sample_interface` (or `project_interface`) is the `command_template`, which holds our command string with variables that will be populated.
In this example, we will run (`count_lines.sh`) in the same directory as the pipeline interface file.
We will pass a single argument to the script, `{sample.file_path}`, which is a variable that will be populated with the `file_path` attribute on the sample.
This `file_path` field is arbitrary -- it is just an attribute for the sample, which corresponds to a column header in the sample table.
As the pipeline author, your command template can use any attributes with `{sample.<attribute>}` syntax.
You would just then define what attributes are necessary to run your pipeline.

You can make the command template much more complicated and refer to any sample or project attributes, as well as a bunch of [other variables made available by looper](../advanced-guide/advanced-computing.md#divvy-config-variable-adapters-and-built-in-looper-variables).

There are many more advanced features, such as providing a schema to specify inputs or outputs, making input-size-dependent compute settings, and more.
Let's walk through some of these more advanced options.

### Variable Templates via `var_templates`

You can use `var_templates` to render re-usable variables for use in the command template.

```yaml title="pipeline_interface.yaml"
pipeline_name: count_lines
var_templates:  
  pipeline: "{looper.piface_dir}/directory_of_pipelines/count_lines.sh"  
sample_interface:
  command_template: >
    {pipeline.var_templates.pipeline} {sample.file_path}
```


### Compute Variables

You can also utilize pipeline specific compute variables within the pipeline interface:


```yaml title="pipeline_interface.yaml"
pipeline_name: count_lines
var_templates:  
  pipeline: "{looper.piface_dir}/directory_of_pipelines/count_lines.sh"  
sample_interface:
  command_template: >
    {pipeline.var_templates.pipeline} {sample.file_path}
compute:
  size_dependent_variables: resources-sample.tsv
```

In this example we are pointing to a `.tsv` file that will determine the resources for each sample as needed.

For clarity here is an example `resources-sample.tsv` would look like:

```tsv title="resources-sample.tsv"
max_file_size cores mem time
0.05  1 16000 00-01:00:00
0.5   1 32000 00-01:00:00
1     1 56000 00-01:00:00
10    1 64000 00-01:00:00
NaN   1 64000 00-02:00:00

```


### Initialize generic pipeline interface

Each Looper project requires one or more pipeline interfaces that points to sample and/or project pipelines. You can run a command that will generate a generic pipeline interface, a generic output_schema.yaml (useful for pipestat compatible pipelines) and a generic pipeline to get you started:

```shell
looper init_piface
```

```console title="Output from looper init_piface"
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

## Example Pipeline Interface Using Pipestat

If you wish to use [pipestat](../tutorial/pipestat.md), you will need to provide an `output_schema`. Note that the pipeline name contained within this pipeline interface should match the one in the pipestat output schema.

```yaml
pipeline_name: example_pipestat_pipeline
output_schema: pipestat_output_schema.yaml
command_template: >
  python {looper.piface_dir}/count_lines.py {sample.file} {sample.sample_name} {pipestat.results_file}
```


For complete details, consult the formal [pipeline interface format specification](pipeline-interface-specification.md).
