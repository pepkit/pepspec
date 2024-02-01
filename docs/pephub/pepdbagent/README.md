[![GitHub source](https://img.shields.io/badge/source-github-354a75?logo=github)](https://github.com/pepkit/pepdbagent)

# pepdbagent

`pepdbagent` is a Python package for uploading, updating, and retrieving [PEP](http://pep.databio.org/en/latest/) metadata from a Postgres database.

The pepdbagent provides a core class called **PEPDatabaseAgent**. This class has 3 modules, divided 
to increase readability, maintainability, and user experience of pepdbagent, which are: **Projects**, 
**Project Annotations**, and **Namespace Annotations**.  Below, we describe each module in detail:

## PEPDatabaseAgent
PEPDatabaseAgent is the primary class that you will use. It connects to the database (using **BaseConnection** class).

Example: Instiantiate a PEPDatabaseAgent object and connect to database:

```python

import pepdbagent
# 1) By providing credentials and connection information:
agent = pepdbagent.PEPDatabaseAgent(user="postgres", password="docker", )
# 2) or By providing connection string:
agent = pepdbagent.PEPDatabaseAgent(dsn="postgresql://postgres:docker@localhost:5432/pep-db")
```

This `agent` object will provide 3 sub-modules, corresponding to the 3 main entity types stored in PEPhub: `agent.project`,  `agent.annotation`, and `agent.namespace`.

## Project

The `.project` module is used to create, update, retrieve, and delete projects.

Example:

```python
import peppy

prj_obj = peppy.Project("sample_pep/basic/project_config.yaml")

# create a project
namespace = "demo"
name = "basic_project"
tag = None
agent.project.create(prj_obj, namespace, name, tag)

# updating record in database (project)
# To update record in the db user should provide `update_dict`,
# that can contains any of 4 keys: [project, is_private, name, tag]
# examples of update_dict:
update_dict1 = {"is_private" = True}
update_dict2 = {"is_private" = True, name = "new_name"}
update_dict3 = {"project" = prj_obj, "is_private" = True}
update_dict4 = {"project" = prj_obj}
update_dict4 = {"tag" = "new_tag"}

# after creation of the dict, update record by providing update_dict and namespace, name and tag:
agent.project.update(update_dict, namespace, name, tag, )

# retrieve a project
agent.project.get(namespace, name, tag)

# delete a project
agent.project.delete(namespace, name, tag)
```

## Annotation

The `.annotation` module provides an interface to PEP annotations. 
PEP annotations refers to the information *about* the PEPs (or, the PEP metadata). 
Retrieved information contains: [number of samples, submission date, last update date,
is private, PEP description, digest, namespace, name, tag]

Example:
```python
# Get annotation of one project:
agent.annotation.get(namespace, name, tag)

# Get annotations of all projects from db:
agent.annotation.get()

# Get annotations of all projects within a given namespace:
agent.annotation.get(namespace='namespace')

# Search for a project with partial string matching, either within namespace or entire database
# This returns a list of projects
agent.annotation.get(query='query')
agent.annotation.get(query='query', namespace='namespace')

# Get annotation of multiple projects given a list of registry paths
agent.annotation.get_by_rp(["namespace1/project1:tag1", "namespace2/project2:tag2"])

# By default get function will retrun annotations for public projects,
# To get annotation including private projects admin list should be provided.
# admin list means list of namespaces where user has admin rights
# For example:
agent.annotation.get(query='search_pattern', admin=['databio', 'ncbi'])
```
Return Example:
```python
# annotation.get return type is pydantic model - AnnotationRetrunModel
AnnotationRetrunModel(count=1,
                      limit=100, 
                      offset=0,
                      results=[AnnotationModel(namespace='databio', 
                                               name='test', 
                                               tag='default', 
                                               is_private=False, 
                                               number_of_samples=8, 
                                               description=None, 
                                               last_update_date='2022-11-09', 
                                               submission_date='2023-01-09', 
                                               digest='36bb973f2eca3706ed9852abddd',
                                               pep_schema="bedmake")])
```


# Namespace
The `.namespace` module contains search namespace functionality that helps to find namespaces in database 
and retrieve information: `number of samples`, `number of projects`.

Example:
```python
# Get info about namespace by providing query argument. Then pepdbagent will
# search for a specified pattern of namespace in database.
agent.namespace.get(query='Namespace')

# By default all get function will retrun namespace information for public projects,
# To get information with private projects, admin list should be provided.
# admin list means list of namespaces where user has admin rights
# For example:
agent.namespace.get(query='search_pattern', admin=['databio', 'geo', 'ncbi'])
```
Return Example:
```python
# namespace.get return type is pydantic model - NamespaceReturnModel
NamespaceReturnModel(count=1, 
                     limit=100, 
                     offset=0, 
                     results=[NamespaceResultModel(namespace='databio', number_of_projects=6, number_of_samples=470)])
```


# Example PEPs
To populate database with example peps use function written in manual tests: [Manual test](../manual_tests.py)