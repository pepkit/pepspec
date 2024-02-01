![Run pytests](https://github.com/pepkit/pipestat/workflows/Run%20pytests/badge.svg)
[![codecov](https://codecov.io/gh/pepkit/pipestat/branch/master/graph/badge.svg?token=O07MXSQZ32)](https://codecov.io/gh/pepkit/pipestat)
[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)
[![GitHub source](https://img.shields.io/badge/source-github-354a75?logo=github)](https://github.com/pepkit/pipestat)


<img src="https://raw.githubusercontent.com/pepkit/pipestat/master/docs/img/pipestat_logo.svg?sanitize=true" alt="pipestat" style="height:70px"/><br>

## What is pipestat?

Pipestat standardizes reporting of pipeline results. It provides 1) a standard specification for how pipeline outputs should be stored; and 2) an implementation to easily write results to that format from within Python or from the command line.

## How does pipestat work?

A pipeline author defines all the outputs produced by a pipeline by writing a JSON-schema. The pipeline then uses pipestat to report pipeline outputs as the pipeline runs, either via the Python API or command line interface. The user configures results to be stored either in a [YAML-formatted file](https://yaml.org/spec/1.2/spec.html) or a [PostgreSQL database](https://www.postgresql.org/). The results are recorded according to the pipestat specification, in a standard, pipeline-agnostic way. This way, downstream software can use this specification to create universal tools for analyzing, monitoring, and visualizing pipeline results that will work with any pipeline or workflow.


# Quick start

## Install pipestat

```console
pip install pipestat
```

## Set environment variables (optional)

```console
export PIPESTAT_RESULTS_SCHEMA=output_schema.yaml
export PIPESTAT_RECORD_IDENTIFIER=my_record
export PIPESTAT_RESULTS_FILE=results_file.yaml
```
Note: When setting environment variables as in the above example, you will need to provide an output_schema.yaml file in your current working directory with the following example data:
```
result_name:
  type: string
  description: "Result Name"
```

## Pipeline results reporting and retrieval
### For these examples below, it is assumed that the proper environment variables (see above) have been set.

### Report a result

From command line:

```console
pipestat report -i result_name -v 1.1
```

From Python:

```python
import pipestat

psm = pipestat.PipestatManager()
psm.report(values={"result_name": 1.1})
```

### Retrieve a result

From command line:

```console
pipestat retrieve -r my_record
```

From Python:

```python
import pipestat

psm = pipestat.PipestatManager()
psm.retrieve_one(result_identifier="result_name")
```

## Pipeline status management

## Set status

From command line:

```console
pipestat status set running
```

From Python:

```python
import pipestat

psm = pipestat.PipestatManager()
psm.set_status(status_identifier="running")
```

## Get status

From command line:

```console
pipestat status get
```

From Python:

```python
import pipestat

psm = pipestat.PipestatManager()
psm.get_status()
```
