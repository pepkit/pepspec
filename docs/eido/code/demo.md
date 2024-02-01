# Python API usage

There are 3 validation functions in the public `eido` package interface:

- `validate_project` to validate the entire PEP
- `validate_sample` to validate only a selected sample
- `validate_config` to validate only the config part of the PEP

Additionally there is a `read_schema` function that lets you read the schema.

## Schema reading

As noted above `read_schema` function can be used to read a YAML-formatted schema to Python. Depending on the class of the argument used, it will get a remote schema (argument is a URL) or will read one from disk (argument is a path).

### Remote


```python
from eido import *

read_schema("https://schema.databio.org/pep/2.0.0.yaml")
```




    [{'description': 'Schema for a minimal PEP',
      'version': '2.0.0',
      'properties': {'config': {'properties': {'name': {'type': 'string',
          'pattern': '^\\S*$',
          'description': 'Project name with no whitespace'},
         'pep_version': {'description': 'Version of the PEP Schema this PEP follows',
          'type': 'string'},
         'sample_table': {'type': 'string',
          'description': 'Path to the sample annotation table with one row per sample'},
         'subsample_table': {'type': 'string',
          'description': 'Path to the subsample annotation table with one row per subsample and sample_name attribute matching an entry in the sample table'},
         'sample_modifiers': {'type': 'object',
          'properties': {'append': {'type': 'object'},
           'duplicate': {'type': 'object'},
           'imply': {'type': 'array',
            'items': {'type': 'object',
             'properties': {'if': {'type': 'object'},
              'then': {'type': 'object'}}}},
           'derive': {'type': 'object',
            'properties': {'attributes': {'type': 'array',
              'items': {'type': 'string'}},
             'sources': {'type': 'object'}}}},
          'project_modifiers': {'type': 'object',
           'properties': {'amend': {'description': 'Object overwriting original project attributes',
             'type': 'object'},
            'import': {'description': 'List of external PEP project config files to import',
             'type': 'array',
             'items': {'type': 'string'}}}}}},
        'required': ['pep_version']},
       'samples': {'type': 'array',
        'items': {'type': 'object',
         'properties': {'sample_name': {'type': 'string',
           'pattern': '^\\S*$',
           'description': 'Unique name of the sample with no whitespace'}},
         'required': ['sample_name']}}},
      'required': ['samples']}]



With this simple call the PEP2.0.0 schema was downloaded from a remote file server and read into a `dict` object in Python.

### Local


```python
read_schema("../tests/data/schemas/test_schema.yaml")
```




    [{'description': 'test PEP schema',
      'properties': {'dcc': {'type': 'object',
        'properties': {'compute_packages': {'type': 'object'}}},
       'samples': {'type': 'array',
        'items': {'type': 'object',
         'properties': {'sample_name': {'type': 'string'},
          'protocol': {'type': 'string'},
          'genome': {'type': 'string'}}}}},
      'required': ['samples']}]



This time the schema was read from disk.

## Schema imports

`eido` lets you import schemas. Schema importing is a very powerful tool to make a cascading system of schemas that will keep the individual building blocks clear and simple.

To import a schema from within a schema one just needs to use an `imports` section somewhere in the schema. The section has to be a YAML list, for example:

```yaml
imports:
    - ../tests/data/schemas/test_schema.yaml
    - https://schema.databio.org/pep/2.0.0.yaml
```

or 

```yaml
imports: [../tests/data/schemas/test_schema.yaml, https://schema.databio.org/pep/2.0.0.yaml]
```

This functionality is particularly useful when one wants to restrict an object that already has a remote schema defined for. For example, to restrict the type of one more sample attribute in a `Project` object (defined by PEP2.0.0 schema).

```yaml
imports:
    - https://schema.databio.org/pep/2.0.0.yaml
description: "Schema for a more restrictive PEP"
properties:
  samples:
    type: array
    items:
      type: object
      properties:
        my_numeric_attribute: 
          type: integer
          minimum: 0
          maximum: 1
      required:
        - my_numeric_attribute
required:
  - samples
```

PEPs to succesfully validate against this schema will need to fulfill all the generic PEP2.0.0 schema requirements _and_ fulfill the new `my_numeric_attribute` requirement.

### How importing works

The output of the `read_schema` function is always a `list` object. In case there are no imports in the read schema it's just a `list` of length 1. 

If there are import statements the `list` length reflects the number of schemas imported. Please note that the schemas can be imported recursively, which means that an imported schema can import more schemas. 

**The order of the output list is meaningful:**

1. It reflects the order of importing in the "schema dependency chain"; the schema used in the `read_schema` call is always last in the output list.
2. It reflects the order of enumerating schemas in the `imports` section; the order is preserved

