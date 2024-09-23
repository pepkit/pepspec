# PEPHub Client

User guide for the PEPHub client.

PEPhubclient is available as Python API and CLI. This document will guide you through the usage of the PEPHub client.

## Installation

To install PEPHubClient from PyPI, use the following command:

```bash
pip install pephubclient
```

To install `pephubclient` from the [GitHub repository](https://github.com/pepkit/pephubclient), use the following command:

```bash
pip install git+https://github.com/pepkit/pephubclient.git
```

## Authentication

To login, use the `login` command:

```
phc login
```


## Using the PEPHubClient CLI

PEPHubClient provides a CLI for interacting with PEPhub.
You can find the list of available commands here:
[PEPHubClient CLI](cli.md)


## Using the PEPHubClient Python API

```python
from pephubclient import PEPHubClient

# initiate pephubclient object
phc = PEPHubClient()

# load pep as peppy.Project object
example_pep = phc.load_project("databio/example:default")
print(example_pep)

# Printed: 
## Project
## 6 samples: 4-1_11102016, 3-1_11102016, 2-2_11102016, 2-1_11102016, 8-3_11152016, 8-1_11152016
## Sections: pep_version, sample_table, name, description

# To upload a project:
phc.upload(example_pep, namespace="databio", name="example", force=True)
```

Full documentation for the Python API can be found here:

- [PEPHubClient Python API](./phc_usage.md)
- [PEPHubClient Python API - Samples](./phc_samples_usage.md)
- [PEPHubClient Python API - Views](./phc_views_usage.md)

----
If you have any questions or need help, please contact us at [databio.org](https://databio.org)