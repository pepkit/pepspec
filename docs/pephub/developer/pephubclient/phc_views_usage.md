<!-- markdownlint-disable -->


# <kbd>module</kbd> `pephubclient.modules.view`




**Global Variables**
---------------
- **PEPHUB_VIEW_URL**
- **PEPHUB_VIEW_SAMPLE_URL**


---


## <kbd>class</kbd> `PEPHubView`
Class for managing views in PEPhub and provides methods for  getting, creating, updating and removing views. 

This class aims to warp the Views API for easier maintenance and better user experience. 


### <kbd>method</kbd> `__init__`

```python
__init__(jwt_data: str = None)
```


- :param jwt_data: jwt token for authorization 




---


### <kbd>method</kbd> `add_sample`

```python
add_sample(
    namespace: str,
    name: str,
    tag: str,
    view_name: str,
    sample_name: str
)
```

Add sample to view in project in PEPhub. 


- :param namespace: namespace of project 
- :param name: name of project 
- :param tag: tag of project 
- :param view_name: name of the view 
- :param sample_name: name of the sample 

---


### <kbd>method</kbd> `create`

```python
create(
    namespace: str,
    name: str,
    tag: str,
    view_name: str,
    description: str = None,
    sample_list: list = None,
    no_fail: bool = False
)
```

Create view in project in PEPhub. 


- :param namespace: namespace of project 
- :param name: name of project 
- :param tag: tag of project 
- :param description: description of the view 
- :param view_name: name of the view 
- :param sample_list: list of sample names 
- :param no_fail: whether to raise an error if view was not added to the project 

---


### <kbd>method</kbd> `delete`

```python
delete(namespace: str, name: str, tag: str, view_name: str) → None
```

Delete view from project in PEPhub. 


- :param namespace: namespace of project 
- :param name: name of project 
- :param tag: tag of project 
- :param view_name: name of the view :return: None 

---


### <kbd>method</kbd> `get`

```python
get(
    namespace: str,
    name: str,
    tag: str,
    view_name: str,
    raw: bool = False
) → Union[Project, dict]
```

Get view from project in PEPhub. 


- :param namespace: namespace of project 
- :param name: name of project 
- :param tag: tag of project 
- :param view_name: name of the view 
- :param raw: if True, return raw response :return: peppy.Project object or dictionary of the project (view) 

---


### <kbd>method</kbd> `remove_sample`

```python
remove_sample(
    namespace: str,
    name: str,
    tag: str,
    view_name: str,
    sample_name: str
)
```

Remove sample from view in project in PEPhub. 


- :param namespace: namespace of project 
- :param name: name of project 
- :param tag: tag of project 
- :param view_name: name of the view 
- :param sample_name: name of the sample :return: None 




---

_This file was automatically generated via [lazydocs](https://github.com/ml-tooling/lazydocs)._
