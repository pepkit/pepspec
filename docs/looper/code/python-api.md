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


# Package `looper` Documentation

Project configuration, particularly for logging.

Project-scope constants may reside here, but more importantly, some setup here
will provide a logging infrastructure for all of the project's modules.
Individual modules and classes may provide separate configuration on a more
local level, but this will at least provide a foundation.


## <a name="Project"></a> Class `Project`
Looper-specific Project.

#### Parameters:

- `cfg` (`str`):  path to configuration file with data fromwhich Project is to be built
- `amendments` (`Iterable[str]`):  name indicating amendment to use, optional
- `divcfg_path` (`str`):  path to an environment configuration YAML filespecifying compute settings.
- `permissive` (`bool`):  Whether a error should be thrown ifa sample input file(s) do not exist or cannot be open.
- `compute_env_file` (`str`):  Environment configuration YAML file specifyingcompute settings.


```python
def __init__(self, cfg=None, amendments=None, divcfg_path=None, runp=False, **kwargs)
```

Initialize self.  See help(type(self)) for accurate signature.



```python
def amendments(self)
```

Return currently active list of amendments or None if none was activated
#### Returns:

- `Iterable[str]`:  a list of currently active amendment names




```python
def build_submission_bundles(self, protocol, priority=True)
```

Create pipelines to submit for each sample of a particular protocol.

With the argument (flag) to the priority parameter, there's control
over whether to submit pipeline(s) from only one of the project's
known pipeline locations with a match for the protocol, or whether to
submit pipelines created from all locations with a match for the
protocol.
#### Parameters:

- `protocol` (`str`):  name of the protocol/library for which tocreate pipeline(s)
- `priority` (`bool`):  to only submit pipeline(s) from the first of thepipelines location(s) (indicated in the project config file) that has a match for the given protocol; optional, default True


#### Returns:

- `Iterable[(PipelineInterface, type, str, str)]`: 


#### Raises:

- `AssertionError`:  if there's a failure in the attempt topartition an interface's pipeline scripts into disjoint subsets of those already mapped and those not yet mapped




```python
def cli_pifaces(self)
```

Collection of pipeline interface sources specified in object constructor
#### Returns:

- `list[str]`:  collection of pipeline interface sources




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
def description(self)
```



```python
def from_dict(cls, pep_dictionary: dict)
```

Init a peppy project instance from a dictionary representation of an already processed PEP.
#### Parameters:

- `pep_dictionary` (`Dict[Any]`):  dict,_samples: list | dict, _subsamples: list[list | dict]}




```python
def from_pandas(cls, samples_df: pandas.core.frame.DataFrame, sub_samples_df: List[pandas.core.frame.DataFrame]=None, config: dict=None)
```

Init a peppy project instance from a pandas Dataframe
#### Parameters:

- `samples_df` (``):  in-memory pandas DataFrame object of samples
- `sub_samples_df` (``):  in-memory list of pandas DataFrame objects of sub-samples
- `config` (``):  dict of yaml file




```python
def from_pep_config(cls, cfg: str=None, amendments: Union[str, Iterable[str]]=None, sample_table_index: Union[str, Iterable[str]]=None, subsample_table_index: Union[str, Iterable[str]]=None, defer_samples_creation: bool=False)
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
def from_sample_yaml(cls, yaml_file: str)
```

Init a peppy project instance from a yaml file
#### Parameters:

- `yaml_file` (`str`):  path to yaml file




```python
def get_pipestat_managers(self, sample_name=None, project_level=False)
```

Get a collection of pipestat managers for the selected sample or project.

The number of pipestat managers corresponds to the number of unique
output schemas in the pipeline interfaces specified by the sample or project.
#### Parameters:

- `sample_name` (`str`):  sample name to get pipestat managers for
- `project_level` (`bool`):  whether the project PipestatManagersshould be returned


#### Returns:

- `dict[str, pipestat.PipestatManager]`:  a mapping of pipestatmanagers by pipeline interface name




```python
def get_sample_piface(self, sample_name)
```

Get a list of pipeline interfaces associated with the specified sample.

Note that only valid pipeline interfaces will show up in the
result (ones that exist on disk/remotely and validate successfully
against the schema)
#### Parameters:

- `sample_name` (`str`):  name of the sample to retrieve list ofpipeline interfaces for


#### Returns:

- `list[looper.PipelineInterface]`:  collection of validpipeline interfaces associated with selected sample




```python
def get_schemas(pifaces, schema_key='input_schema')
```

Get the list of unique schema paths for a list of pipeline interfaces
#### Parameters:

- `pifaces` (`str | Iterable[str]`):  pipeline interfaces to searchschemas for
- `schema_key` (`str`):  where to look for schemas in the piface


#### Returns:

- `Iterable[str]`:  unique list of schema file paths




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
def make_project_dirs(self)
```

