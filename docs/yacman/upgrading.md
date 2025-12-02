# Upgrading to yacman v1.0

## Overview

Yacman v1.0 provides two major feature upgrades:

1. **New constructor pattern**: Constructors now use `YAMLConfigManager.from_x(...)` methods to make object creation clearer
2. **Separate read/write locks**: Locks are now separated into read locks and write locks, allowing multiple simultaneous readers

## Upgrading from v0.9.3 to v1.0.0

### Step 1: Update imports

If you were using `FutureYAMLConfigManager` in v0.9.3, update your imports:

**Before (v0.9.3):**
```python
from yacman import FutureYAMLConfigManager as YAMLConfigManager
```

**After (v1.0.0):**
```python
from yacman import YAMLConfigManager
```

### Step 2: Update context managers

Context managers now use explicit `write_lock` or `read_lock` functions:

```python
from yacman import write_lock, read_lock
```

**Before (v0.9.3):**
```python
with ym as locked_ym:
    locked_ym.write()
```

**After (v1.0.0):**
```python
with write_lock(ym) as locked_ym:
    locked_ym.rebase()
    locked_ym.write()
```

**Important**: In v1.0, you must call `rebase()` before `write()` if you want to allow for multiple processes that may have written to the file since you read it in.

### Step 3: Update constructors

You can no longer create a `YAMLConfigManager` object directly. Use the `from_x()` constructor methods instead:

**Before (v0.9.3):**
```python
ym = YAMLConfigManager(filepath="config.yaml")
ym = YAMLConfigManager(entries={"key": "value"})
```

**After (v1.0.0):**
```python
from yacman import YAMLConfigManager

# From a file
ym = YAMLConfigManager.from_yaml_file("config.yaml")

# From a dictionary
data = {"key": "value"}
ym = YAMLConfigManager.from_obj(data)

# From a YAML string
yaml_data = "key: value"
ym = YAMLConfigManager.from_yaml_data(yaml_data)
```

### Step 4: Update file loading with overrides

In the past, you could load from a file and overwrite some attributes with a dict, all from the constructor. This is now more explicit:

**Before (v0.9.3):**
```python
ym = YAMLConfigManager(filepath="config.yaml", entries={"override_key": "value"})
```

**After (v1.0.0):**
```python
ym = YAMLConfigManager.from_yaml_file("config.yaml")
ym.update_from_obj({"override_key": "value"})
```

## Complete examples

### Example 1: Basic usage with locks

```python
from yacman import YAMLConfigManager, write_lock, read_lock

data = {
    "my_list": [1, 2, 3],
    "my_int": 8,
    "my_str": "hello world!",
    "my_dict": {"nested_val": 15}
}

# Create from object
ym = YAMLConfigManager.from_obj(data)

# Access values
print(ym["my_list"])
print(ym["my_int"])
print(ym["my_dict"])

# Modify and write with a write lock
ym["new_var"] = 15

with write_lock(ym) as locked_ym:
    locked_ym.rebase()  # Capture any changes since file was loaded
    locked_ym.write()
```

### Example 2: Read locks

```python
# Use a read lock to rebase
# This will replay any in-memory updates on top of whatever is re-read from the file
with read_lock(ym) as locked_ym:
    locked_ym.rebase()

# Use a read lock to reset the in-memory object to whatever is on disk
with read_lock(ym) as locked_ym:
    locked_ym.reset()
```

### Example 3: Expanding environment variables

To expand environment variables in values, use the `.exp` attribute:

```python
ym = YAMLConfigManager.from_yaml_file("config.yaml")
expanded_value = ym.exp["path_with_env_vars"]
```

## Migration checklist

- [ ] Update imports from `FutureYAMLConfigManager` to `YAMLConfigManager`
- [ ] Replace direct constructor calls with `from_yaml_file()`, `from_obj()`, or `from_yaml_data()`
- [ ] Update context managers to use `write_lock()` or `read_lock()`
- [ ] Add `rebase()` calls before `write()` in write-lock contexts
- [ ] Replace combined file+override constructors with explicit `update_from_obj()` calls
- [ ] Test all file I/O operations
- [ ] Verify environment variable expansion works correctly

## Deprecated features

The following are deprecated in v1.0 and will be removed in future versions:

- Direct instantiation of `YAMLConfigManager` (use `from_x()` methods instead)
- Using YAMLConfigManager object as a context manager directly (use `write_lock()` or `read_lock()`)
- `YacAttMap` class (replaced by `YAMLConfigManager`)
