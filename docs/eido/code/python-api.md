# Package `eido` Documentation

## Package Overview

The `eido` package provides validation and filtering tools for PEPs (Portable Encapsulated Projects). It enables schema-based validation of project metadata and provides flexible filtering mechanisms.

### Key Features

- **Schema Validation**: Validate PEPs against JSON schemas
- **Sample Filtering**: Filter samples based on custom criteria
- **Config Validation**: Validate project configuration separately
- **Extensible Filtering**: Support for custom filter plugins
- **Error Reporting**: Detailed validation error messages

### Installation

```bash
pip install eido
```

### Quick Example

```python
from eido import validate_project
from peppy import Project

# Load a project
prj = Project("project_config.yaml")

# Validate against a schema
validate_project(prj, "schema.yaml")
```

## API Reference

### Validation Functions

::: eido.validate_project
    options:
      docstring_style: google
      show_source: true
      show_signature: true

::: eido.validate_sample
    options:
      docstring_style: google
      show_source: true
      show_signature: true

::: eido.validate_config
    options:
      docstring_style: google
      show_source: true
      show_signature: true

### Schema Functions

::: eido.read_schema
    options:
      docstring_style: google
      show_source: true
      show_signature: true

### Exceptions

::: eido.EidoValidationError
    options:
      docstring_style: google
      show_source: true
      show_signature: true
      merge_init_into_class: true