Create project directory structure if it doesn't exist.



```python
def name(self)
```



```python
def output_dir(self)
```

Output directory for the project, specified in object constructor
#### Returns:

- `str`:  path to the output directory




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
def piface_key(self)
```

Name of the pipeline interface attribute for this project
#### Returns:

- `str`:  name of the pipeline interface attribute




```python
def populate_pipeline_outputs(self)
```

Populate project and sample output attributes based on output schemas that pipeline interfaces point to.



```python
def results_folder(self)
```

Path to the results folder for the project
#### Returns:

- `str`:  path to the results folder in the output folder




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
def selected_compute_package(self)
```

Compute package name specified in object constructor
#### Returns:

- `str`:  compute package name




```python
def set_sample_piface(self, sample_piface: Union[List[str], str]) -> NoReturn
```

Add sample pipeline interfaces variable to object
#### Parameters:

- `sample_piface` (`list | str`):  sample pipeline interface




```python
def submission_folder(self)
```

Path to the submission folder for the project
#### Returns:

- `str`:  path to the submission in the output folder




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




## <a name="PipelineInterface"></a> Class `PipelineInterface`
This class parses, holds, and returns information for a yaml file that specifies how to interact with each individual pipeline. This includes both resources to request for cluster job submission, as well as arguments to be passed from the sample annotation metadata to the pipeline

#### Parameters:

- `config` (`str | Mapping`):  path to file from which to parseconfiguration data, or pre-parsed configuration data.
- `pipeline_type` (`str`):  type of the pipeline,must be either 'sample' or 'project'.


```python
def __init__(self, config, pipeline_type=None)
```

Object constructor
#### Parameters:

- `entries` (`Iterable[(str, object)] | Mapping[str, object]`):  YAML collectionof key-value pairs.
- `filepath` (`str`):  Path to the YAML config file.
- `yamldata` (`str`):  YAML-formatted string
- `locked` (`bool`):  Whether to initialize as locked (providing write capability)
- `wait_max` (`int`):  how long to wait for creating an object when the filethat data will be read from is locked
- `strict_ro_locks` (`bool`):  By default, we allow RO filesystems that can't be locked.Turn on strict_ro_locks to error if locks cannot be enforced on readonly filesystems.
- `skip_read_lock` (`bool`):  whether the file should not be locked for readingwhen object is created in read only mode
- `schema_source` (`str`):  path or a URL to a jsonschema in YAML format to usefor optional config validation. If this argument is provided the object is always validated at least once, at the object creation stage.
- `validate_on_write` (`bool`):  a boolean indicating whether the object should bevalidated every time the `write` method is executed, which is a way of preventing invalid config writing
- `create_file` (`str`):  Create an empty file at filepath upon data load.




```python
def choose_resource_package(self, namespaces, file_size)
```

Select resource bundle for given input file size to given pipeline.
#### Parameters:

- `file_size` (`float`):  Size of input data (in gigabytes).
- `namespaces` (`Mapping[Mapping[str]]`):  namespaced variables to passas a context for fluid attributes command rendering


#### Returns:

- `MutableMapping`:  resource bundle appropriate for given pipeline,for given input file size


#### Raises:

- `ValueError`:  if indicated file size is negative, or if thefile size value specified for any resource package is negative
- `InvalidResourceSpecificationException`:  if no defaultresource package specification is provided




```python
def copy(self)
```

Copy self to a new object.



```python
def exp(self)
```

Returns a copy of the object's data elements with env vars and user vars expanded. Use it like: object.exp["item"]



```python
def get_pipeline_schemas(self, schema_key='input_schema')
```

Get path to the pipeline schema.
#### Parameters:

- `schema_key` (`str`):  where to look for schemas in the pipeline iface


#### Returns:

- `str`:  absolute path to the pipeline schema file




```python
def pipeline_name(self)
```



```python
def rebase(self, *args, **kwargs)
```



```python
def render_var_templates(self, namespaces)
```

Render path templates under 'var_templates' in this pipeline interface.
#### Parameters:

- `namespaces` (`dict`):  namespaces to use for rendering




```python
def reset(self, *args, **kwargs)
```



```python
def settings(self)
```



```python
def write(self, *args, **kwargs)
```



## <a name="SubmissionConductor"></a> Class `SubmissionConductor`
Collects and then submits pipeline jobs.

