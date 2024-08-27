# Setting up pipestat

!!! success "Learning objectives"
    - What is pipestat? Why is it useful?
    - How can I configure my looper project to use pipestat effectively?
    - Where are pipestat results saved? Can I use other databases?
    - How can I make my pipeline store results in PEPhub?

## Introduction

Pipestat is a tool used by pipelines to standardize reporting of pipeline results. For example, we are using the `count_lines.sh` pipeline to calculate the number of provinces in several countries. This number is a result of the pipeline. Our previous pipelines record the result by printing to the screen and log file. Pipestat will help us collect and aggregate those results in a clean way. 

Pipestat is a standalone tool.
It is not required to use looper, and it can also be used by pipelines that are not looper-compatible. However, using pipestat alongside looper unlocks a set of helpful tools such as html reports via `looper report`.
You can read the complete details about pipestat in the [pipestat documentation](../../pipestat).
In this tutorial, we will wire up our simple pipeline with pipestat, and show how this lets us use powerful reporting tools to view pipeline results nicely.


## A Simple Shell Pipeline

Note: if you'd like the completed pipestat example, it can be downloaded directly here: [pipestat_example](https://github.com/pepkit/hello_looper/tree/master/pipestat_example)

## Set up a working directory
In our previous tutorials, we demonstrated using PEP to specify sample metadata. To begin using pipestat, let's create a copy of the previous tutorial:

```sh
cd ..
cp -r pep_derived_attrs pipestat_example
rm -rf pipestat_example/results  # remove results folder
cd pipestat_example
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

This will pass the sample_name and the pipestat config file as additional arguments to the shell script as pipestat needs this information to report results. Note: pipestat can be configured using a config file. When used with Looper, Looper generates this config file for the user based on items in the looper config and the pipeline interface, storing the location of this config file in `pipestat.config_file`. To read more about pipestat config files, see here: [pipestat configuration](../../pipestat/config.md).

To utilize these, you will also need to modify the shell script (pipeline) to run `pipestat` via the CLI:

```sh title="pipeline/count_lines.sh" hl_lines="3"
#!/bin/bash
linecount=`wc -l $1 | sed -E 's/^[[:space:]]+//' | cut -f1 -d' '`
pipestat report -r $2 -i 'number_of_lines' -v $linecount -c $3
echo "Number of lines: $linecount"
```

Modify the looper config file to give looper some additional information about pipestat regarding _where_ the results will be stored:

```yaml  title=".looper.yaml" hl_lines="5-6"
pep_config: metadata/sample_table.csv
output_dir: results
pipeline_interfaces:
  - pipeline/pipeline_interface.yaml
pipestat:
  results_file_path: results.yaml
```

In this case, we will store the results in a `.yaml` file.


Once this is done, you now have set up Looper to report the pipeline results via `pipestat` into a `results.yaml` file.

Execute the run with:
```sh
looper run
```

You should now be able to navigate to the `results.yaml` file and see the reported results within.

## A  Python based pipeline

Chances are that your pipeline is written in python. Looper can run a `.py` just as easily as a `.sh` file and, using pipestat's python API, can report results from within the `.py` file.

First, we will need to change our shell pipeline to a python base pipeline. In the same folder as your `count_lines.sh`, create a new file `count_lines.py` and place the following code within:

```python
import pipestat
import sys
import os.path

# Very simple pipeline that counts lines and reports the final count via pipestat

# Obtain arguments invoked during looper submission via command templates
text_file = sys.argv[1] 
sample_name = sys.argv[2]   # pipestat needs a unique sample identifier. Looper uses sample_name but pipestat uses record_identifier
results_file = sys.argv[3]  # this is the results.yaml file
schema_path = sys.argv[4]  # This is the output schema

# Create pipestat manager
psm = pipestat.PipestatManager(
    schema_path=schema_path,
    results_file_path=results_file,
    record_identifier=sample_name,
)

# Read text file
text_file = os.path.abspath(text_file)

#Count Lines
with open(text_file, "r") as f:
    result = {"number_of_lines": len(f.readlines())}

# Report Results using Pipestat
psm.report(record_identifier=sample_name, values=result)

```

You will also need to make changes to your pipeline interface. The command template will need to send variables on the CLI in the proper order such that the `count_lines.py` file can interpret them and use them in Pipestat:

```yaml  title="pipeline/pipeline_interface.yaml" hl_lines="5"
pipeline_name: count_lines
output_schema: pipestat_output_schema.yaml
sample_interface:
  command_template: >
    python3 {looper.piface_dir}/count_lines.py {sample.file} {sample.sample_name} {pipestat.results_file} {pipestat.output_schema}
