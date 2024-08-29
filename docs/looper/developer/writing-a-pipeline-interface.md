---
title: Pipeline interface specification
---

# Writing a pipeline interface

## Introduction

If you're interested in making a pipeline looper-compatible, the critical point of contact is the pipeline interface.
A pipeline interface *describes how to run a pipeline*.
Here is a basic walkthrough to write a simple interface file. Once you've been through this, you can consult the formal [pipeline interface format specification](pipeline-interface-specification.md) for further details and reference.

!!! success "Learning objectives"
    - What is a looper pipeline interface?
    - How do I write a looper pipeline interface for my custom pipeline?


## Example

Let's start with a simple example:

```yaml title="pipeline_interface.yaml"
pipeline_name: count_lines
sample_interface:
  command_template: >
    {looper.piface_dir}/count_lines.sh {sample.file_path}
```

What's going on here? Well, we need to supply the interface with a pipeline name. In this case, because our script counts lines, we'll just use that for the name. The pipeline name could be anything. It will be used for messaging and communication. 

Next, we have a command template which is nested under the `sample_interface` key. This key tells looper (and pipestat) that this is a **sample-level pipeline.** Note, we can use `project_interface` for project-level pipelines.

Within the `command_template` our command string contains a combination of variables that can be populated from the various [looper namespaces](../advanced-guide/advanced-computing.md#divvy-config-variable-adapters-and-built-in-looper-variables) (looper, sample, pipestat, etc).

In the above example, we are telling the command to run the script (`count_lines.sh`) found in the looper pipeline interface directory and to execute it on the current sample's file_path. Note that `file_path` is an attribute for the sample. This is generally a columns (`file_path`) in the sample table specified in the PEP.

You can make the command template much more complicated and refer to any sample or project attributes, as well as a bunch of [other variables made available by looper](../advanced-guide/advanced-computing.md#divvy-config-variable-adapters-and-built-in-looper-variables).

Now, you have a basic functional pipeline interface. There are many more advanced features you can use to make your pipeline more powerful, such as providing a schema to specify inputs or outputs, making input-size-dependent compute settings, and more. For complete details, consult the formal [pipeline interface format specification](pipeline-interface-specification.md).


Next, let's walk through some of these more advanced options.


### Variable Templates via `var_templates`
You can utilize `var_templates` to render re-usable variables for use in the command template.

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


### Initialize Generic Pipeline Interface

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
pipeline_type: sample
output_schema: pipestat_output_schema.yaml
command_template: >
  python {looper.piface_dir}/count_lines.py {sample.file} {sample.sample_name} {pipestat.results_file}
```

