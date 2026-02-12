<img src="img/yacman_logo.svg" alt="yacman" height="70"/><br>
![Run pytests](https://github.com/databio/yacman/workflows/Run%20pytests/badge.svg)
![Test locking parallel](https://github.com/databio/yacman/workflows/Test%20locking%20parallel/badge.svg)
[![codecov](https://codecov.io/gh/databio/yacman/branch/master/graph/badge.svg)](https://codecov.io/gh/databio/yacman)
[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)
[![Anaconda-Server Badge](https://anaconda.org/conda-forge/yacman/badges/version.svg)](https://anaconda.org/conda-forge/yacman)

Yacman is a YAML configuration manager. It provides convenient tools for dealing with YAML configuration files and is part of the PEP ecosystem. Several PEP tools use yacman for managing configuration files.

## Quick start

```python
from yacman import YAMLConfigManager, write_lock

# Create from a file
ym = YAMLConfigManager.from_yaml_file("config.yaml")

# Access values
print(ym["my_key"])

# Update and write safely
ym["new_key"] = "new_value"
with write_lock(ym) as locked_ym:
    locked_ym.rebase()
    locked_ym.write()
```

## Documentation

- [Tutorial](notebooks/tutorial.ipynb) - Interactive notebook with features and usage examples
- [API documentation](code/python-api.md) - Detailed API reference
- [Upgrading guide](upgrading.md) - How to upgrade from v0.x to v1.0
