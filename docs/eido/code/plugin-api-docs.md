# Eido Built-in Filters API

## Overview

Eido provides built-in filter functions that can transform PEP projects into different output formats. These filters are useful for converting PEPs to various representations like YAML, CSV, or other formats.

### Available Filters

Eido includes several built-in filters for converting and exporting PEP data:

- **basic_pep_filter**: Returns the basic PEP representation
- **yaml_pep_filter**: Converts PEP to YAML format
- **csv_pep_filter**: Exports sample tables as CSV
- **yaml_samples_pep_filter**: Exports only sample data as YAML

## API Reference

### Filter Functions

::: eido.basic_pep_filter
    options:
      docstring_style: google
      show_source: true
      show_signature: true

::: eido.yaml_pep_filter
    options:
      docstring_style: google
      show_source: true
      show_signature: true

::: eido.csv_pep_filter
    options:
      docstring_style: google
      show_source: true
      show_signature: true

::: eido.yaml_samples_pep_filter
    options:
      docstring_style: google
      show_source: true
      show_signature: true
