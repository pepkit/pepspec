# Setting up a looper project

## Introduction

This guide will walk you through creating a Looper workspace to run a pipeline on a dataset.
Looper is ideal for processing data split into independent samples, allowing you to run the same pipeline in parallel on each sample.
In our demonstration, we'll work with three sample files, each representing a different country: Canada, Mexico, and Switzerland.
Each file contains a list of the states or provinces in that country.
In this context, each country is considered a "sample," and our goal is to run a pipeline on each sample.
The sample pipeline we’ll use is a shell script that counts the number of lines in its input file.
By running this pipeline, we’ll compute the number of states or provinces in each country.

After setting things up, it will be easy to launch all our jobs like this:

```sh
cd looper_csv_example
looper run
```

In a real workspace, you would likely have hundreds or thousands of samples, each with multiple input files.
Your pipeline could be an advanced Python or R script that takes hours or days to run.
The principles of setting up and running looper will be the same as for our simple demonstration project.

Let's get started!


!!! success "Learning objectives"
    - How do I get started using looper?
    - What components do I need to run looper?
    - What is a looper config file, a pipeline interface, and a metadata table?




## Components of a looper workspace

A typical Looper workspace includes the following components:

1. **Sample Data:** Usually stored as one or more files per sample.

2. **Sample Metadata:** A simple `.csv` file that describes the samples. Looper will run your pipeline once for each row in this table. In a future guide, we’ll explore how to leverage more advanced features of `PEP` to describe your samples.

3. **Pipeline:** The script or command you want to run on each sample file. You'll also need a *pipeline interface* file that tells looper how to execute the pipeline.

4. **Looper Configuration File:** This file points to the other components and includes any additional configuration options you want to pass to looper.

