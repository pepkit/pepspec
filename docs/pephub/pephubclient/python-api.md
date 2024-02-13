# Using the PEPHubClient Python API

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


