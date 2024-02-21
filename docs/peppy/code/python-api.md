<script>
document.addEventListener('DOMContentLoaded', (event) => {
  document.querySelectorAll('h3 code').forEach((block) => {
    hljs.highlightBlock(block);
  });
});
</script>

<style>
h3 .content { 
    padding-left: 22px;
    text-indent: -15px;
 }
h3 .hljs .content {
    padding-left: 20px;
    margin-left: 0px;
    text-indent: -15px;
    martin-bottom: 0px;
}
h4 .content, table .content, p .content, li .content { margin-left: 30px; }
h4 .content { 
    font-style: italic;
    font-size: 1em;
    margin-bottom: 0px;
}

</style>


# Package `peppy` Documentation

Project configuration, particularly for logging.

Project-scope constants may reside here, but more importantly, some setup here
will provide a logging infrastructure for all of the project's modules.
Individual modules and classes may provide separate configuration on a more
local level, but this will at least provide a foundation.


## <a name="Project"></a> Class `Project`
A class to model a Project (collection of samples and metadata).

#### Parameters:

- `cfg` (`str`):  Project config file (YAML) or sample table (CSV/TSV)with one row per sample to constitute project
- `sample_table_index` (`str | Iterable[str]`):  name of the columns to setthe sample_table index to
- `subsample_table_index` (`str | Iterable[str]`):  name of the columns to setthe subsample_table index to
- `amendments` (`str | Iterable[str]`):  names of the amendments to activate
- `amendments` (`Iterable[str]`):  amendments to use within configuration file
- `defer_samples_creation` (`bool`):  whether the sample creation should be skipped


#### Examples:

```python
    from peppy import Project
    prj = Project(cfg="ngs.yaml")
    samples = prj.samples
```


```python
def __init__(self, cfg: str = None, amendments: Union[str, Iterable[str]] = None, sample_table_index: Union[str, Iterable[str]] = None, subsample_table_index: Union[str, Iterable[str]] = None, defer_samples_creation: bool = False)
```

Initialize self.  See help(type(self)) for accurate signature.



```python
def activate_amendments(self, amendments)
```

Update settings based on amendment-specific values.

This method will update Project attributes, adding new values
associated with the amendments indicated, and in case of collision with
an existing key/attribute the amendments' values will be favored.
#### Parameters:

- `amendments` (`Iterable[str]`):  A string with amendmentnames to be activated


#### Returns:

- `peppy.Project`:  Updated Project instance


#### Raises:

- `TypeError`:  if argument to amendment parameter is null
- `NotImplementedError`:  if this call is made on a project notcreated from a config file




```python
def add_samples(self, samples)
```

Add list of Sample objects
#### Parameters:

- `samples` (`peppy.Sample | Iterable[peppy.Sample]`):  samples to add




```python
def amendments(self)
```

Return currently active list of amendments or None if none was activated
#### Returns:

- `Iterable[str]`:  a list of currently active amendment names




```python
def attr_constants(self)
```

Update each Sample with constants declared by a Project. If Project does not declare constants, no update occurs.



```python
def attr_derive(self, attrs=None)
```

Set derived attributes for all Samples tied to this Project instance



```python
def attr_imply(self)
```

Infer value for additional field(s) from other field(s).

Add columns/fields to the sample based on values in those already-set
that the sample's project defines as indicative of implications for
additional data elements for the sample.



```python
def attr_merge(self)
```

Merge sample subannotations (from subsample table) with sample annotations (from sample_table)



```python
def attr_remove(self)
```

Remove declared attributes from all samples that have them defined



```python
def attr_synonyms(self)
```

Copy attribute values for all samples to a new one



```python
def config(self)
```

Get the config mapping
#### Returns:

- `Mapping`:  config. May be formatted to comply with the mostrecent version specifications




```python
def config_file(self)
```

Get the config file path
#### Returns:

- `str`:  path to the config file




```python
def copy(self)
```

Copy self to a new object.



```python
def create_samples(self, modify: bool = False)
```

Populate Project with Sample objects



```python
def deactivate_amendments(self)
```

Bring the original project settings back.
#### Returns:

- `peppy.Project`:  Updated Project instance


#### Raises:

- `NotImplementedError`:  if this call is made on a project notcreated from a config file




```python
def description(self)
```



```python
def from_dict(pep_dictionary: dict)
```

