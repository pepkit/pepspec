Final targets: PipestatBoss, PipestatError, PipestatManager, ProjectPipestatManager, SamplePipestatManager, __version__
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


# Package `pipestat` Documentation

## <a name="PipestatError"></a> Class `PipestatError`
Base exception type for this package


## <a name="SamplePipestatManager"></a> Class `SamplePipestatManager`
Pipestat standardizes reporting of pipeline results and pipeline status management. It formalizes a way for pipeline developers and downstream tools developers to communicate -- results produced by a pipeline can easily and reliably become an input for downstream analyses. A PipestatManager object exposes an API for interacting with the results and pipeline status and can be backed by either a YAML-formatted file or a database.


```python
def __init__(self, **kwargs)
```

Initialize the PipestatManager object
#### Parameters:

- `record_identifier` (`str`):  record identifier to report for. Thiscreates a weak bound to the record, which can be overridden in this object method calls
- `schema_path` (`str`):  path to the output schema that formalizesthe results structure
- `results_file_path` (`str`):  YAML file to report into, if file isused as the object back-end
- `database_only` (`bool`):  whether the reported data should not bestored in the memory, but only in the database
- `config_file` (`str`):  path to the configuration file
- `config_dict` (`dict`):   a mapping with the config file content
- `flag_file_dir` (`str`):  path to directory containing flag files
- `show_db_logs` (`bool`):  Defaults to False, toggles showing database logs
- `pipeline_type` (`str`):  "sample" or "project"
- `pipeline_name` (`str`):  name of the current pipeline, defaults to
- `result_formatter` (`str`):  function for formatting result
- `multi_pipelines` (`bool`):  allows for running multiple pipelines for one file backend
- `output_dir` (`str`):  target directory for report generation via summarize and table generation via table.




```python
def clear_status(self, *args, **kwargs)
```



```python
def config_path(self)
```

Config path. None if the config was not provided or if provided as a mapping of the config contents
#### Returns:

- `str`:  path to the provided config




```python
def count_records(self, *args, **kwargs)
```



```python
def data(self)
```

Data object
#### Returns:

- `yacman.YAMLConfigManager`:  the object that stores the reported data




```python
def db_url(self)
```

Database URL, generated based on config credentials
#### Returns:

- `str`:  database URL


#### Raises:

- `PipestatDatabaseError`:  if the object is not backed by a database




```python
def file(self)
```

File path that the object is reporting the results into
#### Returns:

- `str`:  file path that the object is reporting the results into




```python
def get_status(self, *args, **kwargs)
```



```python
def highlighted_results(self)
```

Highlighted results
#### Returns:

- `List[str]`:  a collection of highlighted results




```python
def initialize_dbbackend(*args, **kwargs)
```



```python
def link(self, *args, **kwargs)
```



```python
def list_recent_results(self, *args, **kwargs)
```



```python
def output_dir(self)
```

Output directory for report and stats generation
#### Returns:

- `str`:  path to output_dir




```python
def pipeline_name(self)
```

Pipeline name
#### Returns:

- `str`:  Pipeline name




```python
def pipeline_type(self)
```

Pipeline type: "sample" or "project"
#### Returns:

- `str`:  pipeline type




```python
def project_name(self)
```

Project name the object writes the results to
#### Returns:

- `str`:  project name the object writes the results to




```python
def record_count(self)
```

Number of records reported
#### Returns:

- `int`:  number of records reported




```python
def record_identifier(self)
```

Pipeline type: "sample" or "project"
#### Returns:

- `str`:  pipeline type




```python
def remove(self, *args, **kwargs)
```



```python
def report(self, *args, **kwargs)
```



```python
def result_schemas(self)
```

Result schema mappings
#### Returns:

- `dict`:  schemas that formalize the structure of each resultin a canonical jsonschema way




```python
def retrieve_one(self, *args, **kwargs)
```



```python
def schema(self)
```

Schema mapping
#### Returns:

- `ParsedSchema`:  schema object that formalizes the results structure




