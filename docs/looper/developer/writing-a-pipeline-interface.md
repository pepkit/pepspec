---
title: Pipeline interface specification
---

# Writing a pipeline interface

## Introduction

If you're interested in building a looper-compatible pipeline, or taking an existing pipeline and making it work with looper, the critical point of contact is the pipeline interface.
A pipeline interface *describes how to run a pipeline*.
If you're using *existing* looper-compatible pipelines, you don't need to create a new interface; just point your looper configuration file at the one that comes with the pipeline.
You only need to write a new pipeline interface file if you're creating a *new* looper-compatible pipeline.

Here is a walkthrough to write a pipeline interface. Once you've been through this, you can consult the formal [pipeline interface format specification](pipeline-interface-specification.md) for further details and reference.

!!! success "Learning objectives"
    - What is a looper pipeline interface?
    - How do I write a looper pipeline interface for my custom pipeline?
    - Do I have to write a pipeline interface to have looper just run some command that isn't really a pipeline?


### A simple pipeline interface example

Each Looper project requires one or more pipeline interfaces that points to sample and/or project pipelines. Let's revisit the simple pipeline interface the `count_lines` pipeline example:

```yaml title="pipeline_interface.yaml"
pipeline_name: count_lines
sample_interface:
  command_template: >
    pipeline/count_lines.sh {sample.file_path}
```

What's going on here?
This file tells looper how to run the pipeline.
There are only 2 required keys.
First, the `pipeline_name` can be anything, as long as it is unique to the pipeline.
It will be used for communication and keeping track of which results belong to which pipeline.
Think of it as a unique identifier label you assign to the pipeline.