Init a peppy project instance from a dictionary representation of an already processed PEP.
#### Parameters:

- `pep_dictionary` (`Dict[Any]`):  dict,_samples: list | dict, _subsamples: list[list | dict]}




```python
def from_pandas(samples_df: pandas.core.frame.DataFrame, sub_samples_df: List[pandas.core.frame.DataFrame] = None, config: dict = None)
```

Init a peppy project instance from a pandas Dataframe
#### Parameters:

- `samples_df` (``):  in-memory pandas DataFrame object of samples
- `sub_samples_df` (``):  in-memory list of pandas DataFrame objects of sub-samples
- `config` (``):  dict of yaml file




```python
def from_pep_config(cfg: str = None, amendments: Union[str, Iterable[str]] = None, sample_table_index: Union[str, Iterable[str]] = None, subsample_table_index: Union[str, Iterable[str]] = None, defer_samples_creation: bool = False)
```

Init a peppy project instance from a yaml file
#### Parameters:

- `cfg` (`str`):  Project config file (YAML) or sample table (CSV/TSV)with one row per sample to constitute project
- `sample_table_index` (`str | Iterable[str]`):  name of the columns to setthe sample_table index to
- `subsample_table_index` (`str | Iterable[str]`):  name of the columns to setthe subsample_table index to
- `amendments` (`str | Iterable[str]`):  names of the amendments to activate
- `amendments` (`Iterable[str]`):  amendments to use within configuration file
- `defer_samples_creation` (`bool`):  whether the sample creation should be skipped




```python
def from_sample_yaml(yaml_file: str)
```

Init a peppy project instance from a yaml file
#### Parameters:

- `yaml_file` (`str`):  path to yaml file




```python
def get_description(self)
```

Infer project description from config file.

The provided description has to be of class coercible to string
#### Returns:

- `str`:  inferred name for project.


#### Raises:

- `InvalidConfigFileException`:  if description is not of classcoercible to string




```python
def get_sample(self, sample_name)
```

Get an individual sample object from the project.

Will raise a ValueError if the sample is not found.
In the case of multiple samples with the same name (which is not
typically allowed), a warning is raised and the first sample is returned
#### Parameters:

- `sample_name` (`str`):  The name of a sample to retrieve


#### Returns:

- `peppy.Sample`:  The requested Sample object


#### Raises:

- `ValueError`:  if there's no sample with the specified name defined




```python
def get_samples(self, sample_names)
```

Returns a list of sample objects given a list of sample names
#### Parameters:

- `sample_names` (`list`):  A list of sample names to retrieve


#### Returns:

- `list[peppy.Sample]`:  A list of Sample objects




```python
def infer_name(self)
```

Infer project name from config file path.

First assume the name is the folder in which the config file resides,
unless that folder is named "metadata", in which case the project name
is the parent of that folder.
#### Returns:

- `str`:  inferred name for project.


#### Raises:

- `InvalidConfigFileException`:  if the project lacks both a name anda configuration file (no basis, then, for inference)
- `InvalidConfigFileException`:  if specified Project name is invalid




```python
def is_sample_table_large(self)
```



```python
def list_amendments(self)
```

Return a list of available amendments or None if not declared
#### Returns:

- `Iterable[str]`:  a list of available amendment names




```python
def load_samples(self)
```

Read the sample_table and subsample_tables into dataframes and store in the object root. The values sourced from the project config can be overwritten by the optional arguments.



```python
def modify_samples(self)
```

Perform any sample modifications defined in the config.



```python
def name(self)
```



```python
def parse_config_file(self, cfg_path: str = None, amendments: Iterable[str] = None)
```

Parse provided yaml config file and check required fields exist.
#### Parameters:

- `cfg_path` (`str`):  path to the config file to read and parse
- `amendments` (`Iterable[str]`):  Name of amendments to activate


#### Raises:

- `KeyError`:  if config file lacks required section(s)




```python
def pep_version(self)
```

The declared PEP version string

It is validated to make sure it is a valid PEP version string
#### Returns:

- `str`:  PEP version string


#### Raises:

- `InvalidConfigFileException`:  in case of invalid PEP version




```python
def remove_samples(self, sample_names)
```

Remove Samples from Project
#### Parameters:

- `sample_names` (`Iterable[str]`):  sample names to remove




```python
def sample_name_colname(self)
```

**Deprecated, please use `Project.sample_table_index` instead**

