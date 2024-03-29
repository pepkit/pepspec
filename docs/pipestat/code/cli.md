# Pipestat CLI

This tutorial demonstrates how to use the pipeline command-line interface (CLI). You should have already installed pipestat. **Before following this tutorial please make sure you're familiar with more information-rich "Pipestat Python API" tutorial.** 
Also, for the following tutorial, you will need to point to a **sample_output_schema.yaml** in the schema path. An example file can be found here:

https://github.com/pepkit/pipestat/blob/master/tests/data/sample_output_schema.yaml

Report results from the command line by calling `pipestat` and passing in all relevant information:


```python
rm ../tests/data/test_results_1.yaml
touch ../tests/data/test_results_1.yaml
pipestat report \
    --record-identifier sample_name \
    --result-identifier percentage_of_things \
    --value 12 \
    --results-file ../tests/data/test_results_1.yaml \
    --schema ../tests/data/sample_output_schema.yaml
```

    Reported records for 'sample_name' in 'pipeline_name' namespace:
     - percentage_of_things: 12


But this is obviously pretty cumbersome, since you have to pass lots of constant information to every call to report a result. So instead, you have an option to set up environment variables for a particular pipeline run:

## Prepare environment

Pipestat environment variables avoid copious repetition of arguments in subsequent `pipestat` calls. Refer to the [Environment variables reference](http://pipestat.databio.org/en/latest/env_vars/) for the complete list of supported environment variables. We will set a few for this tutorial:


```python
export PIPESTAT_RESULTS_SCHEMA=../tests/data/sample_output_schema.yaml
export PIPESTAT_RECORD_IDENTIFIER=sample1
export PIPESTAT_RESULTS_FILE=`mktemp` # temporary file for results storage
```

Before we dive in, let's take a quick glance at the schema. This is the file that describes what sort of results are reported by this pipeline:


```python
cat $PIPESTAT_RESULTS_SCHEMA
```

    number_of_things:
      type: integer
      description: "Number of things"
    percentage_of_things:
      type: number
      description: "Percentage of things"
    name_of_something:
      type: string
      description: "Name of something"
    switch_value:
      type: boolean
      description: "Is the switch on of off"
    collection_of_things:
      type: array
      description: "This store collection of values"
    output_object:
      type: object
      description: "Object output"
    output_file:
      type: file
      description: "This a path to the output file"
    output_image:
      type: image
      description: "This a path to the output image"
    md5sum:
      type: string
      description: "MD5SUM of an object"
      highlight: true


### Reporting

Naturally, the command line interface provides access to all the Python API functionalities of `pipestat`. So, for example, to report a result and back the object by a file use:


```python
pipestat report -i number_of_things -v 100
```

    Reported records for 'sample1' in 'test' namespace:
     - number_of_things: 100


The result has been reported and the database file has been updated:


```python
cat $PIPESTAT_RESULTS_FILE
```

    test:
      sample1:
        number_of_things: 100


Let's report another result:


```python
pipestat report -i percentage_of_things -v 1.1
```

    Reported records for 'sample1' in 'test' namespace:
     - percentage_of_things: 1.1



```python
cat $PIPESTAT_RESULTS_FILE
```

    test:
      sample1:
        number_of_things: 100
        percentage_of_things: 1.1


### Inspection

`pipestat inspect` command is a way to briefly look at the general `PipestatManager` state, like number of records, type of backend etc.


```python
pipestat inspect
```

    
    
    PipestatManager (test)
    Backend: File 
     - results: /var/folders/h8/8npwnh2s4rb8lr6hsy2ydrsh0000gp/T/tmp.hk8q23wT
     - status: /var/folders/h8/8npwnh2s4rb8lr6hsy2ydrsh0000gp/T)
    Results schema source: ../tests/data/sample_output_schema.yaml
    Status schema source: /usr/local/lib/python3.9/site-packages/pipestat/schemas/status_schema.yaml
    Records count: 1
    Highlighted results: md5sum


In order to display the contents of the results file or database table associated with the indicated namespace, add `--data` flag:


```python
pipestat inspect --data
```

    
    
    PipestatManager (test)
    Backend: File 
     - results: /var/folders/h8/8npwnh2s4rb8lr6hsy2ydrsh0000gp/T/tmp.hk8q23wT
     - status: /var/folders/h8/8npwnh2s4rb8lr6hsy2ydrsh0000gp/T)
    Results schema source: ../tests/data/sample_output_schema.yaml
    Status schema source: /usr/local/lib/python3.9/site-packages/pipestat/schemas/status_schema.yaml
    Records count: 1
    Highlighted results: md5sum
    
    Data:
    test:
      sample1:
        number_of_things: 100
        percentage_of_things: 1.1


### Retrieval

Naturally, the reported results can be retrieved. Just call `pipestat retrieve` to do so:


```python
pipestat retrieve -i percentage_of_things
```

    1.1


### Removal

In order to remove a result call `pipestat remove`:


```python
pipestat remove -i percentage_of_things
```

    Removed result 'percentage_of_things' for record 'sample1' from 'test' namespace


The results file and the state of the `PipestatManager` object reflect the removal:


```python
cat $PIPESTAT_RESULTS_FILE
```

    test:
      sample1:
        number_of_things: 100



```python
pipestat inspect --data
```

    
    
    PipestatManager (test)
    Backend: File 
     - results: /var/folders/h8/8npwnh2s4rb8lr6hsy2ydrsh0000gp/T/tmp.hk8q23wT
     - status: /var/folders/h8/8npwnh2s4rb8lr6hsy2ydrsh0000gp/T)
    Results schema source: ../tests/data/sample_output_schema.yaml
    Status schema source: /usr/local/lib/python3.9/site-packages/pipestat/schemas/status_schema.yaml
    Records count: 1
    Highlighted results: md5sum
    
    Data:
    test:
      sample1:
        number_of_things: 100


## Status management

To manage pipeline status call `pipestat status <subcommand>`:

- `set` to set pipeline statuses
- `get` to retrieve pipeline statuses

Starting with `pipestat 0.0.3` the `--schema` argument is not required for status management.


```python
pipestat status set running
```


```python
pipestat status get
```

    running


Note that only statuses defined in the status schema are supported:


```python
cat /usr/local/lib/python3.9/site-packages/pipestat/schemas/status_schema.yaml
```

    running:
      description: "the pipeline is running"
      color: [30, 144, 255] # dodgerblue
    completed:
      description: "the pipeline has completed"
      color: [50, 205, 50] # limegreen
    failed:
      description: "the pipeline has failed"
      color: [220, 20, 60] # crimson
    waiting:
      description: "the pipeline is waiting"
      color: [240, 230, 140] # khaki
    partial:
      description: "the pipeline stopped before completion point"
      color: [169, 169, 169] # darkgray


## HTML Report Generation

To generate a static html report, call `pipestat summarize --results-file PIPESTAT_RESULTS_FILE --schema PIPESTAT_RESULTS_SCHEMA`


```python
rm $PIPESTAT_RESULTS_FILE
```
