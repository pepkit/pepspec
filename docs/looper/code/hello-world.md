# Hello World! example for looper

This tutorial demonstrates how to install `looper` and use it to run a pipeline on a PEP project. 

## 1. Install the latest version of looper:

```console
pip install --user --upgrade looper
```

## 2. Download and unzip the hello_looper repository

The [hello looper repository](http://github.com/pepkit/hello_looper) contains a basic functional example project (in `/project`) and a looper-compatible pipeline (in `/pipeline`) that can run on that project. Let's download and unzip it:



```python
!wget https://github.com/pepkit/hello_looper/archive/refs/heads/dev.zip
```

    --2024-07-08 18:58:59--  https://github.com/pepkit/hello_looper/archive/refs/heads/dev.zip
    Resolving github.com (github.com)... 140.82.112.4
    Connecting to github.com (github.com)|140.82.112.4|:443... connected.
    HTTP request sent, awaiting response... 302 Found
    Location: https://codeload.github.com/pepkit/hello_looper/zip/refs/heads/dev [following]
    --2024-07-08 18:59:00--  https://codeload.github.com/pepkit/hello_looper/zip/refs/heads/dev
    Resolving codeload.github.com (codeload.github.com)... 140.82.114.10
    Connecting to codeload.github.com (codeload.github.com)|140.82.114.10|:443... connected.
    HTTP request sent, awaiting response... 200 OK
    Length: unspecified [application/zip]
    Saving to: ‘dev.zip’
    
    dev.zip                 [ <=>                ]  21.28K  --.-KB/s    in 0.09s   
    
    2024-07-08 18:59:01 (224 KB/s) - ‘dev.zip’ saved [21793]
    



```python
!unzip dev.zip
```

    Archive:  dev.zip
    2e840c22a2148fa941a7ecf987853bb768d40b3d
       creating: hello_looper-dev/
      inflating: hello_looper-dev/.gitignore  
      inflating: hello_looper-dev/.looper.yaml  
      inflating: hello_looper-dev/README.md  
       creating: hello_looper-dev/advanced/
      inflating: hello_looper-dev/advanced/.looper.yaml  
      inflating: hello_looper-dev/advanced/.looper_advanced_pipestat.yaml  
       creating: hello_looper-dev/advanced/pipeline/
     extracting: hello_looper-dev/advanced/pipeline/col_pipeline1.py  
     extracting: hello_looper-dev/advanced/pipeline/col_pipeline2.py  
     extracting: hello_looper-dev/advanced/pipeline/other_pipeline2.py  
      inflating: hello_looper-dev/advanced/pipeline/output_schema.yaml  
     extracting: hello_looper-dev/advanced/pipeline/pipeline1.py  
      inflating: hello_looper-dev/advanced/pipeline/pipeline_interface1_project.yaml  
      inflating: hello_looper-dev/advanced/pipeline/pipeline_interface1_sample.yaml  
      inflating: hello_looper-dev/advanced/pipeline/pipeline_interface2_project.yaml  
      inflating: hello_looper-dev/advanced/pipeline/pipeline_interface2_sample.yaml  
      inflating: hello_looper-dev/advanced/pipeline/pipestat_output_schema.yaml  
      inflating: hello_looper-dev/advanced/pipeline/pipestat_pipeline_interface1_sample.yaml  
      inflating: hello_looper-dev/advanced/pipeline/pipestat_pipeline_interface2_sample.yaml  
      inflating: hello_looper-dev/advanced/pipeline/readData.R  
      inflating: hello_looper-dev/advanced/pipeline/resources-project.tsv  
      inflating: hello_looper-dev/advanced/pipeline/resources-sample.tsv  
       creating: hello_looper-dev/advanced/project/
      inflating: hello_looper-dev/advanced/project/annotation_sheet.csv  
      inflating: hello_looper-dev/advanced/project/project_config.yaml  
       creating: hello_looper-dev/csv/
      inflating: hello_looper-dev/csv/.looper.yaml  
       creating: hello_looper-dev/csv/data/
      inflating: hello_looper-dev/csv/data/frog1_data.txt  
      inflating: hello_looper-dev/csv/data/frog2_data.txt  
       creating: hello_looper-dev/csv/pipeline/
      inflating: hello_looper-dev/csv/pipeline/count_lines.sh  
      inflating: hello_looper-dev/csv/pipeline/pipeline_interface.yaml  
       creating: hello_looper-dev/csv/project/
      inflating: hello_looper-dev/csv/project/sample_annotation.csv  
       creating: hello_looper-dev/intermediate/
      inflating: hello_looper-dev/intermediate/.looper.yaml  
       creating: hello_looper-dev/intermediate/data/
      inflating: hello_looper-dev/intermediate/data/frog_1.txt  
      inflating: hello_looper-dev/intermediate/data/frog_2.txt  
       creating: hello_looper-dev/intermediate/pipeline/
      inflating: hello_looper-dev/intermediate/pipeline/count_lines.sh  
      inflating: hello_looper-dev/intermediate/pipeline/pipeline_interface.yaml  
       creating: hello_looper-dev/intermediate/project/
      inflating: hello_looper-dev/intermediate/project/project_config.yaml  
      inflating: hello_looper-dev/intermediate/project/sample_annotation.csv  
       creating: hello_looper-dev/minimal/
      inflating: hello_looper-dev/minimal/.looper.yaml  
       creating: hello_looper-dev/minimal/data/
      inflating: hello_looper-dev/minimal/data/frog_1.txt  
      inflating: hello_looper-dev/minimal/data/frog_2.txt  
       creating: hello_looper-dev/minimal/pipeline/
      inflating: hello_looper-dev/minimal/pipeline/count_lines.sh  
      inflating: hello_looper-dev/minimal/pipeline/pipeline_interface.yaml  
       creating: hello_looper-dev/minimal/project/
      inflating: hello_looper-dev/minimal/project/project_config.yaml  
      inflating: hello_looper-dev/minimal/project/sample_annotation.csv  
       creating: hello_looper-dev/pephub/
      inflating: hello_looper-dev/pephub/.looper.yaml  
       creating: hello_looper-dev/pephub/data/
      inflating: hello_looper-dev/pephub/data/frog1_data.txt  
      inflating: hello_looper-dev/pephub/data/frog2_data.txt  
       creating: hello_looper-dev/pephub/pipeline/
      inflating: hello_looper-dev/pephub/pipeline/count_lines.sh  
      inflating: hello_looper-dev/pephub/pipeline/pipeline_interface.yaml  
       creating: hello_looper-dev/pipestat/
      inflating: hello_looper-dev/pipestat/.looper.yaml  
      inflating: hello_looper-dev/pipestat/.looper_pipestat_shell.yaml  
       creating: hello_looper-dev/pipestat/data/
      inflating: hello_looper-dev/pipestat/data/frog_1.txt  
      inflating: hello_looper-dev/pipestat/data/frog_2.txt  
       creating: hello_looper-dev/pipestat/pipeline_pipestat/
      inflating: hello_looper-dev/pipestat/pipeline_pipestat/count_lines.py  
      inflating: hello_looper-dev/pipestat/pipeline_pipestat/count_lines_pipestat.sh  
      inflating: hello_looper-dev/pipestat/pipeline_pipestat/pipeline_interface.yaml  
      inflating: hello_looper-dev/pipestat/pipeline_pipestat/pipeline_interface_shell.yaml  
      inflating: hello_looper-dev/pipestat/pipeline_pipestat/pipestat_output_schema.yaml  
       creating: hello_looper-dev/pipestat/project/
      inflating: hello_looper-dev/pipestat/project/project_config.yaml  
      inflating: hello_looper-dev/pipestat/project/sample_annotation.csv  


## 3. Run it

Run it by changing to the directory and then invoking `looper run` on the project configuration file.


```python
cd hello_looper-dev/minimal
```

    /home/drc/GITHUB/pepspec/docs/looper/notebooks/hello_looper-dev/minimal


    /home/drc/GITHUB/pepspec/.venv/lib/python3.10/site-packages/IPython/core/magics/osm.py:417: UserWarning: This is now an optional IPython functionality, setting dhist requires you to install the `pickleshare` library.
      self.shell.db['dhist'] = compress_dhist(dhist)[-100:]



```python
!looper run --config .looper.yaml
```

    Looper version: 2.0.0a1
    Command: run
    Using default divvy config. You may specify in env var: ['DIVCFG']
    [36m## [1 of 2] sample: frog_1; pipeline: count_lines[0m
    Writing script to /home/drc/GITHUB/pepspec/docs/looper/notebooks/hello_looper-dev/minimal/results/submission/count_lines_frog_1.sub
    Job script (n=1; 0.00Gb): /home/drc/GITHUB/pepspec/docs/looper/notebooks/hello_looper-dev/minimal/results/submission/count_lines_frog_1.sub
    Compute node: databio
    Start time: 2024-07-08 19:01:59
    Number of lines: 4
    [36m## [2 of 2] sample: frog_2; pipeline: count_lines[0m
    Writing script to /home/drc/GITHUB/pepspec/docs/looper/notebooks/hello_looper-dev/minimal/results/submission/count_lines_frog_2.sub
    Job script (n=1; 0.00Gb): /home/drc/GITHUB/pepspec/docs/looper/notebooks/hello_looper-dev/minimal/results/submission/count_lines_frog_2.sub
    Compute node: databio
    Start time: 2024-07-08 19:01:59
    Number of lines: 7
    
    Looper finished
    Samples valid for job generation: 2 of 2
    {'Pipestat compatible': False, 'Commands submitted': '2 of 2', 'Jobs submitted': 2}
    [0m

Voila! You've run your very first pipeline across multiple samples using `looper`!

# Exploring the results

Now, let's inspect the `hello_looper` repository you downloaded. It has 3 components, each in a subfolder:


```python
!tree *
```

    [01;34mdata[0m
    ├── frog_1.txt
    └── frog_2.txt
    [01;34mpipeline[0m
    ├── [01;32mcount_lines.sh[0m
    └── pipeline_interface.yaml
    [01;34mproject[0m
    ├── project_config.yaml
    └── sample_annotation.csv
    [01;34mresults[0m
    └── [01;34msubmission[0m
        ├── count_lines_frog_1.log
        ├── count_lines_frog_1.sub
        ├── count_lines_frog_2.log
        └── count_lines_frog_2.sub
    
    1 directory, 4 files


These are:

 * `/data` -- contains 2 data files for 2 samples. These input files were each passed to the pipeline.
 * `/pipeline` -- contains the script we want to run on each sample in our project. Our pipeline is a very simple shell script named `count_lines.sh`, which (duh!) counts the number of lines in an input file.
 * `/project` -- contains 2 files that describe metadata for the project (`project_config.yaml`) and the samples (`sample_annotation.csv`). This particular project describes just two samples listed in the annotation file. These files together make up a [PEP](http://pep.databio.org)-formatted project, and can therefore be read by any PEP-compatible tool, including `looper`.




When we invoke `looper` from the command line we told it to `run project/project_config.yaml`. `looper` reads the [project/project_config.yaml](https://github.com/pepkit/hello_looper/blob/master/project/project_config.yaml) file, which points to:

 * the [project/sample_annotation.csv](https://github.com/pepkit/hello_looper/blob/dev/project/sample_annotation.csv) file, which specifies a few samples, their type, and path to data file

The 3 folders (`data`, `project`, and `pipeline`) are modular; there is no need for these to live in any predetermined folder structure. For this example, the data and pipeline are included locally, but in practice, they are usually in a separate folder; you can point to anything (so data, pipelines, and projects may reside in distinct spaces on disk).

## Looper config

The [looper config](looper-config.md) contains paths to the project config, the output_dir as well as any defined pipeline interfaces. 


```python
!cat .looper.yaml
```

    pep_config: project/project_config.yaml # local path to pep config
    # pep_config: pepkit/hello_looper:default  # you can also use a pephub registry path
    output_dir: "results"
    pipeline_interfaces:
      - pipeline/pipeline_interface.yaml




## Project Config

The project config file contains the PEP version and sample annotation sheet. (see [defining a project](defining-a-project.md)).



```python
!cat project/project_config.yaml
```

    pep_version: 2.0.0
    sample_table: sample_annotation.csv

## Pipeline Interface

The [pipeline interface](pipeline-interface-specification.md) shows the pipeline_name, as well as the var_templates and command_templates used for this pipeline.



```python
!cat pipeline/pipeline_interface.yaml
```

    pipeline_name: count_lines
    var_templates:
      pipeline: '{looper.piface_dir}/count_lines.sh'
    sample_interface:
      command_template: >
        {pipeline.var_templates.pipeline} {sample.file}


Alright, next let's explore what this pipeline stuck into our `output_dir`:



```python
!tree results/
```

    [01;34mresults/[0m
    └── [01;34msubmission[0m
        ├── count_lines_frog_1.log
        ├── count_lines_frog_1.sub
        ├── count_lines_frog_2.log
        └── count_lines_frog_2.sub
    
    1 directory, 4 files



Inside of an `output_dir` there will be one to two directories:

- `submissions` - which holds a YAML representation of each sample and a log file for each submitted job
- `results_pipeline` - a directory with output of the pipeline(s) (if applicable), for each sample/pipeline combination (often one per sample). In this minimal example, the output was simply printed to terminal instead of producing files.

From here to running hundreds of samples of various sample types is virtually the same effort!



## A few more basic looper options

Looper also provides a few other simple arguments that let you adjust what it does. You can find a [complete reference of usage](usage.md) in the docs. Here are a few of the more common options:

For `looper run`:

- `-d`: Dry run mode (creates submission scripts, but does not execute them) 
- `--limit`: Only run a few samples 
- `--lumpn`: Run several commands together as a single job. This is useful when you have a quick pipeline to run on many samples and want to group them.

There are also other commands:

- `looper check`: checks on the status (running, failed, completed) of your jobs (requires pipestat)
- `looper summarize`: produces an output file that summarizes your project results (requires pipestat)
- `looper destroy`: completely erases all results so you can restart
- `looper rerun`: rerun only jobs that have failed.


## On your own

To use `looper` on your own, you will need to prepare 2 things: a **project** (metadata that define *what* you want to process), and **pipelines** (*how* to process data). To link your project to `looper`, you will need to [define a project](defining-a-project.md). You will want to either use pre-made `looper`-compatible pipelines or link your own custom-built pipelines. These docs will also show you how to connect your pipeline to your project.



```python

```