We'll walk through how to set up each of these components. If you'd rather skip the setup instructions, you can also download the files from the [hello world git repository](https://github.com/pepkit/hello_looper/tree/master/looper_csv_example), which have the files structured the way you'd get at the end of this tutorial. But we recommend following these instructions the first time because they will help you get a feel for the contents of the files.

## Step 1: Set up a directory

In practice, looper can handle any locations for any of the components, but to keep things simple in this tutorial, we'll create a root folder for all the components, split into subfolders for data, metadata, and pipeline.

```sh
mkdir looper_csv_example
cd looper_csv_example
```

## Step 2: Grab the data

First, we'll need some data. Download these 3 files and save them in a subfolder called `data/`:

```sh
mkdir data
wget mexico.txt  //TODO: Make these wget commands correct to raw files hosted on github
wget canada.txt
wget switzerland.txt
```

Take a peak at the contents of the files. They are each a simple list of the states or provinces of each country, with one per line, like this:

```sh
head data/mexico.txt -n 5

Aguascalientes
Baja California
Baja California Sur
Campeche
Chiapas
```

## Step 3: Create a metadata table

Looper needs a list of samples in the form of a sample metadata table, which names each sample and includes paths to the data files. Looper will accept a PEP, which we'll discuss more later, or just a simple CSV file, which is where we'll start. Create a new file called `metadata/sample_table.csv` and paste this content in it:

```csv  title="metadata/sample_table.csv"
sample_name,area_type,file_path
mexico,state,data/mexico.txt
switzerland,canton,data/switzerland.txt
canada,province,data/canada.txt
```

Each row corresponds to a sample, with a unique identifier under `sample_name`, a pointer to its corresponding file in `file_path`, and any other information you want to include about the sample (in this case, `area_type`). These will be the different values available to pass to your pipeline.

## Step 4: Create the pipeline

Our example pipeline is a shell script that counts the lines in an input file. Since our data has one line per province, this script will tell us how many provinces there are in each country. Create a file under `pipeline/count_lines.sh` with this content:

```sh title="pipeline/count_lines.sh"
#!/bin/bash
linecount=`wc -l $1 | sed -E 's/^[[:space:]]+//' | cut -f1 -d' '`
echo "Number of lines: $linecount"
```


All this script does is run the unix `wc` command, and then parse the output using `sed` and `cut`, and then print the result with `echo`.
In a real workspace, your pipeline is more likely to be a powerful Python script or something else.
The important thing for looper is just that there's a command you can run and to execute it. 
Since looper will need to execute it, make sure your script has execute permission:

```sh
chmod 755 pipeline/count_lines.sh
```


## Step 5: Create a pipeline interface

In order to run a pipeline, looper needs to know how to construct the command, which will be different for each sample.
A pipeline developer does this through the *pipeline interface*.
Our `count_lines.sh` pipeline just takes a single argument, which is the file path, so the command would be `count_lines.sh path/to/file.txt`.
Here's how to create the appropriate pipeline interface for this pipeline.
Create a file in `pipeline/pipeline_interface.yaml` and paste this content into it:

```yaml  title="pipeline/pipeline_interface.yaml"
pipeline_name: count_lines
sample_interface:
  command_template: >
    pipeline/count_lines.sh {sample.file_path}
```

This is the pipeline interface file.
It specifies the `pipeline_name`, which looper uses to keep track of pipelines in case it is running multiple of them.
It also specifies the `command_template`, which uses `{sample.file_path}` to tell looper to use the value of the `file_path` attribute on samples.
Later we'll cover more powerful features you can add to the pipeline interface.
For now, the important part is just that the `command_template` is telling looper how to run the `count_lines.sh` script we just created, passing it a single argument as a parameter, which it will get from the `file_path` column from the sample metadata table.

## Step 6: Create the looper config

Now you have all the components finished for your looper project.
The last step is to create the looper configuration file.
The easiest way to do this is to run `looper init` from within the root `my_looper_project` folder.
This will walk you through a wizard that will build the file for you.

Here's how to answer the questions

| Prompt                                      | You should respond:                      |
|---------------------------------------------|--------------------------------------|
| Project name: (new_csv)                     | (leave blank to accept the default)  |
| Registry path or file path to PEP: (databio/example) | metadata/sample_table.csv            |
| Path to output directory: (results)         | (leave blank to accept the default)  |
| Add each path to a pipeline interface: (pipeline_interface.yaml) | pipeline/pipeline_interface.yaml     |


This will create a file at `.looper.yaml`, with this content:

```yaml  title=".looper.yaml"
pep_config: metadata/sample_table.csv
output_dir: results
pipeline_interfaces:
  - pipeline/pipeline_interface.yaml
```

You could also just create this manually, but the `init` function makes it so you don't have to remember the config syntax. Now that that the project is configured, you can run it like this:

```sh
looper run
```

This will submit a job for each sample. That's basically all there is to it; after this, there's a lot of powerful options and tweaks you can do to control your jobs. Here we'll just mention a few of them.

- **Dry runs**. You can use `-d, --dry-run` to create the job submission scripts, but not actually run them. This is really useful for testing that everything is set up correctly before you commit to submitting hundreds of jobs.
- **Limiting the number of jobs**. You can `-l, --limit` to test a few before running all samples. You can also use the `--selector-*` arguments to select certain samples to include or exclude.
- **Grouping jobs**. You can use `-u, --lump`, `-n, --lumpn`, `-j, --lumpj` to group jobs. [More details on grouping jobs](../advanced-guide/advanced-run-options.md).
- **Changing compute settings**. You can use `-p, --package`, `-s, --settings`, or `--compute` to change the compute templates. Read more in [advanced computing](../advanced-guide/advanced-computing.md).
- **Time delay**. You can stagger submissions to not overload a submission engine using `--time-delay`.
- **Use rerun to resubmit jobs**. To run only jobs that previously failed, try `looper rerun`.
- **Tweak the command on-the-fly**. The `--command-extra` arguments allow you to pass extra arguments to every command straight through from looper. See [advanced run options](../advanced-guide/advanced-run-options.md).



!!! tip "Summary"
    - To use looper, you'll need to have data, metadata, a pipeline (with pipeline interface), and a looper configuration file. 
    - Looper is best suited for data that is split into samples, where you're trying to run a pipeline independently on each sample.
    - Once you've configured everything correctly, you run your samples with the command `looper run`.

