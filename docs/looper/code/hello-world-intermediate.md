# Hello World Intermediate and Advanced Examples

This tutorial assumes you have already followed the Simple Hello World example in the previous example.

Assuming you have already downloaded and unzipped the examples from hello looper.

Ensure you are in the `hello_looper-dev/intermediate` folder.

e.g.



```python
cd hello_looper-dev/intermediate
```

    /home/drc/GITHUB/pepspec/docs/looper/notebooks/hello_looper-dev/intermediate


    /home/drc/GITHUB/pepspec/.venv/lib/python3.10/site-packages/IPython/core/magics/osm.py:417: UserWarning: This is now an optional IPython functionality, setting dhist requires you to install the `pickleshare` library.
      self.shell.db['dhist'] = compress_dhist(dhist)[-100:]



```python
!pwd
```

    /home/drc/GITHUB/pepspec/docs/looper/notebooks/hello_looper-dev/intermediate


The contents of this looper project is very similar to the minimal example.


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
    
    0 directories, 2 files


You can run the project via:


```python
!looper run -c .looper.yaml
```

    Looper version: 2.0.0a1
    Command: run
    Using default divvy config. You may specify in env var: ['DIVCFG']
    [36m## [1 of 2] sample: frog_1; pipeline: count_lines[0m
    Writing script to /home/drc/GITHUB/pepspec/docs/looper/notebooks/hello_looper-dev/intermediate/results/submission/count_lines_frog_1.sub
    Job script (n=1; 0.00Gb): /home/drc/GITHUB/pepspec/docs/looper/notebooks/hello_looper-dev/intermediate/results/submission/count_lines_frog_1.sub
    Compute node: databio
    Start time: 2024-07-08 19:16:03
    Number of lines: 4
    [36m## [2 of 2] sample: frog_2; pipeline: count_lines[0m
    Writing script to /home/drc/GITHUB/pepspec/docs/looper/notebooks/hello_looper-dev/intermediate/results/submission/count_lines_frog_2.sub
    Job script (n=1; 0.00Gb): /home/drc/GITHUB/pepspec/docs/looper/notebooks/hello_looper-dev/intermediate/results/submission/count_lines_frog_2.sub
    Compute node: databio
    Start time: 2024-07-08 19:16:03
    Number of lines: 7
    
    Looper finished
    Samples valid for job generation: 2 of 2
    {'Pipestat compatible': False, 'Commands submitted': '2 of 2', 'Jobs submitted': 2}
    [0m

However, in this example, we've utilized `sample_modifiers` within the PEP


```python
!cat project/project_config.yaml
```

    pep_version: 2.0.0
    sample_table: sample_annotation.csv
    sample_modifiers:
      derive:
        attributes: [file]
        sources:
          source1: "data/{sample_name}.txt"

Looking at the samples, we can see an additional column vs the minimal example:


```python
!cat project/sample_annotation.csv
```

    sample_name,library,file,toggle
    frog_1,anySampleType,source1,1
    frog_2,anySampleType,source1,1


By harnessing the PEP specification, Looper can extend the PEP during sample submission, adding flexibility to the project.

## More Advanced Examples


```python
cd ..
```

    /home/drc/GITHUB/pepspec/docs/looper/notebooks



```python
cd hello_looper-dev/advanced
```

    /home/drc/GITHUB/pepspec/docs/looper/notebooks/hello_looper-dev/advanced



```python
!tree -a
```

    [01;34m.[0m
    ├── .looper_advanced_pipestat.yaml
    ├── .looper.yaml
    ├── [01;34mpipeline[0m
    │   ├── col_pipeline1.py
    │   ├── col_pipeline2.py
    │   ├── other_pipeline2.py
    │   ├── output_schema.yaml
    │   ├── pipeline1.py
    │   ├── pipeline_interface1_project.yaml
    │   ├── pipeline_interface1_sample.yaml
    │   ├── pipeline_interface2_project.yaml
    │   ├── pipeline_interface2_sample.yaml
    │   ├── pipestat_output_schema.yaml
    │   ├── pipestat_pipeline_interface1_sample.yaml
    │   ├── pipestat_pipeline_interface2_sample.yaml
    │   ├── readData.R
    │   ├── resources-project.tsv
    │   └── resources-sample.tsv
    └── [01;34mproject[0m
        ├── annotation_sheet.csv
        └── project_config.yaml
    
    2 directories, 19 files


Similarly, you can run one of the looper projects within. Let's take a look at the advanced example using pipestat, a results reporter that looper can use when submitting pipelines.


```python
!looper run -c .looper_advanced_pipestat.yaml
```

    Looper version: 2.0.0a1
    Command: run
    Using default divvy config. You may specify in env var: ['DIVCFG']
    Initializing results file '/home/drc/GITHUB/pepspec/docs/looper/notebooks/hello_looper-dev/advanced/results/example_pipestat_pipeline/results.yaml'
    File does not exist, but create_file is true. Creating...
    [36m## [1 of 6] sample: sample1; pipeline: example_pipestat_pipeline[0m
    Calling pre-submit function: looper.write_sample_yaml
    Writing script to /home/drc/GITHUB/pepspec/docs/looper/notebooks/hello_looper-dev/advanced/results/submission/example_pipestat_pipeline_sample1.sub
    Job script (n=1; 0.00Gb): /home/drc/GITHUB/pepspec/docs/looper/notebooks/hello_looper-dev/advanced/results/submission/example_pipestat_pipeline_sample1.sub
    Compute node: databio
    Start time: 2024-07-08 19:32:28
    [36m## [2 of 6] sample: sample1; pipeline: example_pipestat_pipeline[0m
    Calling pre-submit function: looper.write_sample_yaml
    Writing script to /home/drc/GITHUB/pepspec/docs/looper/notebooks/hello_looper-dev/advanced/results/submission/example_pipestat_pipeline_sample1.sub
    Job script (n=1; 0.00Gb): /home/drc/GITHUB/pepspec/docs/looper/notebooks/hello_looper-dev/advanced/results/submission/example_pipestat_pipeline_sample1.sub
    Compute node: databio
    Start time: 2024-07-08 19:32:29
    [36m## [3 of 6] sample: sample2; pipeline: example_pipestat_pipeline[0m
    Calling pre-submit function: looper.write_sample_yaml
    Writing script to /home/drc/GITHUB/pepspec/docs/looper/notebooks/hello_looper-dev/advanced/results/submission/example_pipestat_pipeline_sample2.sub
    Job script (n=1; 0.00Gb): /home/drc/GITHUB/pepspec/docs/looper/notebooks/hello_looper-dev/advanced/results/submission/example_pipestat_pipeline_sample2.sub
    Compute node: databio
    Start time: 2024-07-08 19:32:31
    [36m## [4 of 6] sample: sample2; pipeline: example_pipestat_pipeline[0m
    Calling pre-submit function: looper.write_sample_yaml
    Writing script to /home/drc/GITHUB/pepspec/docs/looper/notebooks/hello_looper-dev/advanced/results/submission/example_pipestat_pipeline_sample2.sub
    Job script (n=1; 0.00Gb): /home/drc/GITHUB/pepspec/docs/looper/notebooks/hello_looper-dev/advanced/results/submission/example_pipestat_pipeline_sample2.sub
    Compute node: databio
    Start time: 2024-07-08 19:32:32
    [36m## [5 of 6] sample: sample3; pipeline: example_pipestat_pipeline[0m
    Calling pre-submit function: looper.write_sample_yaml
    Writing script to /home/drc/GITHUB/pepspec/docs/looper/notebooks/hello_looper-dev/advanced/results/submission/example_pipestat_pipeline_sample3.sub
    Job script (n=1; 0.00Gb): /home/drc/GITHUB/pepspec/docs/looper/notebooks/hello_looper-dev/advanced/results/submission/example_pipestat_pipeline_sample3.sub
    Compute node: databio
    Start time: 2024-07-08 19:32:32
    [36m## [6 of 6] sample: sample3; pipeline: example_pipestat_pipeline[0m
    Calling pre-submit function: looper.write_sample_yaml
    Writing script to /home/drc/GITHUB/pepspec/docs/looper/notebooks/hello_looper-dev/advanced/results/submission/example_pipestat_pipeline_sample3.sub
    Job script (n=1; 0.00Gb): /home/drc/GITHUB/pepspec/docs/looper/notebooks/hello_looper-dev/advanced/results/submission/example_pipestat_pipeline_sample3.sub
    Compute node: databio
    Start time: 2024-07-08 19:32:32
    
    Looper finished
    Samples valid for job generation: 3 of 3
    {'Pipestat compatible': True, 'Commands submitted': '6 of 6', 'Jobs submitted': 6}
    [0m

Let's take a look at that config file:


```python
!cat .looper_advanced_pipestat.yaml
```

    pep_config: project/project_config.yaml
    output_dir: "results"
    pipeline_interfaces:
        - pipeline/pipestat_pipeline_interface1_sample.yaml
        - pipeline/pipestat_pipeline_interface2_sample.yaml
    pipestat:
      results_file_path: results.yaml
      flag_file_dir: results/flags

Notice a couple of key points here:

This looper configuration file points to two pipeline interfaces.

It also has a pipestat section that it uses for configuring pipestat.


Let's also look at the project config:


```python
!cat project/project_config.yaml
```

    name: looper_advanced_test
    pep_version: "2.0.0"
    sample_table: annotation_sheet.csv
    
    sample_modifiers:
      append:
        attr: "val"
      derive:
        attributes: [read1, read2]
        sources:
          SRA_1: "{SRR}_1.fastq.gz"
          SRA_2: "{SRR}_2.fastq.gz"


Similar to the intermediate example, this advanced example leverages sample_modifiers to extend the project and derive sample attributes.

Finally, let's take a look at one of the pipeline interfaces


```python
!cat pipeline/pipestat_pipeline_interface1_sample.yaml
```

    pipeline_name: example_pipestat_pipeline
    input_schema: https://schema.databio.org/pep/2.0.0.yaml
    output_schema: pipestat_output_schema.yaml
    var_templates:
      path: "{looper.piface_dir}/pipeline1.py"
    pre_submit:
        python_functions:
          - looper.write_sample_yaml
    sample_interface:
      command_template: >
        python3 {pipeline.var_templates.path} --sample-name {sample.sample_name} --req-attr {sample.attr}
    
    


Some new items here include:
output_schema -> used by pipestat to report results
pre_submit functions -> a function to execute before looper submits samples

We can also see that this is a sample-level pipeline because it contains `sample_interface`.


An example of a project-level pipeline


```python
!cat pipeline/pipeline_interface1_project.yaml
```

    pipeline_name: PIPELINE1
    output_schema: output_schema.yaml
    var_templates:
      path: "{looper.piface_dir}/col_pipeline1.py"
    project_interface:
      command_template: >
        python3 {pipeline.var_templates.path} --project-name {project.name}
    
    



```python

```