```python
def schema_path(self)
```

Schema path
#### Returns:

- `str`:  path to the provided schema




```python
def select_distinct(self, *args, **kwargs)
```



```python
def select_records(self, *args, **kwargs)
```



```python
def set_status(self, *args, **kwargs)
```



```python
def status_schema(self)
```

Status schema mapping
#### Returns:

- `dict`:  schema that formalizes the pipeline status structure




```python
def status_schema_source(self)
```

Status schema source
#### Returns:

- `dict`:  source of the schema that formalizesthe pipeline status structure




```python
def summarize(self, *args, **kwargs)
```



```python
def table(self, *args, **kwargs)
```



## <a name="ProjectPipestatManager"></a> Class `ProjectPipestatManager`
Pipestat standardizes reporting of pipeline results and pipeline status management. It formalizes a way for pipeline developers and downstream tools developers to communicate -- results produced by a pipeline can easily and reliably become an input for downstream analyses. A PipestatManager object exposes an API for interacting with the results and pipeline status and can be backed by either a YAML-formatted file or a database.


```python
def __init__(self, **kwargs)
```

Initialize the PipestatManager object
#### Parameters:

- `record_identifier` (`str`):  record identifier to report for. Thiscreates a weak bound to the record, which can be overridden in this object method calls
- `schema_path` (`str`):  path to the output schema that formalizesthe results structure
- `results_file_path` (`str`):  YAML file to report into, if file isused as the object back-end
- `database_only` (`bool`):  whether the reported data should not bestored in the memory, but only in the database
- `config_file` (`str`):  path to the configuration file
- `config_dict` (`dict`):   a mapping with the config file content
- `flag_file_dir` (`str`):  path to directory containing flag files
- `show_db_logs` (`bool`):  Defaults to False, toggles showing database logs
- `pipeline_type` (`str`):  "sample" or "project"
- `pipeline_name` (`str`):  name of the current pipeline, defaults to
- `result_formatter` (`str`):  function for formatting result
- `multi_pipelines` (`bool`):  allows for running multiple pipelines for one file backend
- `output_dir` (`str`):  target directory for report generation via summarize and table generation via table.




```python
def clear_status(self, *args, **kwargs)
```



```python
def config_path(self)
```

Config path. None if the config was not provided or if provided as a mapping of the config contents
#### Returns:

- `str`:  path to the provided config




```python
def count_records(self, *args, **kwargs)
```



```python
def data(self)
```

Data object
#### Returns:

- `yacman.YAMLConfigManager`:  the object that stores the reported data




```python
def db_url(self)
```

Database URL, generated based on config credentials
#### Returns:

- `str`:  database URL


#### Raises:

- `PipestatDatabaseError`:  if the object is not backed by a database




```python
def file(self)
```

File path that the object is reporting the results into
#### Returns:

- `str`:  file path that the object is reporting the results into




```python
def get_status(self, *args, **kwargs)
```



```python
def highlighted_results(self)
```

Highlighted results
#### Returns:

- `List[str]`:  a collection of highlighted results




```python
def initialize_dbbackend(*args, **kwargs)
```



```python
def link(self, *args, **kwargs)
```



```python
def list_recent_results(self, *args, **kwargs)
```



```python
def output_dir(self)
```

Output directory for report and stats generation
#### Returns:

- `str`:  path to output_dir




```python
def pipeline_name(self)
```

Pipeline name
#### Returns:

- `str`:  Pipeline name




```python
def pipeline_type(self)
```

Pipeline type: "sample" or "project"
#### Returns:

- `str`:  pipeline type




```python
def project_name(self)
```

Project name the object writes the results to
#### Returns:

- `str`:  project name the object writes the results to




```python
def record_count(self)
```

Number of records reported
#### Returns:

- `int`:  number of records reported




```python
def record_identifier(self)
```

Pipeline type: "sample" or "project"
#### Returns:

- `str`:  pipeline type




