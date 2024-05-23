<!-- markdownlint-disable -->


# <kbd>module</kbd> `pephubclient.pephubclient`

---


## <kbd>class</kbd> `PEPHubClient`


---

#### <kbd>property</kbd> sample

view represents the PHCSample class which contains all samples API


---

#### <kbd>property</kbd> view

view represents the PHCView class which contains all views API



---

### <kbd>method</kbd> `find_project`

```python
find_project(
    namespace: str,
    query_string: str = '',
    limit: int = 100,
    offset: int = 0,
    filter_by: Literal['submission_date', 'last_update_date'] = None,
    start_date: str = None,
    end_date: str = None
) → SearchReturnModel
```

Find project in specific namespace and return list of PEP annotation 

- 
- - :param namespace: Namespace where to search for projects 
- 
- - :param query_string: Search query 
- 
- - :param limit: Return limit 
- 
- - :param offset: Return offset 
- 
- - :param filter_by: Use filter date. Option: [submission_date, last_update_date] 
- 
- - :param start_date: filter beginning date 
- 
- - :param end_date: filter end date (if none today's date is used) :return: 

---


### <kbd>method</kbd> `load_project`

```python
load_project(
    project_registry_path: str,
    query_param: Optional[dict] = None
) → Project
```

Load peppy project from PEPhub in peppy.Project object 


- :param project_registry_path: registry path of the project 

- :param query_param: query parameters used in get request :return Project: peppy project. 

---


### <kbd>method</kbd> `load_raw_pep`

```python
load_raw_pep(registry_path: str, query_param: Optional[dict] = None) → dict
```

Request PEPhub and return the requested project as peppy.Project object. 


- :param registry_path: Project namespace, eg. "geo/GSE124224:tag" 
- :param query_param: Optional variables to be passed to PEPhub :return: Raw project in dict. 

---


### <kbd>method</kbd> `login`

```python
login() → NoReturn
```

Log in to PEPhub 

---


### <kbd>method</kbd> `logout`

```python
logout() → NoReturn
```

Log out from PEPhub 

---


### <kbd>method</kbd> `pull`

```python
pull(
    project_registry_path: str,
    force: Optional[bool] = False,
    zip: Optional[bool] = False,
    output: Optional[str] = None
) → None
```

Download project locally 


- :param str project_registry_path: Project registry path in PEPhub (e.g. databio/base:default) 
- :param bool force: if project exists, overwrite it. 
- :param bool zip: if True, save project as zip file 
- :param str output: path where project will be saved :return: None 

---


### <kbd>method</kbd> `push`

```python
push(
    cfg: str,
    namespace: str,
    name: Optional[str] = None,
    tag: Optional[str] = None,
    is_private: Optional[bool] = False,
    force: Optional[bool] = False
) → None
```

Push (upload/update) project to Pephub using config/csv path 


- :param str cfg: Project config file (YAML) or sample table (CSV/TSV)  with one row per sample to constitute project 
- :param str namespace: namespace 
- :param str name: project name 
- :param str tag: project tag 
- :param bool is_private: Specifies whether project should be private [Default= False] 
- :param bool force: Force push to the database. Use it to update, or upload project. [Default= False] :return: None 

---


### <kbd>method</kbd> `upload`

```python
upload(
    project: Project,
    namespace: str,
    name: str = None,
    tag: str = None,
    is_private: bool = False,
    force: bool = True
) → None
```

Upload peppy project to the PEPhub. 


- :param peppy.Project project: Project object that has to be uploaded to the DB 
- :param namespace: namespace 
- :param name: project name 
- :param tag: project tag 
- :param force: Force push to the database. Use it to update, or upload project. 
- :param is_private: Make project private 
- :param force: overwrite project if it exists :return: None 




---

_This file was automatically generated via [lazydocs](https://github.com/ml-tooling/lazydocs)._
