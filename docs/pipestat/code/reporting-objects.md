# Reporting objects

This tutorial will show you how pipestat can report not just primitive types, but structured results as objects.

First create a `pipestat.PipestatManager` object with our example schema:


```python

```


```python
import pipestat
psm = pipestat.PipestatManager(
    record_identifier="sample1",
    results_file_path="pipestat_results.yaml",
    schema_path="https://schema.databio.org/pipestat/object_result.yaml",
)
```

    Initialize PipestatBackend
    Initialize FileBackend


Here, we're pointing to a remote `schema_path`. Let's take a look at the schema object. You can see a preview of it here at the schema server: <https://schema.databio.org/?namespace=pipestat&schema=object_result>. We can also see what it looks like in Python code:


```python
psm.schema
```




    ParsedSchemaDB (refget)
     Project-level properties:
     - None
     Sample-level properties:
     -  value : {'type': 'string', 'description': 'Value of the object referred to by the key'}
     -  mydict : {'type': 'object', 'description': 'Can pipestat handle nested objects?'}
     Status properties:
     - None



This schema defines two sample-level variables: `value` is a string, and `mydict` is an object. Let's see how to report a `mydict`:


```python
psm.report({"mydict": {"toplevel": {"value": "456"}}}, force_overwrite=True)
```




    ["Reported records for 'sample1' in 'refget' :\n - mydict: {'toplevel': {'value': '456'}}",
     "Reported records for 'sample1' in 'refget' :\n - pipestat_created_time: 2024-02-21 20:52:20",
     "Reported records for 'sample1' in 'refget' :\n - pipestat_modified_time: 2024-02-21 20:52:20"]



And now we can retrieve those results:


```python
psm.retrieve_one("sample1", "mydict")
```




    {'toplevel': {'value': '456'}}



Is there a way to retrieve the values within? Something like `psm.retrieve_one("sample1", "mydict.toplevel.value")` ? I can't find any docs about that.