```python
def remove(self, *args, **kwargs)
```



```python
def report(self, *args, **kwargs)
```



```python
def result_schemas(self)
```

Result schema mappings
#### Returns:

- `dict`:  schemas that formalize the structure of each resultin a canonical jsonschema way




```python
def retrieve_one(self, *args, **kwargs)
```



```python
def schema(self)
```

Schema mapping
#### Returns:

- `ParsedSchema`:  schema object that formalizes the results structure




```python
def schema_path(self)
```

Schema path
#### Returns:

- `str`:  path to the provided schema




```python
def select_distinct(self, *args, **kwargs)
```



```python
def select_records(self, *args, **kwargs)
```



```python
def set_status(self, *args, **kwargs)
```



```python
def status_schema(self)
```

Status schema mapping
#### Returns:

- `dict`:  schema that formalizes the pipeline status structure




```python
def status_schema_source(self)
```

Status schema source
#### Returns:

- `dict`:  source of the schema that formalizesthe pipeline status structure




```python
def summarize(self, *args, **kwargs)
```



```python
def table(self, *args, **kwargs)
```



## <a name="PipestatBoss"></a> Class `PipestatBoss`
PipestatBoss simply holds Sample or Project Managers that are child classes of PipestatManager. :param list[str] pipeline_list: list that holds pipeline types, e.g. ['sample','project'] :param str record_identifier: record identifier to report for. This creates a weak bound to the record, which can be overridden in this object method calls :param str schema_path: path to the output schema that formalizes the results structure :param str results_file_path: YAML file to report into, if file is used as the object back-end :param bool database_only: whether the reported data should not be stored in the memory, but only in the database :param str | dict config: path to the configuration file or a mapping with the config file content :param str flag_file_dir: path to directory containing flag files :param bool show_db_logs: Defaults to False, toggles showing database logs :param str pipeline_type: "sample" or "project" :param str result_formatter: function for formatting result :param bool multi_pipelines: allows for running multiple pipelines for one file backend :param str output_dir: target directory for report generation via summarize and table generation via table.


```python
def __init__(self, pipeline_list: Optional[list]=None, **kwargs)
```

Initialize self.  See help(type(self)) for accurate signature.



## <a name="PipestatManager"></a> Class `PipestatManager`
Pipestat standardizes reporting of pipeline results and pipeline status management. It formalizes a way for pipeline developers and downstream tools developers to communicate -- results produced by a pipeline can easily and reliably become an input for downstream analyses. A PipestatManager object exposes an API for interacting with the results and pipeline status and can be backed by either a YAML-formatted file or a database.


```python
def __init__(self, project_name: Optional[str]=None, record_identifier: Optional[str]=None, schema_path: Optional[str]=None, results_file_path: Optional[str]=None, database_only: Optional[bool]=True, config_file: Optional[str]=None, config_dict: Optional[dict]=None, flag_file_dir: Optional[str]=None, show_db_logs: bool=False, pipeline_type: Optional[str]=None, pipeline_name: Optional[str]='default_pipeline_name', result_formatter: staticmethod=<function default_formatter at 0x7f47f614fbe0>, multi_pipelines: bool=False, output_dir: Optional[str]=None)
```

Initialize the PipestatManager object
#### Parameters:

- `record_identifier` (`str`):  record identifier to report for. Thiscreates a weak bound to the record, which can be overridden in this object method calls
- `schema_path` (`str`):  path to the output schema that formalizesthe results structure
- `results_file_path` (`str`):  YAML file to report into, if file isused as the object back-end
- `database_only` (`bool`):  whether the reported data should not bestored in the memory, but only in the database
- `config_file` (`str`):  path to the configuration file
- `config_dict` (`dict`):   a mapping with the config file content
- `flag_file_dir` (`str`):  path to directory containing flag files
- `show_db_logs` (`bool`):  Defaults to False, toggles showing database logs
- `pipeline_type` (`str`):  "sample" or "project"
- `pipeline_name` (`str`):  name of the current pipeline, defaults to
- `result_formatter` (`str`):  function for formatting result
- `multi_pipelines` (`bool`):  allows for running multiple pipelines for one file backend
- `output_dir` (`str`):  target directory for report generation via summarize and table generation via table.




