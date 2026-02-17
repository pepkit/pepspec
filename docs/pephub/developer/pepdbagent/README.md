[![PEP compatible](https://pepkit.github.io/img/PEP-compatible-green.svg)](https://pep.databio.org/)
![Run pytests](https://github.com/pepkit/pepdbagent/workflows/Run%20pytests/badge.svg)
[![pypi-badge](https://img.shields.io/pypi/v/pepdbagent?color=%2334D058)](https://pypi.org/project/pepdbagent)
[![pypi-version](https://img.shields.io/pypi/pyversions/pepdbagent.svg?color=%2334D058)](https://pypi.org/project/pepdbagent)
[![Downloads](https://static.pepy.tech/badge/pepdbagent)](https://pepy.tech/project/pepdbagent)
[![Github badge](https://img.shields.io/badge/source-github-354a75?logo=github)](https://github.com/pepkit/pepdbagent)



<h1 align="center">pepdbagent</h1>


---

**Documentation**: <a href="https://pep.databio.org/pephub/developer/pepdbagent/" target="_blank">https://pep.databio.org/pephub/developer/pepdbagent/</a>

**Source Code**: <a href="https://github.com/pepkit/pepdbagent" target="_blank">https://github.com/pepkit/pepdbagent</a>

---

`pepdbagent` is a Python library and toolkit that gives a user-friendly 
interface to connect, upload, update and retrieve information from pep database. This library is designed to work 
to be used by PEPhub, but it can be used for any other purpose, to manage data in pep database.

pepdbagent creates a connection to the database and creates table schemas for the PEPhub database if necessary.
Core database is `postgres` database, but it can be easily extended to other relational databases.
To use `pepdbagent`, you need to have a database instance running with it's credentials.
If the version of the database schema is not compatible with the version of `pepdbagent`, it will throw an exception.

## Installation
To install `pepdbagent` use this command: 
```
pip install pepdbagent
```
or install the latest version from the GitHub repository:
```
pip install git+https://github.com/pepkit/pepdbagent.git
```

---
## Overview:

The pepdbagent provides a core class called **PEPDatabaseAgent**. This class has 4 modules, divided 
to increase readability, maintainability, and user experience of pepdbagent, which are:

**The `pepdbagent` consists of 6 main modules:**
- <u>Namespace</u>: Includes methods for searching namespaces, retrieving statistics, and fetching information.
- <u>Project</u>: Provides functionality for retrieving, uploading, updating, and managing projects.
- <u>Annotation</u>: Offers features for searching projects in the database and namespaces, retrieving annotations, and other related information.
- <u>Sample</u>: Handles the creation, modification, and deletion of samples, without modification of the entire project.
- <u>View</u>: Manages the creation, modification, and deletion of views for specific projects.
- <u>User</u>: Contains user-related information such as favorites and other user-related data.

## Example:

#### Instiantiate a PEPDatabaseAgent object and connect to database:

```python
import pepdbagent
# 1) By providing credentials and connection information:
agent = pepdbagent.PEPDatabaseAgent(user="postgres", password="docker", )
# 2) or By providing connection string:
agent = pepdbagent.PEPDatabaseAgent(dsn="postgresql://postgres:docker@localhost:5432/pep-db")
```

#### Example of usage of the pepdbagent modules:

```python
import peppy

prj_obj = peppy.Project("sample_pep/basic/project_config.yaml")

# create a project
namespace = "demo"
name = "basic_project"
tag = None
agent.project.create(prj_obj, namespace, name, tag)

update_dict = {"is_private" = True}
# after creation of the dict, update record by providing update_dict and namespace, name and tag:
agent.project.update(update_dict, namespace, name, tag)
```


#### Annotation example:


The `.annotation` module provides an interface to PEP annotations. 
PEP annotations refers to the information *about* the PEPs (or, the PEP metadata). 
Retrieved information contains: [number of samples, submission date, last update date,
is private, PEP description, digest, namespace, name, tag]

```python

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

# By default get function will return annotations for public projects,
# To get annotation including private projects admin list should be provided.
# admin list means list of namespaces where user has admin rights
# For example:
agent.annotation.get(query='search_pattern', admin=['databio', 'ncbi'])
```


#### Namespace
The `.namespace` module contains search namespace functionality that helps to find namespaces in database 
and retrieve information: `number of samples`, `number of projects`.

Example:
```python
# Get info about namespace by providing query argument. Then pepdbagent will
# search for a specified pattern of namespace in database.
agent.namespace.get(query='Namespace')

# By default all get function will return namespace information for public projects,
# To get information with private projects, admin list should be provided.
# admin list means list of namespaces where user has admin rights
# For example:
agent.namespace.get(query='search_pattern', admin=['databio', 'geo', 'ncbi'])
```
For more information, developers should use `pepdbagent pytest` as documentation due to its natural language syntax and the 
ability to write tests that serve as executable examples. 
This approach not only provides detailed explanations but also ensures that code examples are kept 
up-to-date with the latest changes in the codebase.