```

Note: as with previous tutorials, you may need to change the permissions on the `count_lines.py` file:

```sh
chmod 755 pipeline/count_lines.py
```

Some key things to note: 
Our command template removed the configuration file as an argument and fed the results_file_path directly. However, we could've just as easily made our command template use the config file instead. Using a config file is important for more complex result backends such as databases.


```yaml  title="pipeline/pipeline_interface.yaml" hl_lines="5"
pipeline_name: count_lines
output_schema: pipestat_output_schema.yaml
sample_interface:
  command_template: >
    pipeline/count_lines.sh {sample.file_path} {sample.sample_name} {pipestat.config_file} {pipestat.output_schema}
```

```python hl_lines="17"
import pipestat
import sys
import os.path

# Very simple pipeline that counts lines and reports the final count via pipestat

# Obtain arguments invoked during looper submission via command templates
text_file = sys.argv[1] 
sample_name = sys.argv[2]   # pipestat needs a unique sample identifier. Looper uses sample_name but pipestat uses record_identifier
config_file_path = sys.argv[3]  # this is the config file path
schema_path = sys.argv[4]  # This is the output schema

# Create pipestat manager
psm = pipestat.PipestatManager(
    schema_path=schema_path,
    record_identifier=sample_name,
    config_file=config_file_path,
)

# Read text file
text_file = os.path.abspath(text_file)

#Count Lines
with open(text_file, "r") as f:
    result = {"number_of_lines": len(f.readlines())}

# Report Results using Pipestat
psm.report(record_identifier=sample_name, values=result)
```

Again, you can now run the example with:

```sh
looper run
```

## Setting and Checking Status

Another neat feature of looper's integration with pipestat is that it can be used to check the status of pipeline runs given that the pipeline utilizes pipestat to _set_ status flags. Looper cannot set status flags directly. It can only check the status of flags.

To use status flags, we must modify the pipeline to set the status and we must tell looper and pipestat where those status flags will live.

Modify the looper config file to set the flag status directory:

```yaml  title=".looper.yaml" hl_lines="7"
pep_config: metadata/sample_table.csv
output_dir: results
pipeline_interfaces:
  - pipeline/pipeline_interface.yaml
pipestat:
  results_file_path: results.yaml
  flag_file_dir: results/flags
```

This `flag_file_dir` will be passed along in the configuration file generated by Looper and sent to the pipeline via the command template. However, we must still modify our original pipeline by telling pipestat to set the status. This will generate a flag file in our flag file directory which can later be checked.

```python hl_lines="31"
import pipestat
import sys
import os.path

# Very simple pipeline that counts lines and reports the final count via pipestat

# Obtain arguments invoked during looper submission via command templates
text_file = sys.argv[1] 
sample_name = sys.argv[2]   # pipestat needs a unique sample identifier. Looper uses sample_name but pipestat uses record_identifier
config_file_path = sys.argv[3]  # this is the config file path
schema_path = sys.argv[4]  # This is the output schema

# Create pipestat manager
psm = pipestat.PipestatManager(
    schema_path=schema_path,
    record_identifier=sample_name,
    config_file=config_file_path,
)

# Read text file
text_file = os.path.abspath(text_file)

#Count Lines
with open(text_file, "r") as f:
    result = {"number_of_lines": len(f.readlines())}

# Report Results using Pipestat
psm.report(record_identifier=sample_name, values=result)

# Set status of pipeline for this specific sample at the completion of the pipeline
psm.set_status(record_identifier=sample_name, status_identifier="completed")
```

Run looper again: `looper run`

Now, pipestat will have set completed flags upon successful completion of the samples.

To check the status of all samples and see reported flag statuses, you can use the command:

```sh
looper check
```

## Generating an HTML Report

Finally, looper's integration with pipestat allows for the generation of a html report showing all the reported results.

Assuming you've been following along and have reported results previously, simply run:

```sh
looper run
```

This command will call `pipestat summarize` on the results located in your results location. In this case, the `results.yaml` file.


## Reporting results back to PEPhub

As shown in the previous tutorial, Looper can process metadata from PEPhub using a path to a PEP on PEPhub. Using Looper + Pipestat integration, we can also report results back to PEPhub.

Create a new PEP on PEPHub to hold these results (in this case, let's use the demo example): `databio/pipestat_demo:default`

We must change our looper config file to no longer use a results file path. Instead, it will now use a pephub_url:
```yaml  title=".looper.yaml" hl_lines="6"
pep_config: metadata/sample_table.csv
output_dir: results
pipeline_interfaces:
  - pipeline/pipeline_interface.yaml
pipestat:
  pephub_path: "databio/pipestat_demo:default"
  flag_file_dir: results/flags
```

The pipeline can remain the same as the last example. Looper will pass along the information in the generated pipestat config file. Pipestat will read the pephub_path from the config file and report results directly to the PEP!




!!! tip "Summary"
    - Pipestat is a standalone tool that can be used with or without looper.
    - Using Pipestat with Looper allows for helpful features such as status checking, html report generation, and reporting results to PEPhub.