```python
def check_multi_results(self)
```



```python
def clear_status(self, *args, **kwargs)
```



```python
def config_path(self)
```

Config path. None if the config was not provided or if provided as a mapping of the config contents
#### Returns:

- `str`:  path to the provided config




```python
def count_records(self, *args, **kwargs)
```



```python
def data(self)
```

Data object
#### Returns:

- `yacman.YAMLConfigManager`:  the object that stores the reported data




```python
def db_url(self)
```

Database URL, generated based on config credentials
#### Returns:

- `str`:  database URL


#### Raises:

- `PipestatDatabaseError`:  if the object is not backed by a database




```python
def file(self)
```

File path that the object is reporting the results into
#### Returns:

- `str`:  file path that the object is reporting the results into




```python
def get_status(self, *args, **kwargs)
```



```python
def highlighted_results(self)
```

Highlighted results
#### Returns:

- `List[str]`:  a collection of highlighted results




```python
def initialize_dbbackend(*args, **kwargs)
```



```python
def initialize_filebackend(self, record_identifier, results_file_path, flag_file_dir)
```



```python
def link(self, *args, **kwargs)
```



```python
def list_recent_results(self, *args, **kwargs)
```



```python
def output_dir(self)
```

Output directory for report and stats generation
#### Returns:

- `str`:  path to output_dir




```python
def pipeline_name(self)
```

Pipeline name
#### Returns:

- `str`:  Pipeline name




```python
def pipeline_type(self)
```

Pipeline type: "sample" or "project"
#### Returns:

- `str`:  pipeline type




```python
def process_schema(self, schema_path)
```



```python
def project_name(self)
```

Project name the object writes the results to
#### Returns:

- `str`:  project name the object writes the results to




```python
def record_count(self)
```

Number of records reported
#### Returns:

- `int`:  number of records reported




```python
def record_identifier(self)
```

Pipeline type: "sample" or "project"
#### Returns:

- `str`:  pipeline type




```python
def remove(self, *args, **kwargs)
```



```python
def report(self, *args, **kwargs)
```



```python
def resolve_results_file_path(self, results_file_path)
```

Replace {record_identifier} in results_file_path if it exists.
#### Parameters:

- `results_file_path` (`str`):  YAML file to report into, if file isused as the object back-end




```python
def result_schemas(self)
```

Result schema mappings
#### Returns:

- `dict`:  schemas that formalize the structure of each resultin a canonical jsonschema way




```python
def retrieve_many(self, record_identifiers: List[str], result_identifier: Optional[str]=None) -> Union[Any, Dict[str, Any]]
```


#### Parameters:

- `record_identifiers` (``):  list of record identifiers
- `result_identifier` (`str`):  single record_identifier


#### Returns:

- ``:  a mapping with filteredresults reported for the record




```python
def retrieve_one(self, *args, **kwargs)
```



```python
def schema(self)
```

Schema mapping
#### Returns:

- `ParsedSchema`:  schema object that formalizes the results structure




```python
def schema_path(self)
```

Schema path
#### Returns:

- `str`:  path to the provided schema




```python
def select_distinct(self, *args, **kwargs)
```



```python
def select_records(self, *args, **kwargs)
```



```python
def set_status(self, *args, **kwargs)
```



```python
def status_schema(self)
```

Status schema mapping
#### Returns:

- `dict`:  schema that formalizes the pipeline status structure




```python
def status_schema_source(self)
```

Status schema source
#### Returns:

- `dict`:  source of the schema that formalizesthe pipeline status structure




```python
def summarize(self, *args, **kwargs)
```



```python
def table(self, *args, **kwargs)
```






*Version Information: `pipestat` v0.6.0a11, generated by `lucidoc` v0.4.4*
