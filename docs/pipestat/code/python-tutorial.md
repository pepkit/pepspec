# Pipestat Python API

Pipestat is a [Python package](https://pypi.org/project/pipestat/) for a standardized reporting of pipeline statistics. It formalizes a way to communicate between pipelines and downstream tools that analyze their results so that pipeline results can easily become input for downstream analyses.

This tutorial is targeted toward pipeline developers, and shows how to use pipestat to manage pipeline results. This tutorial assumes you're writing your pipeline in Python; if not, there's another tutorial that accomplishes the same thing for any pipeline using the command-line interface.

## Introduction

To make your Python pipeline pipestat-compatible, you first need to initialize pipestat with some important configuration setup:

1. **pipestat schema**: a path to a JSON-schema file that defines results reported by this pipeline
2. **pipeline_name**: defines a unique group name for reported results
3. **record_identifier**: a unique name for a particular *run* of the pipeline, typically a sample name
4. **backend**: where the results should be stored. Either path to a YAML-formatted file or pipestat config with PostgreSQL database login credentials

## Back-end types

Two types of back-ends are currently supported:

1. a **file** (pass a file path to the constructor)  
The changes reported using the `report` method of `PipestatManger` will be securely written to the file. Currently only [YAML](https://yaml.org/) format is supported. 

2. a **PostgreSQL database** (pass a path to the pipestat config to the constructor)
This option gives the user the possibility to use a fully fledged database to back `PipestatManager`. 


## Initializing a pipestat session

Start by importing the `pipestat` package in Python.



```python
import pipestat
from jsonschema import ValidationError
```

After importing the package, we need to create an `PipestatManager` object. The object constructor requires a few pieces of information. We'll use a file as the back-end, by passing a file path string to the constructor. Let's create a temporary file first:


```python
from tempfile import mkstemp

_, temp_file = mkstemp(suffix=".yaml")
print(temp_file)
```

    /tmp/tmpu4r0mojr.yaml


Now we can create a `PipestatManager` object that uses this file as the back-end:


```python
psm = pipestat.PipestatManager(
    record_identifier="sample1",
    results_file_path=temp_file,
    schema_path="../tests/data/sample_output_schema.yaml",
)
```

    Initialize FileBackend


Note: For schema_path, you will need to point to a **sample_output_schema.yaml**. An example file can be found here: https://github.com/pepkit/pipestat/blob/master/tests/data/sample_output_schema.yaml

You can also put these settings into a config file and just pass that to the `config` argument, instead of specifying each argument separately. The results will be reported to a "test" namespace.


```python
psm.pipeline_name
```




    'default_pipeline_name'



By default, `PipestatManager` instance is bound to the record it was initialized with. However, reporting or removing results for a different record can be enforced in the respective methods with `sameple_name` argument.


```python
psm.record_identifier
```




    'sample1'



Since we've used a newly created file, nothing has been reported yet:


```python
print(psm.retrieve_one(record_identifier='sample1'))
```

Using `psm.retrieve_one` at this stage will return a `RecordNotFound` exception.


```python
psm.data
```




    default_pipeline_name:
      project: {}
      sample: {}




## Reporting results

To report a result, use a `report` method. It requires two pieces of information:

1. record_identifier -- record to report the result for, for example a unique name of the sample (optional if provided at `PipestatManager` initialization stage)
2. values -- a Python `dict` of resultID-value pairs to report. The top level keys must correspond to the results identifiers defined in the schema

### Available results defined in schemas

To learn about the results that the current `PipestatManager` instance supports check out the `schema.result_schemas` property:


```python
psm.result_schemas
```




    {'number_of_things': {'type': 'integer', 'description': 'Number of things'},
     'percentage_of_things': {'type': 'number',
      'description': 'Percentage of things'},
     'name_of_something': {'type': 'string', 'description': 'Name of something'},
     'switch_value': {'type': 'boolean', 'description': 'Is the switch on or off'},
     'output_file': {'description': 'This a path to the output file',
      'type': 'object',
      'object_type': 'file',
      'properties': {'path': {'type': 'string'}, 'title': {'type': 'string'}},
      'required': ['path', 'title']},
     'output_image': {'description': 'This a path to the output image',
      'type': 'object',
      'object_type': 'image',
      'properties': {'path': {'type': 'string'},
       'thumbnail_path': {'type': 'string'},
       'title': {'type': 'string'}},
      'required': ['path', 'thumbnail_path', 'title']},
     'md5sum': {'type': 'string',
      'description': 'MD5SUM of an object',
      'highlight': True}}



To learn about the actual required attributes of the reported results, like `file` or `image` (see: `output_file` and `output_image` results) select the `output_file` from the `result_schemas` property:


```python
psm.result_schemas["output_file"]
```




    {'description': 'This a path to the output file',
     'type': 'object',
     'object_type': 'file',
     'properties': {'path': {'type': 'string'}, 'title': {'type': 'string'}},
     'required': ['path', 'title']}



### Results composition enforcement
As you can see, to report a `output_file` result, you need to provide an object with `path` and `title` string attributes. If you fail to do so `PipestatManager` will issue an informative validation error:


```python
try:
    psm.report(record_identifier="sample1", values={"output_file": {"path": "/home/user/path.csv"}})
except ValidationError as e:
    print(e)
```

`SchemaValidationErrorDuringReport: 'title' is a required property`

Let's report a correct object this time:


```python
psm.report(record_identifier="sample1",
    values={
        "output_file": {
            "path": "/home/user/path.csv",
            "title": "CSV file with some data",
        }
    }
)
```




    ["Reported records for 'sample1' in 'default_pipeline_name' :\n - output_file: {'path': '/home/user/path.csv', 'title': 'CSV file with some data'}"]



Inspect the object's database to verify whether the result has been successfully reported:


```python
psm.data
```




    default_pipeline_name:
      project: {}
      sample:
        sample1:
          meta:
            pipestat_modified_time: '2024-04-18 15:04:33'
            pipestat_created_time: '2024-04-18 15:04:33'
          output_file:
            path: /home/user/path.csv
            title: CSV file with some data




Or use the retrieve function (required for database backends):


```python
psm.retrieve_one('sample1')
```




    {'output_file': {'path': '/home/user/path.csv',
      'title': 'CSV file with some data'},
     'record_identifier': 'sample1'}



Results are overwritten unless force_overwrite is set to False!


```python
psm.report(record_identifier="sample1",
    values={
        "output_file": {
            "path": "/home/user/path_new.csv",
            "title": "new CSV file with some data",
        }
    }
)
```

    These results exist for 'sample1': output_file
    Overwriting existing results: output_file





    ["Reported records for 'sample1' in 'default_pipeline_name' :\n - output_file: {'path': '/home/user/path_new.csv', 'title': 'new CSV file with some data'}"]




```python
psm.report(record_identifier="sample1",
    values={
        "output_file": {
            "path": "/home/user/path_new.csv",
            "title": "new CSV file with some data",
        }
    },
    force_overwrite=False,
)

psm.retrieve_one('sample1')
```

    These results exist for 'sample1': output_file





    {'output_file': {'path': '/home/user/path_new.csv',
      'title': 'new CSV file with some data'},
     'record_identifier': 'sample1'}



Most importantly, by backing the object by a file, the reported results persist -- another `PipestatManager` object reads the results when created:


```python
psm1 = pipestat.PipestatManager(
    pipeline_name="test",
    record_identifier="sample1",
    results_file_path=temp_file,
    schema_path="../tests/data/sample_output_schema.yaml",
)
```

    Initialize FileBackend



```python
psm.retrieve_one('sample1')
```




    {'output_file': {'path': '/home/user/path_new.csv',
      'title': 'new CSV file with some data'},
     'record_identifier': 'sample1'}



That's because the contents are stored in the file we've specified at object creation stage:


```python
!echo $temp_file
!cat $temp_file
```

    /tmp/tmps01teih1.yaml
    default_pipeline_name:
      project: {}
      sample:
        sample1:
          output_file:
            path: /home/user/path_new.csv
            title: new CSV file with some data
          pipestat_created_time: '2023-11-07 17:30:39'
          pipestat_modified_time: '2023-11-07 17:30:48'


Note that two processes can securely report to a single file and single namespace since `pipestat` supports locks and race-free writes to control multi-user conflicts and prevent data loss.

### Results type enforcement

By default `PipestatManager` raises an exception if a non-compatible result value is reported. 

This behavior can be changed by setting `strict_type` to `True` in `PipestatManager.report` method. In this case `PipestatManager` tries to cast the reported results values to the Python classes required by schema. For example, if a result defined as `integer` is reported and a `str` value is passed, the eventual value will be `int`:


```python
psm.result_schemas["number_of_things"]
```




    {'type': 'integer', 'description': 'Number of things'}




```python
psm.report(record_identifier="sample1",values={"number_of_things": "10"}, strict_type=False)
```




    ["Reported records for 'sample1' in 'default_pipeline_name' :\n - number_of_things: 10"]



The method will attempt to cast the value to a proper Python class and store the converted object. In case of a failure, an error will be raised:


```python
try:
    psm.report(
        record_identifier="sample2", values={"number_of_things": []}, strict_type=False
    )
except TypeError as e:
    print(e)
```

    int() argument must be a string, a bytes-like object or a real number, not 'list'


Note that in this case we tried to report a result for a different record (`sample2`), which had to be enforced with `record_identifier` argument.


```python
psm.data
```




    default_pipeline_name:
      project: {}
      sample:
        sample1:
          meta:
            pipestat_modified_time: '2024-04-18 15:06:45'
            pipestat_created_time: '2024-04-18 15:04:33'
            history:
              output_file:
                '2024-04-18 15:06:04':
                  path: /home/user/path.csv
                  title: CSV file with some data
          output_file:
            path: /home/user/path_new.csv
            title: new CSV file with some data
          number_of_things: '10'




## Retrieving results

Naturally, the reported results can be retrieved. Let's explore all the options the `PipestatManager.retrieve` method provides:

To retrieve a *specific* result for a record, provide the identifiers:


```python
psm.retrieve_one(record_identifier="sample1", result_identifier="number_of_things")
```




    '10'



To retrieve *all* the results for a record, skip the `result_identifier` argument:


```python
psm.retrieve_one(record_identifier="sample1")
```




    {'output_file': {'path': '/home/user/path_new.csv',
      'title': 'new CSV file with some data'},
     'number_of_things': '10',
     'record_identifier': 'sample1'}



## Retrieving History

Pipestat records a history of reported results by default.
If results have been overwritten, the historical results can be obtained via:


```python
psm.retrieve_history(record_identifier="sample1")
```




    {'output_file': {'2024-04-18 15:06:04': {'path': '/home/user/path.csv',
       'title': 'CSV file with some data'}}}



## Removing results

`PipestatManager` object also supports results removal. Call `remove` method and provide `record_identifier` and  `result_identifier` arguments to do so:


```python
psm.remove(record_identifier="sample1",result_identifier="number_of_things")
```

    Removed result 'number_of_things' for record 'sample1' from 'default_pipeline_name' namespace





    True



The entire record, skip the `result_identifier` argument:


```python
psm.remove()
```

    Removing 'sample1' record





    True



Verify that an appropriate entry from the results was deleted:


```python
psm.backend._data
```




    default_pipeline_name:
      project: {}
      sample: {}




## Highlighting results

In order to highlight results we need to add an extra property in the pipestat results schema (`highlight: true`) under the result identifier that we wish to highlight. 


```python
from tempfile import mkstemp

_, temp_file_highlight = mkstemp(suffix=".yaml")
print(temp_file_highlight)

psm_highlight = pipestat.PipestatManager(
    pipeline_name="test_highlight",
    record_identifier="sample1",
    results_file_path=temp_file_highlight,
    schema_path="../tests/data/sample_output_schema_highlight.yaml",
)
```

    Initialize PipestatBackend
    Initialize FileBackend


    /tmp/tmpa9fo3rk7.yaml


For example, result `log` is highlighted in this case:


```python
psm_highlight.result_schemas['log']
```




    {'highlight': True,
     'description': 'The log file of the pipeline run',
     'type': 'object',
     'object_type': 'file',
     'properties': {'path': {'type': 'string'}, 'title': {'type': 'string'}},
     'required': ['path', 'title']}



The highlighting feature can be used by pipestat clients to present the highlighted results in a special way.


```python
psm_highlight.highlighted_results
```




    ['log', 'profile', 'commands', 'version']



## Pipeline status management

Pipestat provides a pipeline status management system, which can be used to set and read pipeline status. To maintain the status information between sessions it uses flags or additional DB table if the `PipestatManager` object is backed with YAML file or PostgreSQL database, respectively.

To set pipeline status use `set_status` method:


```python
psm.set_status(record_identifier="sample1", status_identifier="running")
```

To get pipeline status use `get_status` method:


```python
psm.get_status(record_identifier="sample1")
```




    'running'



Allowable statuses and related metadata are defined in the status schema, which can be accessed via:


```python
psm.cfg['_status_schema']
```




    {'running': {'description': 'the pipeline is running',
      'color': [30, 144, 255]},
     'completed': {'description': 'the pipeline has completed',
      'color': [50, 205, 50]},
     'failed': {'description': 'the pipeline has failed', 'color': [220, 20, 60]},
     'waiting': {'description': 'the pipeline is waiting',
      'color': [240, 230, 140]},
     'partial': {'description': 'the pipeline stopped before completion point',
      'color': [169, 169, 169]}}



`pipestat` Python package ships with a default status schema, so we did not have to provide the schema when constructing the `PipestatManager` object. Similarly, the flags containing directory is an optional configuration option. 

Please refer to the Python API documentation (`__init__` method) to see how to use custom status schema and flags directory.

## Initializing `PipestatManager` without results schema

Starting with `pipestat 0.0.3`, it is possible to initialize the `PipestatManager` object without specifying the results schema file. This feature comes in handy if `PipestatManager` is created with a sole intent to monitor pipeline status.

Here's an example:


```python
_, temp_file_no_schema = mkstemp(suffix=".yaml")
print(temp_file_no_schema)

psm_no_schema = pipestat.PipestatManager(
    pipeline_name="test_no_schema", results_file_path=temp_file_no_schema
)
```

    No schema supplied.
    Initialize PipestatBackend
    Initialize FileBackend


    /tmp/tmpxpe5w75w.yaml


As mentioned above, the pipeline status management capabilities are supported with no results schema defined:


```python
psm_no_schema.set_status(status_identifier="running", record_identifier="sample1")
psm_no_schema.get_status(record_identifier="sample1")
```




    'running'



## Generate static HTML Report using the `summarize` command

You can generate a static browsable html report using the `summarize` function:


```python
psm.summarize()
```

    Building index page for pipeline: default_pipeline_name
     * Creating sample pages
     * Creating object pages





    '/tmp/reports/default_pipeline_name/index.html'



## Sample and Project Level Pipelines

All of the examples above assume the user has a sample level pipeline. Pipestat defaults to setting pipeline_type = 'sample'. However, the user can set the pipeline_type = 'project'.

Beginning in Pipestat 0.6.0, the user can call SamplePipestatManager() or ProjectPipestatManager() that do everything PipestatManager does but sets the pipeline_type to either 'sample' or 'project' respectively.


```python
psm_sample = pipestat. SamplePipestatManager(record_identifier="sample1",
    results_file_path=temp_file,
    schema_path="../tests/data/sample_output_schema.yaml",)
```

    Initialize PipestatBackend
    Initialize FileBackend
    Initialize PipestatMgrSample



```python
psm_sample.result_schemas["output_file"]
```




    {'description': 'This a path to the output file',
     'type': 'object',
     'object_type': 'file',
     'properties': {'path': {'type': 'string'}, 'title': {'type': 'string'}},
     'required': ['path', 'title']}



## PipestatBoss

Also in Pipestat 0.6.0, the user can call PipestatBoss with the sample arguments as SamplePipestatManager or ProjectPipestatmanger while also including a list of pipeline_types. This will create and object containing multiple PipestatManager objects.


```python
psb = pipestat.PipestatBoss(pipeline_list=['sample', 'project',], 
                   schema_path="../tests/data/sample_output_schema.yaml", results_file_path=temp_file)
```

    Initialize PipestatBoss
    Initialize PipestatBackend
    Initialize FileBackend
    Initialize PipestatMgrSample
    Initialize PipestatBackend
    Initialize FileBackend
    Initialize PipestatMgrProject



```python
psb.samplemanager.report(record_identifier="sample1",values={
        "output_file": {
            "path": "/home/user/path.csv",
            "title": "CSV file with some data",
        }
    })
```




    ["Reported records for 'sample1' in 'default_pipeline_name' :\n - output_file: {'path': '/home/user/path.csv', 'title': 'CSV file with some data'}",
     "Reported records for 'sample1' in 'default_pipeline_name' :\n - pipestat_created_time: 2023-11-07 17:31:18",
     "Reported records for 'sample1' in 'default_pipeline_name' :\n - pipestat_modified_time: 2023-11-07 17:31:18"]




```python

```