Name of the effective sample name containing column in the sample table.
It is "sample_name" by default, but when it's missing it could be
replaced by the selected sample table index, defined on the
object instantiation stage.
#### Returns:

- `str`:  name of the column that consist of sample identifiers




```python
def sample_table(self)
```

Get sample table. If any sample edits were performed, it will be re-generated
#### Returns:

- `pandas.DataFrame`:  a data frame with current samples attributes




```python
def sample_table_index(self)
```

The effective sample table index.

It is `sample_name` by default, but could be overwritten by the selected sample table index,
defined on the object instantiation stage or in the project configuration file
via `sample_table_index` field.
That's the sample table index selection priority order:
1. Constructor specified
2. Config specified
3. Deafult: `sample_table`
#### Returns:

- `str`:  name of the column that consist of sample identifiers




```python
def samples(self)
```

Generic/base Sample instance for each of this Project's samples.
#### Returns:

- `Iterable[Sample]`:  Sample instance for eachof this Project's samples




```python
def subsample_table(self)
```

Get subsample table
#### Returns:

- `pandas.DataFrame`:  a data frame with subsample attributes




```python
def subsample_table_index(self)
```

The effective subsample table indexes.

It is `[subasample_name, sample_name]` by default,
but could be overwritten by the selected subsample table indexes,
defined on the object instantiation stage or in the project configuration file
via `subsample_table_index` field.
That's the subsample table indexes selection priority order:
1. Constructor specified
2. Config specified
3. Deafult: `[subasample_name, sample_name]`
#### Returns:

- `List[str]`:  names of the columns that consist of sample and subsample identifiers




```python
def to_dict(self, extended: bool = False, orient: Literal['dict', 'list', 'series', 'split', 'tight', 'records', 'index'] = 'dict') -> dict
```

Convert the Project object to a dictionary.
#### Parameters:

- `extended` (`bool`):  whether to produce complete project dict (used to reinit the project)
- `orient` (`Literal`):  orientation of the returned df


#### Returns:

- `dict`:  a dictionary representation of the Project object




## <a name="Sample"></a> Class `Sample`
Class to model Samples based on a pandas Series.

#### Parameters:

- `series` (`Mapping | pandas.core.series.Series`):  Sample's data.


```python
def __init__(self, series, prj=None)
```

Initialize self.  See help(type(self)) for accurate signature.



```python
def attributes(self)
```



```python
def copy(self)
```

Copy self to a new object.



```python
def derive_attribute(self, data_sources, attr_name)
```

Uses the template path provided in the project config section "data_sources" to piece together an actual path by substituting variables (encoded by "{variable}"") with sample attributes.
#### Parameters:

- `data_sources` (`Mapping`):  mapping from key name (as a value ina cell of a tabular data structure) to, e.g., filepath
- `attr_name` (`str`):  Name of sample attribute(equivalently, sample sheet column) specifying a derived column.


#### Returns:

- `str`:  regex expansion of data source specified in configuration,with variable substitutions made


#### Raises:

- `ValueError`:  if argument to data_sources parameter is null/empty




```python
def get_sheet_dict(self)
```

Create a K-V pairs for items originally passed in via the sample sheet. This is useful for summarizing; it provides a representation of the sample that excludes things like config files and derived entries.
#### Returns:

- `OrderedDict`:  mapping from name to value for data elementsoriginally provided via the sample sheet (i.e., the a map-like representation of the instance, excluding derived items)




```python
def project(self)
```

Get the project mapping
#### Returns:

- `peppy.Project`:  project object the sample was created from




```python
def to_dict(self, add_prj_ref=False)
```

Serializes itself as dict object.
#### Parameters:

- `add_prj_ref` (`bool`):  whether the project reference bound do theSample object should be included in the YAML representation


#### Returns:

- `dict`:  dict representation of this Sample




```python
def to_yaml(self, path, add_prj_ref=False)
```

Serializes itself in YAML format.
#### Parameters:

- `path` (`str`):  A file path to write yaml to; provide this orthe subs_folder_path
- `add_prj_ref` (`bool`):  whether the project reference bound do theSample object should be included in the YAML representation




## <a name="PeppyError"></a> Class `PeppyError`
Base error type for peppy custom errors.


```python
def __init__(self, msg)
```

Initialize self.  See help(type(self)) for accurate signature.






*Version Information: `peppy` v0.40.1, generated by `lucidoc` v0.4.4*