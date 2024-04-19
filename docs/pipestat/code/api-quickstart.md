# Pipestat API Quickstart Guide

This example is for quickly reporting results to a results.yaml filebackend.


```python
from pipestat import PipestatManager

#File Backend requires a results.yaml file
result_file = "../tests/data/results_docs_example.yaml"

#Every pipestat manager requires an output schema to know the format of results
schema_file = "../tests/data/sample_output_schema.yaml"

# With these two files, we can initialize a PipestatManager object and begin reporting results
```


```python
psm = PipestatManager(results_file_path=result_file, schema_path=schema_file)
```

    Initialize FileBackend



```python
# Let's look at our output schema. Notice that the schema is only for reporting sample-level results
print(psm.schema)
```

    ParsedSchema (default_pipeline_name)
     Project-level properties:
     - None
     Sample-level properties:
     - number_of_things : {'type': 'integer', 'description': 'Number of things'}
     - percentage_of_things : {'type': 'number', 'description': 'Percentage of things'}
     - name_of_something : {'type': 'string', 'description': 'Name of something'}
     - switch_value : {'type': 'boolean', 'description': 'Is the switch on or off'}
     - output_file : {'description': 'This a path to the output file', 'type': 'object', 'object_type': 'file', 'properties': {'path': {'type': 'string'}, 'title': {'type': 'string'}}, 'required': ['path', 'title']}
     - output_image : {'description': 'This a path to the output image', 'type': 'object', 'object_type': 'image', 'properties': {'path': {'type': 'string'}, 'thumbnail_path': {'type': 'string'}, 'title': {'type': 'string'}}, 'required': ['path', 'thumbnail_path', 'title']}
     - md5sum : {'type': 'string', 'description': 'MD5SUM of an object', 'highlight': True}
     Status properties:
     - None



```python
# Let's report a result. The result_identifier (e.g. percentage_of_things) must be in the output schema.
# When reporting a result, a record_identifier must be provided either at the time of reporting 
# or upon PipestatManager creation.

psm.report(record_identifier="my_sample_name_1", values={"percentage_of_things": 100})
```




    ["Reported records for 'my_sample_name_1' in 'default_pipeline_name' :\n - percentage_of_things: 100"]




```python
# Pipestat reports the result as well as a created time and a modified time.
# We can overwrite the modified time by reporting a new result. This is because force_overwrite defualts to True
psm.report(record_identifier="my_sample_name_1", values={"percentage_of_things": 50})
```

    These results exist for 'my_sample_name_1': percentage_of_things
    Overwriting existing results: percentage_of_things





    ["Reported records for 'my_sample_name_1' in 'default_pipeline_name' :\n - percentage_of_things: 50"]




```python
# If you set the flag to false and attempt to report results for a result that already exists...
psm.report(record_identifier="my_sample_name_1", values={"percentage_of_things": 50}, force_overwrite=False)
```

    These results exist for 'my_sample_name_1': percentage_of_things





    False




```python
# Let's look at the reported data
# Note that history recording is turned on by default and lives under meta -> history keys
psm.data
```




    default_pipeline_name:
      project: {}
      sample:
        my_sample_name_1:
          meta:
            pipestat_modified_time: '2024-04-18 14:17:08'
            pipestat_created_time: '2024-04-18 14:17:07'
            history:
              percentage_of_things:
                '2024-04-18 14:17:08': 100
          percentage_of_things: 50





```python
# You can also retrieve a result:
result = psm.retrieve_one(record_identifier="my_sample_name_1")
print(result)
```

    {'percentage_of_things': 50, 'record_identifier': 'my_sample_name_1'}



```python
# Similarly you can retrieve historical results as well
result = psm.retrieve_history(record_identifier="my_sample_name_1")
print(result)
```

    {'percentage_of_things': {'2024-04-18 14:17:08': 100}}



```python

```
