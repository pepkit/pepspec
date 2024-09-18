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


### Initialize generic pipeline interface

Each Looper project requires one or more pipeline interfaces that points to sample and/or project pipelines. You can run a command that will generate a generic pipeline interface, a generic output_schema.yaml (useful for pipestat compatible pipelines) and a generic pipeline to get you started:

```shell
looper init_piface
```

We can inspect our simple, generic example:

`cat pipeline_interface.yaml`


```yaml title="pipeline_interface.yaml"
pipeline_name: count_lines
output_schema: output_schema.yaml
var_templates:
  pipeline: '{looper.piface_dir}/count_lines.sh'
sample_interface:
  command_template: '{pipeline.var_templates.pipeline} {sample.file} --output-parent {looper.sample_output_folder}'
```

What's going on here?
First, looper needs to know the name of the pipeline so it can keep track of outputs of different pipelines.
The pipeline name could be anything, as long as it is unique to the pipeline.
It will be used for communication and keeping track of which results belong to which pipeline.
Think of it as a unique identifier label you assign to the pipeline.

The `output_schema` field is useful if you are using pipestat to report results. If you are not using pipestat, you can remove this line from your own pipeline interface.

We will come back to the `var_templates` in a moment. First, we must discuss the `sample_interface` key.

This key tells looper (and pipestat) that this is a **sample-level pipeline.**
If this interface were describing a project-level pipeline, it would instead use `project_interface`.

!!! tip "Sample and project interfaces"
    Remember, looper distinguishes sample-level from project-level pipelines.
    This is explained in detail in [Advanced run options](../advanced-guide/advanced-run-options.md) and a specific example of running a project-level pipeline can be found here under the [pipestat tutorial](../tutorial/pipestat/#running-project-level-pipelines).
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

Let us circle back to the `var_templates` key. You can use `var_templates` to render re-usable variables for use in the command template.

```yaml title="pipeline_interface.yaml" hl_lines="3 4"
pipeline_name: count_lines
output_schema: output_schema.yaml
var_templates:
  pipeline: '{looper.piface_dir}/count_lines.sh'
sample_interface:
  command_template: {pipeline.var_templates.pipeline} {sample.file} --output-parent {looper.sample_output_folder}
```

You can add anything to the var_templates that you need to later access in the command templates:
```yaml title="pipeline_interface.yaml"
pipeline_name: count_lines
var_templates:  
  pipeline: '{looper.piface_dir}/count_lines.sh' 
  refgenie_config: "$REFGENIE"
sample_interface:
  command_template: >
    {pipeline.var_templates.pipeline} --config {pipeline.var_templates.refgenie_config} {sample.file_path} --output-parent {looper.sample_output_folder}
```


### Adding compute variables to the pipeline interface

Sometimes, you may want to modify compute variables for a specific pipeline, e.g. adding a specific memory requirement.
Therefore, you can also utilize pipeline specific compute variables within the pipeline interface:


```yaml title="pipeline_interface.yaml"
pipeline_name: count_lines
var_templates:  
  pipeline: "{looper.piface_dir}/directory_of_pipelines/count_lines.sh"  
sample_interface:
  command_template: >
    {pipeline.var_templates.pipeline} {sample.file_path}
compute:
  cores: '32'
  mem: '32000'
```

In this example, we are specifying that the pipeline run will require 32 cores and 32 gigabytes of memory.

We can add other items as well, such as the HPC partition to run our pipeline, and the maximum time to allot for the run.:

```yaml title="pipeline_interface.yaml"
compute:
  cores: '32'
  mem: '32000'
  partition: standard
  time: '01-00:00:00'
```
Finally, you can even point to a `.tsv` file that will determine the resources for each sample as needed.

```yaml title="pipeline_interface.yaml"
compute:
  cores: '32'
  mem: '32000'
  partition: standard
  time: '01-00:00:00'
  size_dependent_variables: resources-sample.tsv
```

For clarity here is an example `resources-sample.tsv` would look like:

```tsv title="resources-sample.tsv"
max_file_size cores mem time
0.05  1 16000 00-01:00:00
0.5   1 32000 00-01:00:00
1     1 56000 00-01:00:00
10    1 64000 00-01:00:00
NaN   1 64000 00-02:00:00

```

For complete details, consult the formal [pipeline interface format specification](pipeline-interface-specification.md).


!!! tip "Summary"
    - You learned how to initialize and modify a generic pipeline interface using `looper init_piface`. 
    - Using var_templates can easily allow you to re-use the same variables within your command template. 
    - Pipeline specific compute variables can be added to the pipeline interface to set items such as memory and number of cpus during the pipeline run.