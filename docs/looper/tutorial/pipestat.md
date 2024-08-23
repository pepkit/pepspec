# Setting up pipestat

## Introduction

Pipestat is a tool used by pipelines to standardize reporting of pipeline results. For example, we are using the `count_lines.sh` pipeline to calculate the number of provinces in several countries. This number is a result of the pipeline. Our previous pipelines record the result by printing to the screen and log file. Pipestat will help us collect and aggregate those results in a clean way. 

Pipestat is a standalone tool.
It is not required to use looper, and it can also be used by pipelines that are not looper-compatible.
You can read the complete details about pipestat in the [pipestat documentation](../../pipestat).
In this tutorial, we will wire up our simple pipeline with pipestat, and show how this lets use powerful reporting tools to view pipeline results nicely.

!!! success "Learning objectives"
    - What is pipestat? 
    - How can I configure my looper project to use pipestat effectively?
    - How can I make my pipeline store results in PEPhub?
    - Where are pipestat results saved? Can I use other databases?

## Set up a working directory
In our previous tutorials, we demonstrated using PEP to specify sample metadata. To begin using pipestat, let's create a copy of the previous tutorial:

```sh
cd ..
cp -r pep_derived_attrs pipestat_example
rm -rf pipestat_example/results  # remove results folder
```

First we need to take a look at and modify our pipeline interface in `pipeline/pipeline_interface.yaml` by adding an **output schema**:

While not strictly necessary, pipestat utilizes this output schema to define reported results. We should create a new file that defines an [output schema](../../pipestat/pipestat-specification.md).

Create a file in `pipeline/pipestat_output_schema.yaml` and paste this content into it:

```yaml  title="pipeline/pipestat_output_schema.yaml"
pipeline_name: count_lines
samples:
  number_of_lines:
    type: integer
    description: "Number of lines in the input file."
```

You can read more about pipestat output schemas in the [pipestat documentation](../../pipestat/pipestat-specification.md). However, for now know that this is a way to specify what results are to be reported by your pipeline and what _type_ they are.

Once you've created this file, you'll need to add it to your pipeline interface in `pipeline/pipeline_interface.yaml`.

```yaml  title="pipeline/pipeline_interface.yaml" hl_lines="2"
pipeline_name: count_lines
output_schema: pipestat_output_schema.yaml
sample_interface:
  command_template: >
    pipeline/count_lines.sh {sample.file_path}
```

Because this pipeline is a simple shell script, we will need to use the CLI version of pipestat and thus we will need to make some more additions.

In the command template, you'll need to add a couple of items:

```yaml  title="pipeline/pipeline_interface.yaml" hl_lines="5"
pipeline_name: count_lines
output_schema: pipestat_output_schema.yaml
sample_interface:
  command_template: >
    pipeline/count_lines.sh {sample.file_path} {sample.sample_name} {pipestat.config_file}
```

This will pass the sample_name and the pipestat config file as additional arguments to the shell script as pipestat needs this information to report results.

To utilize these, you will also need to modify the shell script (pipeline):

```sh title="pipeline/count_lines.sh" hl_lines="3"
#!/bin/bash
linecount=`wc -l $1 | sed -E 's/^[[:space:]]+//' | cut -f1 -d' '`
pipestat report -r $2 -i 'number_of_lines' -v $linecount -c $3
echo "Number of lines: $linecount"
```

Modify the looper config file to give looper some additional information about pipestat:

```yaml  title=".looper.yaml" hl_lines="5-6"
pep_config: metadata/sample_table.csv
output_dir: results
pipeline_interfaces:
  - ['pipeline/pipeline_interface.yaml']
pipestat:
  results_file_path: results.yaml
```



---

- Show how to add pipestat reporting to the count_lines script. (maybe with the shell version, and then the Python version? Or just go straight to Python? I see the advantage of doing both, because then you demonstrate the CLI of pipestat)
- Show how to report results back into the PEP at PEPhub
- Show how to use `looper check` with the pipestat-compatible pipeline
- Show how to use `looper report`.


!!! tip "Summary"
    - Pipestat is a standalone tool that can be used with or without looper.
    - ...
    - ...