This class holds a 'pool' of commands to submit as a single cluster job.
Eager to submit a job, each instance's collection of commands expands until
it reaches the 'pool' has been filled, and it's therefore time to submit the
job. The pool fills as soon as a fill criteria has been reached, which can
be either total input file size or the number of individual commands.


```python
def __init__(self, pipeline_interface, prj, delay=0, extra_args=None, extra_args_override=None, ignore_flags=False, compute_variables=None, max_cmds=None, max_size=None, automatic=True, collate=False)
```

Create a job submission manager.

The most critical inputs are the pipeline interface and the pipeline
key, which together determine which provide critical pipeline
information like resource allocation packages and which pipeline will
be overseen by this instance, respectively.
#### Parameters:

- `pipeline_interface` (`PipelineInterface`):  Collection of importantdata for one or more pipelines, like resource allocation packages and option/argument specifications
- `prj` (``):  Project with which each sample being considered isassociated (what generated each sample)
- `delay` (`float`):  Time (in seconds) to wait before submitting a jobonce it's ready
- `extra_args` (`str`):  string to pass to each job generated,for example additional pipeline arguments
- `extra_args_override` (`str`):  string to pass to each job generated,for example additional pipeline arguments. This deactivates the 'extra' functionality that appends strings defined in Sample.command_extra and Project.looper.command_extra to the command template.
- `ignore_flags` (`bool`):  Whether to ignore flag files present inthe sample folder for each sample considered for submission
- `compute_variables` (`dict[str]`):  A dict with variables that will be madeavailable to the compute package. For example, this should include the name of the cluster partition to which job or jobs will be submitted
- `max_cmds` (`int | NoneType`):  Upper bound on number of commands toinclude in a single job script.
- `max_size` (`int | float | NoneType`):  Upper bound on total filesize of inputs used by the commands lumped into single job script.
- `automatic` (`bool`):  Whether the submission should be automatic oncethe pool reaches capacity.
- `collate` (`bool`):  Whether a collate job is to be submitted (runs onthe project level, rather that on the sample level)




```python
def add_sample(self, sample, rerun=False)
```

Add a sample for submission to this conductor.
#### Parameters:

- `sample` (`peppy.Sample`):  sample to be included with this conductor'scurrently growing collection of command submissions
- `rerun` (`bool`):  whether the given sample is being rerun rather thanrun for the first time


#### Returns:

- `bool`:  Indication of whether the given sample was added tothe current 'pool.'


#### Raises:

- `TypeError`:  If sample subtype is provided but does not extendthe base Sample class, raise a TypeError.




```python
def check_executable_path(self, pl_iface)
```

Determines if supplied pipelines are callable. Raises error and exits Looper if not callable
#### Parameters:

- `pl_iface` (`dict`):  pipeline interface that stores paths to executables


#### Returns:

- `bool`:  True if path is callable.




```python
def failed_samples(self)
```



```python
def is_project_submittable(self, force=False)
```

Check whether the current project has been already submitted
#### Parameters:

- `frorce` (`bool`):  whether to force the project submission (ignore status/flags)




```python
def num_cmd_submissions(self)
```

Return the number of commands that this conductor has submitted.
#### Returns:

- `int`:  Number of commands submitted so far.




```python
def num_job_submissions(self)
```

Return the number of jobs that this conductor has submitted.
#### Returns:

- `int`:  Number of jobs submitted so far.




```python
def submit(self, force=False)
```

Submit one or more commands as a job.

This call will submit the commands corresponding to the current pool
of samples if and only if the argument to 'force' evaluates to a
true value, or the pool of samples is full.
#### Parameters:

- `force` (`bool`):  Whether submission should be done/simulated evenif this conductor's pool isn't full.


#### Returns:

