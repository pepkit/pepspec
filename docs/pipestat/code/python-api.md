# Package `pipestat` Documentation

## Package Overview

The `pipestat` package standardizes reporting of pipeline results and pipeline status management. It provides a formal way for pipeline developers and downstream tools to communicate pipeline outputs and status.

### Key Features

- **Results Reporting**: Standardized API for reporting pipeline results
- **Status Management**: Track pipeline execution status
- **Backend Flexibility**: Store results in YAML files or databases
- **Schema Validation**: Validate results against defined schemas
- **Multi-pipeline Support**: Manage results from multiple pipelines

### Installation

```bash
pip install pipestat
```

### Quick Example

```python
from pipestat import SamplePipestatManager

# Initialize with a schema and results file
psm = SamplePipestatManager(
    schema_path="output_schema.yaml",
    results_file_path="results.yaml"
)

# Report a result
psm.report(record_identifier="sample1", values={"result_name": 42})
```

## API Reference

### SamplePipestatManager Class

The main class for managing sample-level pipeline results:

::: pipestat.SamplePipestatManager
    options:
      docstring_style: google
      show_source: true
      show_signature: true
      merge_init_into_class: true

### ProjectPipestatManager Class

::: pipestat.ProjectPipestatManager
    options:
      docstring_style: google
      show_source: true
      show_signature: true
      merge_init_into_class: true

### Exceptions

::: pipestat.PipestatError
    options:
      docstring_style: google
      show_source: true
      show_signature: true
      merge_init_into_class: true
