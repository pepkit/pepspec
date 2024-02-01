Final targets: EidoValidationError, convert_project, get_available_pep_filters, get_input_files_size, inspect_project, read_schema, validate_config, validate_input_files, validate_project, validate_sample
<script>
document.addEventListener('DOMContentLoaded', (event) => {
  document.querySelectorAll('h3 code').forEach((block) => {
    hljs.highlightBlock(block);
  });
});
</script>

<style>
h3 .content { 
    padding-left: 22px;
    text-indent: -15px;
 }
h3 .hljs .content {
    padding-left: 20px;
    margin-left: 0px;
    text-indent: -15px;
    martin-bottom: 0px;
}
h4 .content, table .content, p .content, li .content { margin-left: 30px; }
h4 .content { 
    font-style: italic;
    font-size: 1em;
    margin-bottom: 0px;
}

</style>


# Package `eido` Documentation


Project configuration

## <a name="EidoValidationError"></a> Class `EidoValidationError`
Object was not validated successfully according to schema.


```python
def __init__(self, message, errors_by_type)
```

Initialize self.  See help(type(self)) for accurate signature.



```python
def validate_project(project, schema)
```

Validate a project object against a schema
#### Parameters:

- `project` (`peppy.Project`):  a project object to validate
- `schema` (`str | dict`):  schema dict to validate against or a path to onefrom the error. Useful when used ith large projects




```python
def validate_sample(project, sample_name, schema)
```

Validate the selected sample object against a schema
#### Parameters:

- `project` (`peppy.Project`):  a project object to validate
- `sample_name` (`str | int`):  name or index of the sample to validate
- `schema` (`str | dict`):  schema dict to validate against or a path to one




```python
def validate_config(project, schema)
```

Validate the config part of the Project object against a schema
#### Parameters:

- `project` (`peppy.Project`):  a project object to validate
- `schema` (`str | dict`):  schema dict to validate against or a path to one




```python
def read_schema(schema)
```

Safely read schema from YAML-formatted file.

If the schema imports any other schemas, they will be read recursively.
#### Parameters:

- `schema` (`str | Mapping`):  path to the schema fileor schema in a dict form


#### Returns:

- `list[dict]`:  read schemas


#### Raises:

- `TypeError`:  if the schema arg is neither a Mapping nor a file path orif the 'imports' sections in any of the schemas is not a list




```python
def inspect_project(p, sample_names=None, max_attr=10)
```

Print inspection info: Project or, if sample_names argument is provided, matched samples
#### Parameters:

- `p` (`peppy.Project`):  project to inspect
- `sample_names` (`Iterable[str]`):  list of samples to inspect
- `max_attr` (`int`):  max number of sample attributes to display




```python
def get_available_pep_filters()
```

Get a list of available target formats
#### Returns:

- `List[str]`:  a list of available formats




```python
def convert_project(prj, target_format, plugin_kwargs=None)
```

Convert a `peppy.Project` object to a selected format
#### Parameters:

- `prj` (`peppy.Project`):  a Project object to convert
- `plugin_kwargs` (`dict`):  kwargs to pass to the plugin function
- `target_format` (`str`):  the format to convert the Project object to


#### Raises:

- `EidoFilterError`:  if the requested filter is not defined




```python
def validate_input_files(project, schemas, sample_name=None)
```

Determine which of the required and optional files are missing.

The names of the attributes that are required and/or deemed as inputs
are sourced from the schema, more specifically from `required_files`
and `files` sections in samples section:
- If any of the required files are missing, this function raises an error.
- If any of the optional files are missing, the function raises a warning.
Note, this function also performs Sample object validation with jsonschema.
#### Parameters:

- `project` (`peppy.Project`):  project that defines the samples to validate
- `schema` (`str | dict`):  schema dict to validate against or a path to one
- `sample_name` (`str | int`):  name or index of the sample to validate. If None,validate all samples in the project


#### Raises:

- `PathAttrNotFoundError`:  if any required sample attribute is missing




```python
def get_input_files_size(sample, schema)
```

Determine which of this Sample's required attributes/files are missing and calculate sizes of the files (inputs).

The names of the attributes that are required and/or deemed as inputs
are sourced from the schema, more specifically from required_input_attrs
and input_attrs sections in samples section. Note, this function does
perform actual Sample object validation with jsonschema.
#### Parameters:

- `sample` (`peppy.Sample`):  sample to investigate
- `schema` (`list[dict] | str`):  schema dict to validate against or a path to one


#### Returns:

- `dict`:  dictionary with validation data, i.e missing,required_inputs, all_inputs, input_file_size


#### Raises:

- `ValidationError`:  if any required sample attribute is missing







*Version Information: `eido` v0.2.2-dev, generated by `lucidoc` v0.4.4*
