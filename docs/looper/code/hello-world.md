# Hello World! example for looper

This tutorial demonstrates how to install `looper` and use it to run a pipeline on a PEP project. 

## 1. Install the latest version of looper:

```console
pip install --user --upgrade looper
```

## 2. Download and unzip the hello_looper repository

The [hello looper repository](http://github.com/pepkit/hello_looper) contains a basic functional example project (in `/project`) and a looper-compatible pipeline (in `/pipeline`) that can run on that project. Let's download and unzip it:



```python
!wget https://github.com/pepkit/hello_looper/archive/refs/heads/master.zip
```

    --2023-11-08 17:27:01--  https://github.com/pepkit/hello_looper/archive/refs/heads/master.zip
    Resolving github.com (github.com)... 140.82.114.3
    Connecting to github.com (github.com)|140.82.114.3|:443... connected.
    HTTP request sent, awaiting response... 302 Found
    Location: https://codeload.github.com/pepkit/hello_looper/zip/refs/heads/master [following]
    --2023-11-08 17:27:01--  https://codeload.github.com/pepkit/hello_looper/zip/refs/heads/master
    Resolving codeload.github.com (codeload.github.com)... 140.82.113.10
    Connecting to codeload.github.com (codeload.github.com)|140.82.113.10|:443... connected.
    HTTP request sent, awaiting response... 200 OK
    Length: unspecified [application/zip]
    Saving to: ‘master.zip’
    
    master.zip              [ <=>                ]  13.37K  --.-KB/s    in 0.03s   
    
    2023-11-08 17:27:01 (472 KB/s) - ‘master.zip’ saved [13693]
    



```python
!unzip master.zip
```

    Archive:  master.zip
    73ef08e38d3e17fd3d4f940282c80e3ee4dbb91f
       creating: hello_looper-master/
      inflating: hello_looper-master/.gitignore  
      inflating: hello_looper-master/.looper.yaml  
      inflating: hello_looper-master/.looper_pephub.yaml  
      inflating: hello_looper-master/.looper_pipestat.yaml  
      inflating: hello_looper-master/.looper_pipestat_shell.yaml  
      inflating: hello_looper-master/README.md  
       creating: hello_looper-master/data/
      inflating: hello_looper-master/data/frog1_data.txt  
      inflating: hello_looper-master/data/frog2_data.txt  
      inflating: hello_looper-master/looper_pipelines.md  
       creating: hello_looper-master/old_specification/
      inflating: hello_looper-master/old_specification/README.md  
       creating: hello_looper-master/old_specification/data/
      inflating: hello_looper-master/old_specification/data/frog1_data.txt  
      inflating: hello_looper-master/old_specification/data/frog2_data.txt  
       creating: hello_looper-master/old_specification/pipeline/
      inflating: hello_looper-master/old_specification/pipeline/count_lines.sh  
      inflating: hello_looper-master/old_specification/pipeline/pipeline_interface.yaml  
       creating: hello_looper-master/old_specification/project/
      inflating: hello_looper-master/old_specification/project/project_config.yaml  
      inflating: hello_looper-master/old_specification/project/sample_annotation.csv  
       creating: hello_looper-master/pipeline/
      inflating: hello_looper-master/pipeline/count_lines.sh  
      inflating: hello_looper-master/pipeline/pipeline_interface.yaml  
      inflating: hello_looper-master/pipeline/pipeline_interface_project.yaml  
       creating: hello_looper-master/pipeline_pipestat/
      inflating: hello_looper-master/pipeline_pipestat/count_lines.py  
      inflating: hello_looper-master/pipeline_pipestat/count_lines_pipestat.sh  
      inflating: hello_looper-master/pipeline_pipestat/pipeline_interface.yaml  
      inflating: hello_looper-master/pipeline_pipestat/pipeline_interface_shell.yaml  
      inflating: hello_looper-master/pipeline_pipestat/pipestat_output_schema.yaml  
       creating: hello_looper-master/project/
      inflating: hello_looper-master/project/project_config.yaml  
      inflating: hello_looper-master/project/sample_annotation.csv  


## 3. Run it

Run it by changing to the directory and then invoking `looper run` on the project configuration file.


```python
!looper run --looper-config hello_looper-master/.looper.yaml
```

    Looper version: 1.5.2-dev
    Command: run
    Using default divvy config. You may specify in env var: ['DIVCFG']
    Pipestat compatible: False
    [36m## [1 of 2] sample: frog_1; pipeline: count_lines[0m
    /home/drc/GITHUB/looper/master/looper/docs_jupyter/hello_looper-master/pipeline/count_lines.sh data/frog1_data.txt
    Writing script to /home/drc/GITHUB/looper/master/looper/docs_jupyter/hello_looper-master/results/submission/count_lines_frog_1.sub
    Job script (n=1; 0.00Gb): /home/drc/GITHUB/looper/master/looper/docs_jupyter/hello_looper-master/results/submission/count_lines_frog_1.sub
    Compute node: databio
    Start time: 2023-11-08 17:29:45
    wc: data/frog1_data.txt: No such file or directory
    Number of lines: 
    [36m## [2 of 2] sample: frog_2; pipeline: count_lines[0m
    /home/drc/GITHUB/looper/master/looper/docs_jupyter/hello_looper-master/pipeline/count_lines.sh data/frog2_data.txt
    Writing script to /home/drc/GITHUB/looper/master/looper/docs_jupyter/hello_looper-master/results/submission/count_lines_frog_2.sub
    Job script (n=1; 0.00Gb): /home/drc/GITHUB/looper/master/looper/docs_jupyter/hello_looper-master/results/submission/count_lines_frog_2.sub
    Compute node: databio
    Start time: 2023-11-08 17:29:45
    wc: data/frog2_data.txt: No such file or directory
    Number of lines: 
    
    Looper finished
    Samples valid for job generation: 2 of 2
    Commands submitted: 2 of 2
    Jobs submitted: 2
    {'Pipestat compatible': False, 'Commands submitted': '2 of 2', 'Jobs submitted': 2}
    [0m

Voila! You've run your very first pipeline across multiple samples using `looper`!

# Exploring the results

Now, let's inspect the `hello_looper` repository you downloaded. It has 3 components, each in a subfolder:


```python
!tree hello_looper-master/*/
```

    hello_looper-master/data/
    ├── frog1_data.txt
    └── frog2_data.txt
    hello_looper-master/pipeline/
    ├── count_lines.sh
    └── pipeline_interface.yaml
    hello_looper-master/project/
    ├── project_config.yaml
    └── sample_annotation.csv
    
    0 directories, 6 files


These are:

 * `/data` -- contains 2 data files for 2 samples. These input files were each passed to the pipeline.
 * `/pipeline` -- contains the script we want to run on each sample in our project. Our pipeline is a very simple shell script named `count_lines.sh`, which (duh!) counts the number of lines in an input file.
 * `/project` -- contains 2 files that describe metadata for the project (`project_config.yaml`) and the samples (`sample_annotation.csv`). This particular project describes just two samples listed in the annotation file. These files together make up a [PEP](http://pep.databio.org)-formatted project, and can therefore be read by any PEP-compatible tool, including `looper`.




When we invoke `looper` from the command line we told it to `run project/project_config.yaml`. `looper` reads the [project/project_config.yaml](https://github.com/pepkit/hello_looper/blob/master/project/project_config.yaml) file, which points to a few things:

 * the [project/sample_annotation.csv](https://github.com/pepkit/hello_looper/blob/master/project/sample_annotation.csv) file, which specifies a few samples, their type, and path to data file
 * the `output_dir`, which is where looper results are saved. Results will be saved in `$HOME/hello_looper_results`.
 * the `pipeline_interface.yaml` file, ([pipeline/pipeline_interface.yaml](https://github.com/pepkit/hello_looper/blob/master/pipeline/pipeline_interface.yaml)), which tells looper how to connect to the pipeline ([pipeline/count_lines.sh](https://github.com/pepkit/hello_looper/blob/master/pipeline/)).

The 3 folders (`data`, `project`, and `pipeline`) are modular; there is no need for these to live in any predetermined folder structure. For this example, the data and pipeline are included locally, but in practice, they are usually in a separate folder; you can point to anything (so data, pipelines, and projects may reside in distinct spaces on disk). You may also include more than one pipeline interface in your `project_config.yaml`, so in a looper project, many-to-many relationships are possible.

## Looper config

The [looper config](looper-config.md) contains paths to the project config, the output_dir as well as any dfine pipeline interfaces. 


```python
!cat hello_looper-master/.looper.yaml
```

    pep_config: project/project_config.yaml # local path to pep config
    # pep_config: pepkit/hello_looper:default  # you can also use a pephub registry path
    output_dir: "results"
    pipeline_interfaces:
      sample: pipeline/pipeline_interface.yaml




## Project Config

The project config file contains the PEP version and sample annotation sheet. (see [defining a project](defining-a-project.md)).



```python
!cat hello_looper-master/project/project_config.yaml
```

    pep_version: 2.0.0
    sample_table: sample_annotation.csv


## Pipeline Interface

The [pipeline interface](pipeline-interface-specification.md) shows the pipeline_name, pipeline_type, as well as the var_templates and command_templates used for this pipeline.



```python
!cat hello_looper-master/pipeline/pipeline_interface.yaml
```

    pipeline_name: count_lines
    pipeline_type: sample
    var_templates:
      pipeline: '{looper.piface_dir}/count_lines.sh'
    command_template: >
      {pipeline.var_templates.pipeline} {sample.file}


Alright, next let's explore what this pipeline stuck into our `output_dir`:



```python
!tree $HOME/hello_looper_results
```

    /home/nsheff/hello_looper_results
    ├── results_pipeline
    └── submission
        ├── count_lines.sh_frog_1.log
        ├── count_lines.sh_frog_1.sub
        ├── count_lines.sh_frog_2.log
        ├── count_lines.sh_frog_2.sub
        ├── frog_1.yaml
        └── frog_2.yaml
    
    2 directories, 6 files



Inside of an `output_dir` there will be two directories:

- `results_pipeline` - a directory with output of the pipeline(s), for each sample/pipeline combination (often one per sample)
- `submissions` - which holds a YAML representation of each sample and a log file for each submitted job

From here to running hundreds of samples of various sample types is virtually the same effort!


## Running PEPs from PEPHub

Looper also supports running a PEP from [PEPHub](https://pephub.databio.org/)!


```python
!cat hello_looper-master/.looper_pephub.yaml
```

    pep_config: pepkit/hello_looper:default # pephub registry path or local path
    output_dir: results
    pipeline_interfaces:
      sample: pipeline/pipeline_interface.yaml



```python
!looper run --looper-config hello_looper-master/.looper_pephub.yaml
```

    Looper version: 1.5.2-dev
    Command: run
    Using default divvy config. You may specify in env var: ['DIVCFG']
    No config key in Project, or reading project from dict
    Processing project from dictionary...
    Pipestat compatible: False
    [36m## [1 of 2] sample: frog_1; pipeline: count_lines[0m
    /home/drc/GITHUB/looper/master/looper/docs_jupyter/hello_looper-master/pipeline/count_lines.sh data/frog1_data.txt
    Writing script to /home/drc/GITHUB/looper/master/looper/docs_jupyter/hello_looper-master/results/submission/count_lines_frog_1.sub
    Job script (n=1; 0.00Gb): /home/drc/GITHUB/looper/master/looper/docs_jupyter/hello_looper-master/results/submission/count_lines_frog_1.sub
    Compute node: databio
    Start time: 2023-11-09 15:39:28
    wc: data/frog1_data.txt: No such file or directory
    Number of lines: 
    [36m## [2 of 2] sample: frog_2; pipeline: count_lines[0m
    /home/drc/GITHUB/looper/master/looper/docs_jupyter/hello_looper-master/pipeline/count_lines.sh data/frog2_data.txt
    Writing script to /home/drc/GITHUB/looper/master/looper/docs_jupyter/hello_looper-master/results/submission/count_lines_frog_2.sub
    Job script (n=1; 0.00Gb): /home/drc/GITHUB/looper/master/looper/docs_jupyter/hello_looper-master/results/submission/count_lines_frog_2.sub
    Compute node: databio
    Start time: 2023-11-09 15:39:28
    wc: data/frog2_data.txt: No such file or directory
    Number of lines: 
    
    Looper finished
    Samples valid for job generation: 2 of 2
    Commands submitted: 2 of 2
    Jobs submitted: 2
    {'Pipestat compatible': False, 'Commands submitted': '2 of 2', 'Jobs submitted': 2}
    [0m

# Pipestat compatible configurations

Looper can also be used in tandem with [pipestat](https://pipestat.databio.org/en/latest/) to report pipeline results.


```python
!cat hello_looper-master/.looper_pipestat.yaml
```

    pep_config: ./project/project_config.yaml # pephub registry path or local path
    output_dir: ./results
    pipeline_interfaces:
      sample:  ./pipeline_pipestat/pipeline_interface.yaml
    pipestat:
      results_file_path: results.yaml


## A few more basic looper options

Looper also provides a few other simple arguments that let you adjust what it does. You can find a [complete reference of usage](usage.md) in the docs. Here are a few of the more common options:

For `looper run`:

- `-d`: Dry run mode (creates submission scripts, but does not execute them) 
- `--limit`: Only run a few samples 
- `--lumpn`: Run several commands together as a single job. This is useful when you have a quick pipeline to run on many samples and want to group them.

There are also other commands:

- `looper check`: checks on the status (running, failed, completed) of your jobs
- `looper summarize`: produces an output file that summarizes your project results
- `looper destroy`: completely erases all results so you can restart
- `looper rerun`: rerun only jobs that have failed.


## On your own

To use `looper` on your own, you will need to prepare 2 things: a **project** (metadata that define *what* you want to process), and **pipelines** (*how* to process data). To link your project to `looper`, you will need to [define a project](defining-a-project.md). You will want to either use pre-made `looper`-compatible pipelines or link your own custom-built pipelines. These docs will also show you how to connect your pipeline to your project.

