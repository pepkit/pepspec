# Setting up pipestat

## Introduction

In our previous tutorials, we deployed the `count_lines.sh` pipeline, calculated the number of provinces in several countries.
The result of the pipeline was simply printed into the log file.
In this tutorial, we'll demonstrate how to do much better than that, putting the result into either a structured file, a database, or into PEPhub.
We'll do this by introducing a new tool called `pipestat`.
Pipestat will help us record and retrieve pipeline results in a much cleaner way. 

Pipestat is a standalone tool.
It is not required to use looper, and it can also be used by pipelines that are not looper-compatible.
You can read the complete details about pipestat as a standalone tool in the [pipestat documentation](https://pep.databio.org/pipestat/).
However, using pipestat alongside looper unlocks a set of helpful tools such as html reports via `looper report`.
In this tutorial, we will wire up our simple pipeline with pipestat, and demonsrrate these powerful reporting tools.

!!! success "Learning objectives"
    - What is pipestat? Why is it useful?
    - How can I configure my looper workspace to use a pipestat-compatible pipeline effectively?
    - Where are pipestat results saved? Can I use other databases?
    - How can I make my pipeline store results in PEPhub?


## Set up a working directory

In this tutorial, we'll start with the files from the previous tutorial, and adjust them to use pipestat.
If you'd like the completed pipestat example, you can download the [pipestat_example](https://github.com/pepkit/hello_looper/tree/master/pipestat_example).
To begin, create a copy of the previous tutorial:

```sh
cd ..
cp -r pep_derived_attrs pipestat_example
rm -rf pipestat_example/results  # remove results folder
cd pipestat_example
```

## Adapt the pipeline to report results with pipestat

First, we need to introduce the idea of a [pipestat output schema](../../pipestat/pipestat-specification.md). 
An output schema defines the results a pipeline can report.
You can read more about pipestat output schemas in the [pipestat documentation](../../pipestat/pipestat-specification.md). 
For now, we'll make a simple output schema for our `count_lines.sh` pipeline, which reports a single result.
Create a new output schema in `pipeline/pipestat_output_schema.yaml` and paste this content into it:

```yaml  title="pipeline/pipestat_output_schema.yaml" hl_lines="9 10 11"
type: object
properties:
  pipeline_name: "default_pipeline_name"
  samples:
    type: array
    items:
      type: object
      properties:
        number_of_lines:
          type: integer
          description: "number of reported lines"
```

This file specifies what results are reported by a pipeline, and what _type_ they are.
It's actually a [JSON Schema](https://json-schema.org/), which allows us to use this file to validate the results.
But you don't need to worry about that for now.
What matters is that this example defines, for our `count_lines` pipeline, that there is one result, called `number_of_lines`, which is of type `integer`.
This is recorded under the `samples` array as a property of each sample, because your pipeline will report the `number_of_lines` for each sample.

Next, we'll update our `count_lines.sh` pipeline to make it use pipestat, instead of just logging the results to screen.
For a Python pipeline, pipestat can be called directly from within Python.
For any other pipeline, it can be used from the command-line.
Since our pipeline is a shell script, we'll use the `pipestat` CLI interface.
All we have to do is call pipestat to report the results of the pipeline.
Update the pipeline script to have the following code:

```sh title="pipeline/count_lines.sh" hl_lines="3"
#!/bin/bash
linecount=`wc -l $1 | sed -E 's/^[[:space:]]+//' | cut -f1 -d' '`
pipestat report -r $2 -i 'number_of_lines' -v $linecount -c $3
echo "Number of lines: $linecount"
```

We added one new line, which runs the `pipestat` and provides it with this information:
- `-r` provides the record identifier, which identifies the sample
- `-i` provides the ID of the result to report, as defined in the output schema (`number_of_lines`)
- `-v` provides the actual value we are reporting (`$linecount`)
- `-c` provides a path to a pipestat configuration file, which configures how the result is stored 


## Connect pipestat to looper

Since the sample name (`-r $2`) and the pipestat config file (`-c $3`) weren't previously passed to the pipeline, we need to adjust the pipeline interface, to make sure the command template specifies all the inputs our pipeline needs:

```yaml  title="pipeline/pipeline_interface.yaml" hl_lines="5"
pipeline_name: count_lines
output_schema: pipestat_output_schema.yaml
sample_interface:
  command_template: >
    pipeline/count_lines.sh {sample.file_path} {sample.sample_name} {pipestat.config_file}
```

This will pass the sample_name and the pipestat config file as additional arguments to the shell script as pipestat needs this information to report results. 
The `{sample.sample_name}` will just take the appropriate value from the sample table, just like we did previously with `{sample.file_path}`
The `{pipestat.config_file}` is automatically provided by looper.
Looper generates this config file based on the looper configuration and the pipeline interface.
To read more about pipestat config files, see here: [pipestat configuration](../../pipestat/config.md).

Next, we need to tell looper we're dealing with a pipestat-compatible pipeline. Specify this by adding the `output_schema` path to your pipeline interface:

```yaml  title="pipeline/pipeline_interface.yaml" hl_lines="2"
pipeline_name: count_lines
output_schema: pipestat_output_schema.yaml
sample_interface:
  command_template: >
    pipeline/count_lines.sh {sample.file_path}
```

Finally, we need to configure where the pipestat results will be stored.
Pipestat offers several ways to store results, including a simple file for a basic pipeline, or a relational database, or even PEPhub.
We'll start with the simplest option and configure pipestat to use a results file.
Configure pipestat through the looper config file like this:

```yaml  title=".looper.yaml" hl_lines="5-6"
pep_config: metadata/pep_config.yaml
output_dir: results
pipeline_interfaces:
  - pipeline/pipeline_interface.yaml
pipestat:
  results_file_path: results.yaml
```

This instructs looper to configure pipestat to store the results in a `.yaml` file.
Once this is done, you now have set up looper to report the pipeline results via `pipestat` into a `results.yaml` file.

Execute the run with:
```sh
looper run
```

You should now be able to navigate to the `results.yaml` file and see the reported results within.

!!! tip "Key Point"
    One of the remarkable things about this setup is that the result reports are decoupled from the pipeline. All the pipeline has to do is call `pipestat` with information about the same identifier, the name of the result, and the result value itself. There's no configuration of pipestat at the pipeline level. Instead, configuration of the results storage is passed through from the user's looper config file. This allows a user to change how the results are reported for any pipeline.


## A  Python based pipeline

If your pipeline is written in Python, using pipestat is even easier.
Looper can run a `.py` just as easily as a `.sh` file and, using pipestat's python API, can report results from within the `.py` file.

First, we will need to change our shell pipeline to a Python-based pipeline.
In the same folder as your `count_lines.sh`, create a new file `count_lines.py` and place the following code within:

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
    python3 pipeline/count_lines.py {sample.file_path} {sample.sample_name} {pipestat.results_file} {pipestat.output_schema}
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
    python3 pipeline/count_lines.py {sample.file_path} {sample.sample_name} {pipestat.config_file} {pipestat.output_schema}
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
pep_config: metadata/pep_config.yaml
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
looper report
```

This command will call `pipestat summarize` on the results located in your results location. In this case, the `results.yaml` file.

An example html report using `looper report` can be found here: [PEPATAC Gold Summary](https://pepatac.databio.org/en/latest/files/examples/gold/gold_summary.html)


## Reporting results back to PEPhub

As shown in the previous tutorial, Looper can process metadata from PEPhub using a path to a PEP on PEPhub. Using Looper + Pipestat integration, we can also report results back to PEPhub.

Create a new PEP on PEPHub to hold these results (in this case, let's use the demo example): `databio/pipestat_demo:default`

We must change our looper config file to no longer use a results file path. Instead, it will now use a pephub_url:
```yaml  title=".looper.yaml" hl_lines="6"
pep_config: metadata/pep_config.yaml
output_dir: results
pipeline_interfaces:
  - pipeline/pipeline_interface.yaml
pipestat:
  pephub_path: "databio/pipestat_demo:default"
  flag_file_dir: results/flags
```

The pipeline can remain the same as the last example. Looper will pass along the information in the generated pipestat config file. Pipestat will read the pephub_path from the config file and report results directly to the PEP!

## Create tables and stats summaries

Looper can also create pipeline stats summaries and object summaries as  `.tsv` and `.yaml` file respectively.
First, ensure Looper is properly set up to use pipestat and that pipeline results have been reported to the backend of choice.

Run:
```sh
looper table
```

You'll see a path output for each of the summary files:
```
Looper version: 2.0.0
Command: table
Using looper config (.looper.yaml).
Creating objects summary
'count_lines' pipeline stats summary (n=4): results/count_lines_stats_summary.tsv
'count_lines' pipeline objects summary (n=0): results/count_lines_objs_summary.yaml

```

## Create a folder of similar objects (symlinks)

Sometimes your pipeline may create many of the same file types (think images) and you'd like to peruse all of them. You can use `looper link` which will create a folder of similar objects for each sample in one location. Note: this does not create copies of the objects; it simply uses symlinks to achieve this.

To create a directory of linked objects:

```shell
looper link
```


!!! tip "Summary"
    - Pipestat is a standalone tool that can be used with or without looper.
    - Using Pipestat with Looper allows for helpful features such as status checking, html report generation, and reporting results to PEPhub.

