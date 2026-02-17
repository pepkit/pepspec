# <img src="https://raw.githubusercontent.com/pepkit/pipestat/master/docs/img/pipestat_logo.svg?sanitize=true" alt="pipestat" class="img-header"/>

<p align="center">
<a href="https://pep.databio.org" alt="PEP compatible"><img src="https://pepkit.github.io/img/PEP-compatible-green.svg"/></a>
<a href="https://github.com/pepkit/pipestat/actions/workflows/run-pytest.yml" alt="Run pytests"><img src="https://github.com/pepkit/pipestat/workflows/Run%20pytests/badge.svg"/></a>
<a href="https://pypi.org/project/pipestat" alt="PyPI badge"><img src="https://img.shields.io/pypi/v/eido"/></a>
<a href="https://github.com/pepkit/pipestat" alt="GitHub source code"><img src="https://img.shields.io/badge/source-github-354a75?logo=github"/></a>
</p>


## What is pipestat?

Pipestat standardizes reporting of pipeline results. It provides 1) a standard specification for how pipeline outputs should be stored; and 2) an implementation to easily write results to that format from within Python or from the command line.

## How does pipestat work?

A pipeline author defines all the outputs produced by a pipeline by writing a JSON-schema. The pipeline then uses pipestat to report pipeline outputs as the pipeline runs, either via the Python API or command line interface. The user configures results to be stored either in a [YAML-formatted file](https://yaml.org/spec/1.2/spec.html), a [PostgreSQL database](https://www.postgresql.org/) or on [PEPhub](https://pephub.databio.org/). The results are recorded according to the pipestat specification, in a standard, pipeline-agnostic way. This way, downstream software can use this specification to create universal tools for analyzing, monitoring, and visualizing pipeline results that will work with any pipeline or workflow.

<!-- TODO: This needs a graphical representation here. -->

## Quick start
Check out the [quickstart guide](./code/api-quickstart.md). See [API Usage](./code/python-tutorial.md) and [CLI Usage](./code/cli.md).
