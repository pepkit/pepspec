<!-- markdownlint-disable -->


# <kbd>module</kbd> `schema.py`



**Global Variables**
---------------
- **PEPHUB_SCHEMA_VERSION_URL**
- **PEPHUB_SCHEMA_VERSIONS_URL**
- **PEPHUB_SCHEMA_NEW_SCHEMA_URL**
- **PEPHUB_SCHEMA_NEW_VERSION_URL**
- **PEPHUB_SCHEMA_RECORD_URL**
- **LATEST_VERSION**


---

## <kbd>class</kbd> `PEPHubSchema`
Class for managing schemas in PEPhub and provides methods for  getting, creating, updating and removing schemas records and schema versions. 


### <kbd>function</kbd> `__init__`

```python
__init__(jwt_data: str = None)
```


- :param jwt_data: jwt token for authorization 




---


### <kbd>function</kbd> `add_version`

```python
add_version(
    namespace: str,
    schema_name: str,
    schema_value: dict,
    version: str = '1.0.0',
    contributors: str = None,
    release_notes: str = None,
    tags: Optional[str, List[str], dict] = None
) → None
```

Add new version to the schema registry 


- :param namespace: Namespace of the schema 
- :param schema_name: Name of the schema record 
- :param schema_value: Schema value itself in dict format 
- :param version: First version of the schema 
- :param contributors: Schema contributors of current version 
- :param release_notes: Release notes for current version 
- :param tags: Tags of the current version. Can be str, list[str], or dict 

:raise: ResponseError if status not 202. :return: None 

---


### <kbd>function</kbd> `create_schema`

```python
create_schema(
    namespace: str,
    schema_name: str,
    schema_value: dict,
    version: str = '1.0.0',
    description: str = None,
    maintainers: str = None,
    contributors: str = None,
    release_notes: str = None,
    tags: Optional[str, List[str], dict] = None,
    lifecycle_stage: str = None,
    private: bool = False
) → None
```

Create a new schema record + version in the database 


- :param namespace: Namespace of the schema 
- :param schema_name: Name of the schema record 
- :param schema_value: Schema value itself in dict format 
- :param version: First version of the schema 
- :param description: Schema description 
- :param maintainers: Schema maintainers 
- :param contributors: Schema contributors of current version 
- :param release_notes: Release notes for current version 
- :param tags: Tags of the current version. Can be str, list[str], or dict 
- :param lifecycle_stage: Stage of the schema record 
- :param private: Weather project should be public or private. Default: False (public) 

:raise: ResponseError if status not 202. :return: None 

---


### <kbd>function</kbd> `delete_schema`

```python
delete_schema(namespace: str, schema_name: str) → None
```

Delete schema from the database 


- :param namespace: Namespace of the schema 
- :param schema_name: Name of the schema version 

---


### <kbd>function</kbd> `delete_version`

```python
delete_version(namespace: str, schema_name: str, version: str) → None
```

Delete schema Version 


- :param namespace: Namespace of the schema 
- :param schema_name: Name of the schema 
- :param version: Schema version 

:raise: ResponseError if status not 202. :return: None 

---


### <kbd>function</kbd> `get`

```python
get(namespace: str, schema_name: str, version: str = 'latest') → dict
```

Get schema value for specific schema version. 


- :param: namespace: namespace of schema 
- :param: schema_name: name of schema 
- :param: version: version of schema 

:return: Schema object as dictionary 

---


### <kbd>function</kbd> `get_versions`

```python
get_versions(namespace: str, schema_name: str) → SchemaVersionResult
```

Get list of versions 


- :param namespace: Namespace of the schema record 
- :param schema_name: Name of the schema record 

:return: {  pagination: PaginationResult  results: List[SchemaVersionAnnotation] } 

---


### <kbd>function</kbd> `update_record`

```python
update_record(
    namespace: str,
    schema_name: str,
    update_fields: Union[dict, UpdateSchemaRecordFields]
) → None
```

Update schema registry data 


- :param namespace: Namespace of the schema 
- :param schema_name: Name of the schema version 
- :param update_fields: dict or pydantic model UpdateSchemaRecordFields:  {  maintainers: str,  lifecycle_stage: str,  private: bool,  name: str,  description: str,  } 

:raise: ResponseError if status not 202. :return: None 

---


### <kbd>function</kbd> `update_version`

```python
update_version(
    namespace: str,
    schema_name: str,
    version: str,
    update_fields: Union[dict, UpdateSchemaVersionFields]
) → None
```

Update released version of the schema. 


- :param namespace: Namespace of the schema 

- :param schema_name: Name of the schema version 
- :param version: Schema version 
- :param update_fields: dict or pydantic model UpdateSchemaVersionFields:  {  contributors: str,  schema_value: str,  release_notes: str,  } 

:raise: ResponseError if status not 202. :return: None 




---

_This file was automatically generated via [lazydocs](https://github.com/ml-tooling/lazydocs)._
