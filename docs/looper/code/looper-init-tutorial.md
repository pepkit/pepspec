# Initializing Looper

Looper contains a built-in guided tutorial for initializing looper configuration files and a generic pipeline interface.


### Initialize looper config


```python
!looper init
```

Example output:

```
Looper initialization 
Would you like to follow a guided tutorial?  Y / n...

Selection: n
───────────────────────────────────────────────────────────────────────────────────────────────────────
{
│   'pep_config': 'example/pep/path',
│   'output_dir': '.',
│   'pipeline_interfaces': [
│   │   'pipeline_interface1.yaml',
│   │   'pipeline_interface2.yaml'
│   ]
}
Initialized looper config file: /home/drc/PythonProjects/testing_perofrmance/testingperformance/.looper.yaml

```


### Initialize Generic Pipeline Interface


```python
!looper init_piface
```

    [92m───────────────────────────── [0m [35mPipeline Interface[0m[92m ──────────────────────────────[0m
    [1m{[0m
    [2;32m│   [0m[32m'pipeline_name'[0m: [32m'default_pipeline_name'[0m,
    [2;32m│   [0m[32m'output_schema'[0m: [32m'output_schema.yaml'[0m,
    [2;32m│   [0m[32m'var_templates'[0m: [1m{[0m
    [2;32m│   │   [0m[32m'pipeline'[0m: [32m'[0m[32m{[0m[32mlooper.piface_dir[0m[32m}[0m[32m/count_lines.sh'[0m
    [2;32m│   [0m[1m}[0m,
    [2;32m│   [0m[32m'sample_interface'[0m: [1m{[0m
    [2;32m│   │   [0m[32m'command_template'[0m: [32m'[0m[32m{[0m[32mpipeline.var_templates.pipeline[0m[32m}[0m[32m [0m[32m{[0m[32msample.file[0m[32m}[0m[32m --output-parent [0m[32m{[0m[32mlooper.sample_output_folder[0m[32m}[0m[32m'[0m
    [2;32m│   [0m[1m}[0m
    [1m}[0m
    Pipeline interface successfully created at: 
    [33m/home/drc/GITHUB/pepspec/docs/looper/notebooks/pipeline/[0m[33mpipeline_interface.yaml[0m
    [92m──────────────────────────────── [0m [35mOutput Schema[0m[92m ────────────────────────────────[0m
    [1m{[0m
    [2;32m│   [0m[32m'pipeline_name'[0m: [32m'default_pipeline_name'[0m,
    [2;32m│   [0m[32m'samples'[0m: [1m{[0m
    [2;32m│   │   [0m[32m'number_of_lines'[0m: [1m{[0m
    [2;32m│   │   │   [0m[32m'type'[0m: [32m'integer'[0m,
    [2;32m│   │   │   [0m[32m'description'[0m: [32m'Number of lines in the input file.'[0m
    [2;32m│   │   [0m[1m}[0m
    [2;32m│   [0m[1m}[0m
    [1m}[0m
    Output schema successfully created at: 
    [33m/home/drc/GITHUB/pepspec/docs/looper/notebooks/pipeline/[0m[33moutput_schema.yaml[0m
    [92m──────────────────────── [0m [35mExample Pipeline Shell Script[0m[92m ────────────────────────[0m
    #![35m/bin/[0m[95mbash[0m
    [33mlinecount[0m=`wc -l $[1;36m1[0m | sed -E [32m's/^[0m[32m[[0m[32m[[0m[32m:space:[0m[32m][0m[32m][0m[32m+//'[0m | cut -f1 -d' '`
    pipestat report -r $[1;36m2[0m -i [32m'number_of_lines'[0m -v $linecount -c $[1;36m3[0m
    echo [32m"Number of lines: $linecount"[0m
        
    count_lines.sh successfully created at: 
    [33m/home/drc/GITHUB/pepspec/docs/looper/notebooks/pipeline/[0m[33mcount_lines.sh[0m
    [0m


```python

```