- `bool`:  Whether a job was submitted (or would've been ifnot for dry run)




```python
def write_script(self, pool, size)
```

Create the script for job submission.
#### Parameters:

- `pool` (`Iterable[peppy.Sample]`):  collection of sample instances
- `size` (`float`):  cumulative size of the given pool


#### Returns:

- `str`:  Path to the job submission script created.




## <a name="ComputingConfiguration"></a> Class `ComputingConfiguration`
Represents computing configuration objects.

The ComputingConfiguration class provides a computing configuration object
that is an *in memory* representation of a `divvy` computing configuration
file. This object has various functions to allow a user to activate, modify,
and retrieve computing configuration files, and use these values to populate
job submission script templates.

#### Parameters:

- `entries` (`str | Iterable[(str, object)] | Mapping[str, object]`):  configCollection of key-value pairs.
- `filepath` (`str`):  YAML file specifying computing package data. (the`DIVCFG` file)


```python
def __init__(self, entries=None, filepath=None)
```

Object constructor
#### Parameters:

- `entries` (`Iterable[(str, object)] | Mapping[str, object]`):  YAML collectionof key-value pairs.
- `filepath` (`str`):  Path to the YAML config file.
- `yamldata` (`str`):  YAML-formatted string
- `locked` (`bool`):  Whether to initialize as locked (providing write capability)
- `wait_max` (`int`):  how long to wait for creating an object when the filethat data will be read from is locked
- `strict_ro_locks` (`bool`):  By default, we allow RO filesystems that can't be locked.Turn on strict_ro_locks to error if locks cannot be enforced on readonly filesystems.
- `skip_read_lock` (`bool`):  whether the file should not be locked for readingwhen object is created in read only mode
- `schema_source` (`str`):  path or a URL to a jsonschema in YAML format to usefor optional config validation. If this argument is provided the object is always validated at least once, at the object creation stage.
- `validate_on_write` (`bool`):  a boolean indicating whether the object should bevalidated every time the `write` method is executed, which is a way of preventing invalid config writing
- `create_file` (`str`):  Create an empty file at filepath upon data load.




```python
def activate_package(self, package_name)
```

Activates a compute package.

This copies the computing attributes from the configuration file into
the `compute` attribute, where the class stores current compute
settings.
#### Parameters:

- `package_name` (`str`):  name for non-resource compute bundle,the name of a subsection in an environment configuration file


#### Returns:

- `bool`:  success flag for attempt to establish compute settings




```python
def clean_start(self, package_name)
```

Clear current active settings and then activate the given package.
#### Parameters:

- `package_name` (`str`):  name of the resource package to activate


#### Returns:

- `bool`:  success flag




```python
def compute_env_var(self)
```

Environment variable through which to access compute settings.
#### Returns:

- `list[str]`:  names of candidate environment variables, for whichvalue may be path to compute settings file; first found is used.




```python
def default_config_file(self)
```

Path to default compute environment settings file.
#### Returns:

- `str`:  Path to default compute settings file




```python
def exp(self)
```

Returns a copy of the object's data elements with env vars and user vars expanded. Use it like: object.exp["item"]



```python
def get_active_package(self)
```

Returns settings for the currently active compute package
#### Returns:

- `yacman.YacAttMap`:  data defining the active compute package




```python
def get_adapters(self)
```

Get current adapters, if defined.

Adapters are sourced from the 'adapters' section in the root of the
divvy configuration file and updated with an active compute
package-specific set of adapters, if any defined in 'adapters' section
under currently active compute package.
#### Returns:

- `yacman.YAMLConfigManager`:  current adapters mapping




```python
def list_compute_packages(self)
```

Returns a list of available compute packages.
#### Returns:

- `set[str]`:  names of available compute packages




```python
def rebase(self, *args, **kwargs)
```



```python
def reset(self, *args, **kwargs)
```



```python
def reset_active_settings(self)
```

Clear out current compute settings.
#### Returns:

- `bool`:  success flag




```python
def settings(self)
```



```python
def submit(self, output_path, extra_vars=None)
```



```python
def template(self)
```

Get the currently active submission template.
#### Returns:

- `str`:  submission script content template for current state




```python
def templates_folder(self)
```

Path to folder with default submission templates.
#### Returns:

- `str`:  path to folder with default submission templates




```python
def update_packages(self, config_file)
```

Parse data from divvy configuration file.

Given a divvy configuration file, this function will update (not
overwrite) existing compute packages with existing values. It does not
affect any currently active settings.
#### Parameters:

- `config_file` (`str`):  path to file with new divvy configuration data




```python
def write(self, filename=None)
```



```python
def write_script(self, output_path, extra_vars=None)
```

Given currently active settings, populate the active template to write a submission script. Additionally use the current adapters to adjust the select of the provided variables
#### Parameters:

- `output_path` (`str`):  Path to file to write as submission script
- `extra_vars` (`Iterable[Mapping]`):  A list of Dict objects withkey-value pairs with which to populate template fields. These will override any values in the currently active compute package.


#### Returns:

- `str`:  Path to the submission script file




```python
def select_divvy_config(filepath)
```

Selects the divvy config file path to load.

This uses a priority ordering to first choose a config file path if
it's given, but if not, then look in a priority list of environment
variables and choose the first available file path to return. If none of
these options succeed, the default config path will be returned.
#### Parameters:

- `filepath` (`str | NoneType`):  direct file path specification


#### Returns:

- `str`:  path to the config file to read







*Version Information: `looper` v1.5.2-dev, generated by `lucidoc` v0.4.3*