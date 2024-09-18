<!-- markdownlint-disable -->


# <kbd>module</kbd> `pephubclient.modules.sample`




**Global Variables**
---------------
- **PEPHUB_SAMPLE_URL**


---


## <kbd>class</kbd> `PEPHubSample`
Class for managing samples in PEPhub and provides methods for  getting, creating, updating and removing samples. This class is not related to peppy.Sample class. 


### <kbd>method</kbd> `__init__`

```python
__init__(jwt_data: str = None)
```


- :param jwt_data: jwt token for authorization 




---


### <kbd>method</kbd> `create`

```python
create(
    namespace: str,
    name: str,
    tag: str,
    sample_name: str,
    sample_dict: dict,
    overwrite: bool = False
) → None
```

Create sample in project in PEPhub. 


- :param namespace: namespace of project 
- :param name: name of project 
- :param tag: tag of project 
- :param sample_dict: sample dict 
- :param sample_name: sample name 
- :param overwrite: overwrite sample if it exists :return: None 

---


### <kbd>method</kbd> `get`

```python
get(namespace: str, name: str, tag: str, sample_name: str = None) → dict
```

Get sample from project in PEPhub. 


- :param namespace: namespace of project 
- :param name: name of project 
- :param tag: tag of project 
- :param sample_name: sample name :return: Sample object 

---


### <kbd>method</kbd> `remove`

```python
remove(namespace: str, name: str, tag: str, sample_name: str)
```

Remove sample from project in PEPhub. 


- :param namespace: namespace of project 
- :param name: name of project 
- :param tag: tag of project 
- :param sample_name: sample name :return: None 

---


### <kbd>method</kbd> `update`

```python
update(namespace: str, name: str, tag: str, sample_name: str, sample_dict: dict)
```

Update sample in project in PEPhub. 


- :param namespace: namespace of project 
- :param name: name of project 
- :param tag: tag of project 
- :param sample_name: sample name 
- :param sample_dict: sample dict, that contain elements to update, or :return: None 




---

_This file was automatically generated via [lazydocs](https://github.com/ml-tooling/lazydocs)._