This in turn implies the order of the validation in the functions described in detail below.

## Entire PEP validation


```python
from peppy import Project
```

Within Python the `validate_project` function can be used to perform the entire PEP validation. It requires `peppy.Project` object and either a path to the YAML schema file or a read schema (`dict`) as inputs.


```python
p = Project("../tests/data/peps/test_cfg.yaml")
validate_project(project=p, schema="../tests/data/schemas/test_schema.yaml")

from eido.eido import load_yaml

s = _load_yaml("../tests/data/schemas/test_schema.yaml")
validate_project(project=p, schema=s)
```

If a validation is successful, no message is printed. An unsuccessful one is signalized with a corresponding `jsonschema.exceptions.ValidationError`


```python
validate_project(project=p, schema="../tests/data/schemas/test_schema_invalid.yaml")
```


    ---------------------------------------------------------------------------

    ValidationError                           Traceback (most recent call last)

    <ipython-input-6-29fa9395c52f> in <module>
    ----> 1 validate_project(project=p, schema="../tests/data/schemas/test_schema_invalid.yaml")
    

    /Library/Frameworks/Python.framework/Versions/3.6/lib/python3.6/site-packages/eido/eido.py in validate_project(project, schema, exclude_case)
        112     for schema_dict in schema_dicts:
        113         project_dict = project.to_dict()
    --> 114         _validate_object(project_dict, _preprocess_schema(schema_dict), exclude_case)
        115         _LOGGER.debug("Project validation successful")
        116 


    /Library/Frameworks/Python.framework/Versions/3.6/lib/python3.6/site-packages/eido/eido.py in _validate_object(object, schema, exclude_case)
         93     """
         94     try:
    ---> 95         jsonschema.validate(object, schema)
         96     except jsonschema.exceptions.ValidationError as e:
         97         if not exclude_case:


    /Library/Frameworks/Python.framework/Versions/3.6/lib/python3.6/site-packages/jsonschema/validators.py in validate(instance, schema, cls, *args, **kwargs)
        932     error = exceptions.best_match(validator.iter_errors(instance))
        933     if error is not None:
    --> 934         raise error
        935 
        936 


    ValidationError: 'invalid' is a required property
    
    Failed validating 'required' in schema:
        {'description': 'test PEP schema',
         'properties': {'_samples': {'items': {'properties': {'genome': {'anyOf': [{'type': 'string'},
                                                                                   {'items': {'type': 'string'},
                                                                                    'type': 'array'}]},
                                                              'protocol': {'anyOf': [{'type': 'string'},
                                                                                     {'items': {'type': 'string'},
                                                                                      'type': 'array'}]},
                                                              'sample_name': {'anyOf': [{'type': 'string'},
                                                                                        {'items': {'type': 'string'},
                                                                                         'type': 'array'}]}},
                                               'type': 'object'},
                                     'type': 'array'},
                        'dcc': {'properties': {'compute_packages': {'type': 'object'}},
                                'type': 'object'},
                        'invalid': {'type': 'string'}},
         'required': ['_samples', 'invalid']}
    
    On instance:
        {'_config': {'name': 'test',
                     'output_dir': 'test',
                     'pep_version': '2.0.0',
                     'sample_modifiers': {'append': {'organism': {'Homo sapiens': {'genome': 'hg38'}}}},
                     'sample_table': '/Users/mstolarczyk/code/eido/tests/data/peps/test_sample_table.csv'},
         '_config_file': '/Users/mstolarczyk/code/eido/tests/data/peps/test_cfg.yaml',
         '_sample_df':   sample_name protocol genome
        0  GSM1558746      GRO   hg38
        1  GSM1480327      PRO   hg38,
         '_sample_table':             genome                              organism protocol sample_name
        sample_name                                                                  
        GSM1558746    hg38  {'Homo sapiens': {'genome': 'hg38'}}      GRO  GSM1558746
        GSM1480327    hg38  {'Homo sapiens': {'genome': 'hg38'}}      PRO  GSM1480327,
         '_samples': [{'_attributes': ['sample_name', 'protocol', 'genome'],
                       '_derived_cols_done': [],
                       '_project': {'_config': {'name': 'test',
                                                'output_dir': 'test',
                                                'pep_version': '2.0.0',
                                                'sample_modifiers': {'append': {'organism': {'Homo sapiens': {'genome': 'hg38'}}}},
                                                'sample_table': '/Users/mstolarczyk/code/eido/tests/data/peps/test_sample_table.csv'},
                                    '_config_file': '/Users/mstolarczyk/code/eido/tests/data/peps/test_cfg.yaml',
                                    '_sample_df':   sample_name protocol genome
        0  GSM1558746      GRO   hg38
        1  GSM1480327      PRO   hg38,
                                    '_sample_table':             genome                              organism protocol sample_name
        sample_name                                                                  
        GSM1558746    hg38  {'Homo sapiens': {'genome': 'hg38'}}      GRO  GSM1558746
        GSM1480327    hg38  {'Homo sapiens': {'genome': 'hg38'}}      PRO  GSM1480327,
                                    '_samples': <Recursion on list with id=140711461083656>,
                                    '_samples_touched': True,
                                    '_subsample_df': None,
                                    'description': None,
                                    'name': 'test',
                                    'sst_index': ['sample_name',
                                                  'subsample_name'],
                                    'st_index': 'sample_name'},
                       'genome': 'hg38',
                       'organism': PathExAttMap
        Homo sapiens:
          genome: hg38,
                       'protocol': 'GRO',
                       'sample_name': 'GSM1558746'},
                      {'_attributes': ['sample_name', 'protocol', 'genome'],
                       '_derived_cols_done': [],
                       '_project': {'_config': {'name': 'test',
                                                'output_dir': 'test',
                                                'pep_version': '2.0.0',
                                                'sample_modifiers': {'append': {'organism': {'Homo sapiens': {'genome': 'hg38'}}}},
                                                'sample_table': '/Users/mstolarczyk/code/eido/tests/data/peps/test_sample_table.csv'},
                                    '_config_file': '/Users/mstolarczyk/code/eido/tests/data/peps/test_cfg.yaml',
                                    '_sample_df':   sample_name protocol genome
        0  GSM1558746      GRO   hg38
        1  GSM1480327      PRO   hg38,
                                    '_sample_table':             genome                              organism protocol sample_name
        sample_name                                                                  
        GSM1558746    hg38  {'Homo sapiens': {'genome': 'hg38'}}      GRO  GSM1558746
        GSM1480327    hg38  {'Homo sapiens': {'genome': 'hg38'}}      PRO  GSM1480327,
                                    '_samples': <Recursion on list with id=140711461083656>,
                                    '_samples_touched': True,
                                    '_subsample_df': None,
                                    'description': None,
                                    'name': 'test',
                                    'sst_index': ['sample_name',
                                                  'subsample_name'],
                                    'st_index': 'sample_name'},
                       'genome': 'hg38',
                       'organism': PathExAttMap
        Homo sapiens:
          genome: hg38,
                       'protocol': 'PRO',
                       'sample_name': 'GSM1480327'}],
         '_samples_touched': True,
         '_subsample_df': None,
         'description': None,
         'name': 'test',
         'sst_index': ['sample_name', 'subsample_name'],
         'st_index': 'sample_name'}


## Config validation

Similarily, the config part of the PEP can be validated; the function inputs remain the same


```python
validate_config(project=p, schema="../tests/data/schemas/test_schema.yaml")
```

## Sample validation

To validate a specific `peppy.Sample` object within a PEP, one needs to also specify the `sample_name` argument which can be the `peppy.Sample.name` attribute (`str`) or the ID of the sample (`int`)


```python
validate_sample(
    project=p, schema="../tests/data/schemas/test_schema.yaml", sample_name=0
)
```

## Output details

As depicted above the error raised by the `jsonschema` package is very detailed. That's because the entire validated PEP is printed out for the user reference. Since it can get overwhelming in case of the multi sample PEPs each of the `eido` functions presented above privide a way to limit the output to just the general information indicating the unmet schema requirements


```python
validate_project(
    project=p,
    schema="../tests/data/schemas/test_schema_invalid.yaml",
    exclude_case=True,
)
```


    ---------------------------------------------------------------------------

    ValidationError                           Traceback (most recent call last)

    <ipython-input-10-e51679763445> in <module>
          2     project=p,
          3     schema="../tests/data/schemas/test_schema_invalid.yaml",
    ----> 4     exclude_case=True,
          5 )


    /Library/Frameworks/Python.framework/Versions/3.6/lib/python3.6/site-packages/eido/eido.py in validate_project(project, schema, exclude_case)
        112     for schema_dict in schema_dicts:
        113         project_dict = project.to_dict()
    --> 114         _validate_object(project_dict, _preprocess_schema(schema_dict), exclude_case)
        115         _LOGGER.debug("Project validation successful")
        116 


    /Library/Frameworks/Python.framework/Versions/3.6/lib/python3.6/site-packages/eido/eido.py in _validate_object(object, schema, exclude_case)
         97         if not exclude_case:
         98             raise
    ---> 99         raise jsonschema.exceptions.ValidationError(e.message)
        100 
        101 


    ValidationError: 'invalid' is a required property

