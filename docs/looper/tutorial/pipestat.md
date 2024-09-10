# Setting up pipestat

## Introduction

In our previous tutorials, we deployed the `count_lines.sh` pipeline.
The result of that pipeline was the number of provinces in several countries, which was simply printed into the log file.
In a real-life pipeline, we usually don't just want to dig results out of log files.
What if we want to *do* something with the pipeline result, like put it into an aggregated results file, or a database, or into PEPhub?
In this tutorial, we'll demonstrate how to do that.
We'll do this with [pipestat](../../pipestat/README.md), another component in PEPkit.

Like the other PEPkit components, pipestat is a standalone tool.
You can read the complete details about pipestat as a standalone tool in the [pipestat documentation](https://pep.databio.org/pipestat/).
You can use pipestat without using looper, and vice versa, but using pipestat alongside looper unlocks a set of helpful tools such as html reports via `looper report`.
Pipestat will help us record and retrieve pipeline results in a much cleaner way. 
In this tutorial, we will wire up our simple pipeline with pipestat, and demonstrate these powerful reporting tools.

!!! success "Learning objectives"
    - What is pipestat? Why is it useful?
    - How can I configure my looper workspace to use a pipestat-compatible pipeline effectively?
    - Can looper monitor whether my jobs are still running, failed, or already completed?
    - Where are pipestat results saved? How can I store results of my pipeline somewhere else?
    - How can I make my pipeline store results in PEPhub?


## Set up a working directory

In this tutorial, we'll start with the files from the previous tutorial, and adjust them to use pipestat.
If you'd like the completed pipestat example, you can download the [pipestat_example](https://github.com/pepkit/hello_looper/tree/master/pipestat_example) from the hello_looper repo.
Otherwise, you can follow along to create all the necessary files.
To begin, create a copy of the previous tutorial:

```sh
cd ..
cp -r pep_derived_attrs pipestat_example
rm -rf pipestat_example/results  # remove results folder
cd pipestat_example
```

## Create a pipestat output schema

First, we need a [pipestat output schema](../../pipestat/pipestat-specification.md). 
An output schema tells pipestat what results a pipeline can report.
We'll start with a simple output schema for our `count_lines.sh` pipeline, which reports a single result.
Create a file named `pipeline/pipestat_output_schema.yaml` and paste this content into it:

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
It's actually a [JSON Schema](https://json-schema.org/), which allows us to use this file to validate the results, which we'll cover later.
What matters now is that this schema says our `count_lines` pipeline produces one result, called `number_of_lines`, which is of type `integer`.
This is recorded under the `samples` array as a property of each sample, because your pipeline will report the `number_of_lines` for each sample.

## Adapt the pipeline to report results with pipestat

Next, we'll update our `count_lines.sh` pipeline to make it use pipestat, instead of just logging the results to screen.
For a Python pipeline, pipestat can be called directly from within Python, but `count_lines.sh` is a shell script, so we'll use the `pipestat` CLI interface.
All we have to do is call pipestat to report the results of the pipeline, which we do by adding one line to the pipeline script:

```sh title="pipeline/count_lines.sh" hl_lines="3"
#!/bin/bash
linecount=`wc -l $1 | sed -E 's/^[[:space:]]+//' | cut -f1 -d' '`
pipestat report -r $2 -i 'number_of_lines' -v $linecount -c $3
echo "Number of lines: $linecount"
```

We added one new line, which runs `pipestat` and provides it with this information:

- `-r` provides the record identifier, which identifies the sample
- `-i` provides the ID (or key) of the result to report, as defined in the output schema (`number_of_lines`)
- `-v` provides the actual value we are reporting (the number of lines, `$linecount`)
- `-c` provides a path to a pipestat configuration file, which configures how the result is stored 


## Connect pipestat to looper

Next, we need to update our pipeline interface so looper passes all the necessary information to the pipeline.
Since the sample name (`-r $2`) and the pipestat config file (`-c $3`) weren't previously passed to the pipeline, we need to adjust the pipeline interface, to make sure the command template specifies all the inputs our pipeline needs:

```yaml  title="pipeline/pipeline_interface.yaml" hl_lines="5"
pipeline_name: count_lines
output_schema: pipestat_output_schema.yaml
sample_interface:
  command_template: >
    pipeline/count_lines.sh {sample.file_path} {sample.sample_name} {pipestat.config_file}
```

Now, looper will pass the sample_name and the pipestat config file as additional arguments to `count_lines.sh`.
The `{sample.sample_name}` will just take the appropriate value from the sample table, just like we did previously with `{sample.file_path}`
The `{pipestat.config_file}` is automatically provided by looper.
Looper generates this config file based on the looper configuration and the pipeline interface.
To read more about pipestat config files, see here: [pipestat configuration](../../pipestat/config.md).

Next, we need to tell looper we're dealing with a pipestat-compatible pipeline. Specify this by adding the `output_schema` in the pipeline interface to the pipestat output schema we created earlier:

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
Looper will now configured the pipeline to report results into a `results.yaml` file.

Execute the run with:
```sh
looper run
```

You should now be able to navigate to the `results.yaml` file and see the reported results within.
Now that you have your first pipestat pipeline configured with looper, there's lot of other, more powerful things you can add to make this even more useful.
For example, now that looper knows the structure of results your pipeline reports, it can automatically generate beautiful, project-wide results summary HTML pages for you.
It also provides some ability to monitor jobs and make sure they are all succeeding.
But before we get into the details of these advanced features, we'll take a small detour now to show you how to wire up pipestat to a Python pipeline, instead of a shell script.



!!! tip "Key Point"
    One of the remarkable things about this setup is that the result reports are decoupled from the pipeline. All the pipeline has to do is call `pipestat`  and provide the sample identifier, the key of the result, and the result value. There's no configuration of pipestat at the pipeline level; instead, configuration of the results storage is passed through from the user's looper config file. This allows a user to change how the results are reported for any pipeline. We've basically shifted the task of where to store pipeline results from the pipeline author (who usually handles that) to the pipeline user (who actually cares about that).





## A  Python-based pipeline

If your pipeline is written in Python, using pipestat is even easier.
Looper can run a `.py` just as easily as a `.sh` file and, using pipestat's python API, can report results from within the `.py` file.

First, we will need to change our shell pipeline to a Python-based pipeline.
In the same folder as your `count_lines.sh`, create a new file `count_lines.py` with this code:

```python
import pipestat
import sys
import os.path

# Very simple pipeline that counts lines and reports the final count via pipestat

# Obtain arguments invoked during looper submission via command templates
text_file = sys.argv[1] 
sample_name = sys.argv[2]   # pipestat needs a unique sample identifier. Looper uses sample_name but pipestat uses record_identifier
results_file = sys.argv[3]  # the results.yaml file
schema_path = sys.argv[4]  # the output schema

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

Make sure `count_lines.py` is executable:

```sh
chmod 755 pipeline/count_lines.py
```

Now, you need to update the pipeline interface to reflect the pipeline change:

```yaml  title="pipeline/pipeline_interface.yaml" hl_lines="5"
pipeline_name: count_lines
output_schema: pipestat_output_schema.yaml
sample_interface:
  command_template: >
    python3 pipeline/count_lines.py {sample.file_path} {sample.sample_name} {pipestat.results_file} {pipestat.output_schema}
```

In this example, the command template removed the configuration file as an argument and fed the results_file_path directly.
However, we could've just as easily made our command template use the config file instead.
Using the config file would allow more complex result backends such as databases.


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

## Generating result reports

### HTML reports

Now comes the fun part: the reason we want to go to the work of specifying the results in the pipestat output schema, and then reporting them using pipestat, is that this will structure them in a way that we can easily read and aggregate them.
Looper provides an easy `report` command that creates an html report of all reported results.
You've already configured everything above.
To get the report, simply run:

```sh
looper report
```

This command will call `pipestat summarize` on the results located in your results location. In this case, the `results.yaml` file.

Here is an example html report for the above tutorial examples: [count lines report](../count_lines_report/index.html)

A more advanced example of an html report using `looper report` can be found here: [PEPATAC Gold Summary](https://pepatac.databio.org/en/latest/files/examples/gold/gold_summary.html)

### Create tables and stats summaries

Having a nice HTML-browsable record of results is great for human browsing, but you may also want the aggregated results in a machine-readable form for downstream analysis.
Looper can also create summaries in a computable format as  `.tsv` and `.yaml` files.

Run:
```sh
looper table
```

This will produce a `.tsv` file for aggregated primitive results (integers, strings, etc), as well as a `.yaml` file for any aggregated *object* results:
```
Looper version: 2.0.0
Command: table
Using looper config (.looper.yaml).
Creating objects summary
'count_lines' pipeline stats summary (n=4): results/count_lines_stats_summary.tsv
'count_lines' pipeline objects summary (n=0): results/count_lines_objs_summary.yaml

```



## Reporting results back to PEPhub

In the previous tutorial, you configured looper to read sample metadata from PEPhub.
Now, by adding in pipestat integration, we can also report pipeline results *back* to PEPhub.
But first, you'll need to create your own PEP on PEPHub to hold these results.
You won't be able to report the results back to the demo repository because you don't have permissions.
In this example, we'll report the results back to the the demo PEP we used earlier, `databio/pipestat_demo:default`.
You can run this section yourself by replacing that with the registry path to a PEP you control.

To configure pipestat to report results to PEPhub instead of to a file, we just change our looper config to point to a pephub_url:

```yaml  title=".looper.yaml" hl_lines="6"
pep_config: metadata/pep_config.yaml
output_dir: results
pipeline_interfaces:
  - pipeline/pipeline_interface.yaml
pipestat:
  pephub_path: "databio/pipestat_demo:default"
  flag_file_dir: results/flags
```

No other changes are necessarily.
You will have to authenticate with PEPhub using `phc login`, and then looper will pass along the information in the generated pipestat config file.
Pipestat will read the `pephub_path` from the config file and report results directly to PEPhub using its API!


## Setting and checking status

Besides reporting results, another feature of pipestat is that it allows users to set pipeline *status*.
If your pipeline uses pipestat to set status flags, then looper can be used to check the status of pipeline runs.
Let's modify the pipeline to set status:

```python hl_lines="20 21 33 34"
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

# Set status for this sample to 'running'
psm.set_status(record_identifier=sample_name, status_identifier="running")

# Read text file
text_file = os.path.abspath(text_file)

# Count lines
with open(text_file, "r") as f:
    result = {"number_of_lines": len(f.readlines())}

# Report Results using Pipestat
psm.report(record_identifier=sample_name, values=result)

# Set status for this sample to 'completed'
psm.set_status(record_identifier=sample_name, status_identifier="completed")
```

This function creates a flag file in our flag file directory that indicates the status of the current sample.
When the pipeline begins, pipestat sets the status to 'running'.
When the pipeline completes, pipestat sets the status to 'completed'.
Looper will be able to read these flags to tell us how many jobs are running and completed.

One last thing: we should modify the looper config file to set pipestat's "flag file directory".
This `flag_file_dir` will be passed along in the configuration file generated by looper:


```yaml  title=".looper.yaml" hl_lines="7"
pep_config: metadata/pep_config.yaml
output_dir: results
pipeline_interfaces:
  - pipeline/pipeline_interface.yaml
pipestat:
  results_file_path: results.yaml
  flag_file_dir: results/flags
```

Now, the pipeline is configured to set pipestat status flags.
Run looper again: `looper run`. Then, to check the status of all samples, use:

```sh
looper check
```

For this example, the 'running' flag doesn't really help because the pipeline runs so fast that it immediately finishes.
But in a pipeline that will take minutes or hours to complete, it can be useful to know how many and which jobs are running.
That's why `looper check` can be helpful for these long-running pipelines.



!!! info "Do I have to use pipestat?"
    No. You can use looper just as we did in the first two tutorials to run any command.
    Often, you'll want to use looper to run an existing pipeline that you didn't create.
    In that case, you won't have the option of using pipestat, since you're unlikely to go to the effort of adapting someone else's pipeline to use it.
    For non-pipestat-compatible pipelines, you can still use looper to run pipelines, but you won't be able to use `looper report` or `looper check` to manage their output.
    
    **What benefits does pipestat give me?**
    If you *are* developing your own pipeline, then you might want to consider using pipestat in your pipeline.
    This will users to use `looper check` to check on the status of pipelines.
    It will also enable `looper report` and `looper table` to create summarized outputs of pipeline results.
    




## Create a folder of similar objects (symlinks)

Sometimes your pipeline may create many of the same file types (think images) and you'd like to peruse all of them. You can use `looper link` which will create a folder of similar objects for each sample in one location. Note: this does not create copies of the objects; it simply uses symlinks to achieve this.

To create a directory of linked objects:

```shell
looper link
```


!!! tip "Summary"
    - Pipestat is a standalone tool that can be used with or without looper.
    - Pipestat standardizes reporting of pipeline results. It provides a standard specification for how pipeline outputs should be stored; and an implementation to easily write results to that format from within Python or from the command line.
    - A pipeline user can configure a pipestat-compatible pipeline to record results in a file, in a database, or in PEPhub.
    - Looper synergizes with pipestat to add powerful features such as checking job status and generating html reports.