Second, the `sample_interface` tells looper (and pipestat) that this is a **sample-level pipeline.**
Under `sample_interface` is the `command_template`, which holds our command string with variables that will be populated.
In this example, looper will run `pipeline/count_lines.sh`.
Looper will pass a single argument to the script, `{sample.file_path}`, which is a variable that will be populated with the `file_path` attribute on the sample.
This `file_path` field which corresponds to a column header in the sample table.
As the pipeline author, your command template can use any attributes with `{sample.<attribute>}` syntax.
You can make the command template much more complicated and refer to any sample or project attributes, as well as a bunch of [other variables made available by looper](../advanced-guide/advanced-computing.md#divvy-config-variable-adapters-and-built-in-looper-variables).

That's all you need for a basic pipeline interface!
But there's also a lot more you can do, such as providing a schema to specify inputs or outputs, making input-size-dependent compute settings, and more.
Let's walk through some of these more advanced options.

### Initialize generic pipeline interface

So you don't have to remember the general syntax, you can run a command that will create a generic pipeline interface, a generic `output_schema.yaml` (for pipestat-compatible pipelines) and a generic pipeline to get you started:

```shell
looper init_piface
```


<!-- 

The `output_schema` is used if you are using pipestat to report results.
If you are not using pipestat, you can remove this line. -->


### Making pipeline interface portable with `{looper.piface_dir}`

One of the problems with the above pipeline interface is that it is hard-coding a relative path to the pipeline, `pipeline/count_lines.sh`:


```yaml title="pipeline_interface.yaml" hl_lines="4"
pipeline_name: count_lines
sample_interface:
  command_template: >
    pipeline/count_lines.sh {sample.file_path}
```

Looper will literally run `pipeline/count_lines.sh`, which will only work if looper is running from the working directory one level above the script, located in a `pipeline` subfolder.
In other words, this pipeline interface will only work if `looper` (and its resulting jobs) are run from inside a specific working directory.
Often this works, since we typically call `looper run` from our looper workspace folder, where the `.looper.yaml` config file lives.
But still, it would be better if the jobs could run correctly from any working directory.

One way we could do that is to hard-code the absolute path to the script.
Then, the resulting commands could run from anywhere on that system.

```yaml title="pipeline_interface.yaml" hl_lines="4"
pipeline_name: count_lines
sample_interface:
  command_template: >
    /absolute/path/to/pipeline/count_lines.sh {sample.file_path}
```

But then this pipeline interface this would not be portable.
It could not be shared with another user on a different system.

Another solution is that we could just put the pipeline command into our shell `PATH`.
This way, it would run correctly from any folder, and would work on any system.
But then users of our pipeline would have to adjust their `PATH`, which is also not ideal.

Luckily, looper offers a better solution. 
It is more convenient to specify a relative paths that is relative to the pipeline interface file, which looper can populate as needed.
For this purpose, looper provides the `{looper.piface_dir}` variable.
The pipeline interface author can make any paths portable by simply prepending that in a template.

Our improved pipeline interface looks like this:

```yaml title="pipeline_interface.yaml" hl_lines="4"
pipeline_name: count_lines
sample_interface:
  command_template: >
    {looper.piface_dir}/pipeline/count_lines.sh {sample.file_path}
```

Looper will automatically populate `{looper.piface_dir}` on the system with the absolute path, giving us the best of both worlds.
The pipeline script can be distributed alongside the pipeline interface, and this will automatically work from any working directory, on any system.

Therefore, we recommend pipeline authors always use `{looper.piface_dir}` to make sure their pipeline interfaces are portable.
This is also true for pre-submit command templates.

### Parameterizing job templates by sample through size-dependent variables

Next, let's cover a better way to modulate pipeline computing parameters by sample.
In the `count_lines` tutorials, we showed how to paramterize a job submission template via the `compute` section in the pipeline interface file, like this:

```yaml  title="pipeline/pipeline_interface.yaml" hl_lines="5 6 7 8 9"
pipeline_name: count_lines
sample_interface:
  command_template: >
    {looper.piface_dir}/pipeline/count_lines.sh {sample.file_path}
compute:
  partition: standard
  time: '01-00:00:00'
  cores: '32'
  mem: '32000'
```

This allows a job submission template to use computing variables like `{CORES}` and `{MEM}`, so you can control cluster resources.
The problem with this is that it provides the same compute parameters for every sample.
It's common to need to increase memory usage for a larger sample.
Looper provides a simple but powerful way to configure pipelines depending on the input size of the samples.

Replace the `compute` variables with a single variable, `size_dependent_variables`, which points to a `.tsv` file:

```yaml title="pipeline_interface.yaml" hl_lines="2"
compute:
  partition: standard
  size_dependent_variables: resources-sample.tsv
```

Then, create `resources-sample.tsv` with these contents:

```tsv title="resources-sample.tsv"
max_file_size cores mem time
0.05  1 16000 00-01:00:00
0.5   1 32000 00-01:00:00
1     1 56000 00-01:00:00
10    1 64000 00-01:00:00
NaN   1 64000 00-02:00:00
```

In this example, the `partition` will remain constant for all samples, but the `cores`, `mem`, and `time` variables will be modulated by sample file size.
For each sample, looper will select the best-fit row, which is the row whose `max_file_size` value is the largest value that does not exceed the actual input file size of the sample, in gigabytes.
This allows a pipeline author to specify different computing requirements depending on the size of the input sample. 

We recommend pipeline authors configure their pipeline interfaces with appropriate `size_dependent_variables` file, which should be distributed alongside the pipeline interface.


### Adding pre-submission commands to your pipeline run

Sometimes we need to run a set-up task *before* submitting the main pipeline.
Looper handles this through a [pre-submission hook system](pre-submission-hooks.md).

Looper provides several built-in hooks that do things like write out the sample information in different ways, which can be useful for different types of pipeline.
If your pipeline would benefit from one of these representations, all you need to do is add a reference to the plugin into the pipeline interface, like this:

```yaml title="pipeline_interface.yaml"
pre_submit:
  python_functions:
    - looper.write_sample_yaml
```

This will instruct looper to engage this plugin.
You can also parameterize the plugin by adding other variables into the pipeline interface.
Consult the plugin documentation for more details about how to parameterize the  plugins.

You can also write your own custom plugins, which can be as simple as a shell script, or they could be Python functions.
Here's an example of a Python script that will be executed through the command-line:


```yaml title="pipeline_interface.yaml"
pre_submit:
  command_templates:
    - "{looper.piface_dir}/hooks/script.py --genome {sample.genome} --log-file {looper.output_dir}/log.txt"
```

Looper will run this command before running each job, allowing you to create little set-up scripts to prepare things before a full job is run.

### Project-level pipeline interfaces

Remember, looper distinguishes sample-level from project-level pipelines.
This is explained in detail in [Advanced run options](../advanced-guide/advanced-run-options.md) with a specific example of running a project-level pipeline in the [pipestat tutorial](../tutorial/pipestat.md/#running-project-level-pipelines).
Basically, sample-level pipelines run *once per sample*, whereas project-level pipelines run *once per project*.
If this interface were describing a project-level pipeline, we would change out `sample_interface` to `project_interface`.

```yaml title="pipeline_interface.yaml" hl_lines="2"
pipeline_name: count_lines
project_interface:
  command_template: '{looper.piface_dir}/count_lines.sh
```

You can also write an interface with both a `sample_interface` and a `project_interface`.
This would make sense to do for a pipeline that had two parts, one that you run independently for each sample, and a second one that aggregates all those sample results at the project level.


!!! tip "Summary"
    - You can initialize and modify a generic pipeline interface using `looper init_piface`.
    - You should make your pipeline interfaces portable by using `{looper.piface_dir}`.
    - Pipeline-specific and sample-specific compute variables can be added to the pipeline interface to set items such as memory and number of cpus during the pipeline run.
    - You can specify pre-submission hooks for job setup in the pipeline interface.



