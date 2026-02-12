# Package `yacman` Documentation

## Package Overview

Yacman is a YAML configuration manager that provides convenience tools for dealing with YAML configuration files. It's designed for safe, concurrent access to configuration data with file locking support and a flexible attribute-based access pattern.

### Key Features

- **Attribute-Based Access**: Access YAML data as object attributes
- **File Locking**: Race-free reading and writing in multi-user contexts
- **Flexible Construction**: Create from files, strings, or dictionaries
- **Path Expansion**: Automatically expand environment variables and paths
- **Alias Support**: Define custom aliases for configuration keys
- **Context Managers**: Safe read and write operations with locking

### Installation

```bash
pip install yacman
```

### Quick Example

```python
from yacman import YAMLConfigManager

# Create from a file
ym = YAMLConfigManager.from_yaml_file("config.yaml")

# Access values
print(ym["my_key"])

# Update and write safely
ym["new_key"] = "new_value"
from yacman import write_lock
with write_lock(ym) as locked_ym:
    locked_ym.rebase()
    locked_ym.write()
```

## API Reference

### YAMLConfigManager Class

The main class for managing YAML configuration files with locking support:

::: yacman.YAMLConfigManager
    options:
      docstring_style: google
      show_source: true
      show_signature: true
      merge_init_into_class: true

### Context Managers

Yacman provides context managers for safe file locking. These are re-exported from the `ubiquerg` package for convenience.

#### `write_lock(config_manager)`

Context manager for write operations with exclusive locking. Prevents other processes from reading or writing the file while you hold the lock.

**Parameters:**
- `config_manager` (YAMLConfigManager): The configuration manager instance to lock

**Returns:**
- YAMLConfigManager: The locked configuration manager

**Usage:**
```python
from yacman import YAMLConfigManager, write_lock

ym = YAMLConfigManager.from_yaml_file("config.yaml")
ym["key"] = "value"

with write_lock(ym) as locked_ym:
    locked_ym.rebase()  # Sync with any file changes
    locked_ym.write()   # Write to disk
```

#### `read_lock(config_manager)`

Context manager for read operations with shared locking. Multiple processes can hold read locks simultaneously, but no process can hold a write lock while read locks exist.

**Parameters:**

- `config_manager` (YAMLConfigManager): The configuration manager instance to lock

**Returns:**

- YAMLConfigManager: The locked configuration manager

**Usage:**

```python
from yacman import YAMLConfigManager, read_lock

ym = YAMLConfigManager.from_yaml_file("config.yaml")

with read_lock(ym) as locked_ym:
    locked_ym.rebase()  # Sync with file
    print(locked_ym.to_dict())
```

**Note:** These context managers are provided by the `ubiquerg` package and re-exported by yacman for convenience. For more details on the locking implementation, see the [ubiquerg documentation](https://github.com/databio/ubiquerg).

See the [tutorial](../notebooks/tutorial.ipynb) for more examples.

### Utility Functions

Yacman provides several utility functions for working with YAML files and paths:

- `load_yaml(filepath)`: Load a YAML file and return its contents as a dictionary
- `select_config(config_filepath, config_env_vars, default_config_filepath)`: Select a configuration file from multiple sources
- `expandpath(path)`: Expand environment variables and user home directory in a path

These functions are available in the `yacman` module. See the source code or [tutorial](../notebooks/tutorial.ipynb) for usage examples.

## Deprecated Classes (v0.x)

The following classes are deprecated in v1.0 and maintained only for backwards compatibility. Use `YAMLConfigManager` instead:

- `YacAttMap` - Replaced by `YAMLConfigManager`
- `AliasedYacAttMap` - Use `YAMLConfigManager` instead

See the [upgrading guide](../upgrading.md) for migration instructions.
