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


# Package `geofetch` Documentation

 Package-level data 
## <a name="Finder"></a> Class `Finder`
Class for finding GSE accessions in special period of time. Additionally, user can add specific filters for the search, while initialization of the class


```python
def __init__(self, filters: str = None, retmax: int = 10000000)
```


#### Parameters:

- `filters` (``):  filters that have to be added to the query.Filter Patterns can be found here: https://www.ncbi.nlm.nih.gov/books/NBK3837/#EntrezHelp.Using_the_Advanced_Search_Pag
- `retmax` (``):  maximum number of retrieved accessions.




```python
def find_differences(old_list: list, new_list: list) -> list
```

Compare 2 lists and search for elements that are not in old list
#### Parameters:

- `old_list` (``):  old list of elements
- `new_list` (``):  new list of elements


#### Returns:

- ``:  list of elements that are not in old list but are in new_list




```python
def generate_file(self, file_path: str, gse_list: list = None)
```

Save the list of GSE accessions stored in this Finder object to a given file
#### Parameters:

- `file_path` (``):  root to the file where gse accessions have to be saved
- `gse_list` (``):  list of gse accessions


#### Returns:

- ``:  NoReturn




```python
def get_gse_all(self) -> list
```

Get list of all gse accession available in GEO
#### Returns:

- ``:  list of gse accession




```python
def get_gse_by_date(self, start_date: str, end_date: str = None) -> list
```

Search gse accessions by providing start date and end date. By default, the last date is today.
#### Parameters:

- `start_date` (``):  'YYYY/MM/DD']
- `end_date` (``):  'YYYY/MM/DD']


#### Returns:

- ``:  list of gse accessions




```python
def get_gse_by_day_count(self, n_days: int = 1) -> list
```

Get list of gse accessions that were uploaded or updated in last X days
#### Parameters:

- `n_days` (``):  number of days from now [e.g. 5]


#### Returns:

- ``:  list of gse accession




```python
def get_gse_id_by_query(self, url: str) -> list
```

Run esearch (ncbi search tool) by specifying URL and retrieve gse list result
#### Parameters:

- `url` (``):  url of the query


#### Returns:

- ``:  list of gse ids




```python
def get_gse_last_3_month(self) -> list
```

Get list of gse accession that were uploaded or updated in last 3 month
#### Returns:

- ``:  list of gse accession




```python
def get_gse_last_week(self) -> list
```

Get list of gse accession that were uploaded or updated in last week
#### Returns:

- ``:  list of gse accession




```python
def uid_to_gse(uid: str) -> str
```

UID to GES accession converter
#### Parameters:

- `uid` (``):  uid string (Unique Identifier Number in GEO)


#### Returns:

- ``:  GSE id string




## <a name="Geofetcher"></a> Class `Geofetcher`
Class to download or get projects, metadata, data from GEO and SRA


```python
def __init__(self, name: str = '', metadata_root: str = '', metadata_folder: str = '', just_metadata: bool = False, refresh_metadata: bool = False, config_template: str = None, pipeline_samples: str = None, pipeline_project: str = None, skip: int = 0, acc_anno: bool = False, use_key_subset: bool = False, processed: bool = False, data_source: str = 'samples', filter: str = None, filter_size: str = None, geo_folder: str = '.', split_experiments: bool = False, bam_folder: str = '', fq_folder: str = '', sra_folder: str = '', bam_conversion: bool = False, picard_path: str = '', input: str = None, const_limit_project: int = 50, const_limit_discard: int = 1000, attr_limit_truncate: int = 500, max_soft_size: str = '1GB', discard_soft: bool = False, add_dotfile: bool = False, disable_progressbar: bool = False, add_convert_modifier: bool = False, opts=None, max_prefetch_size=None, **kwargs)
```

Constructor
#### Parameters:

- `input` (``):  GSEnumber or path to the input file
- `name` (``):  Specify a project name. Defaults to GSE number or name of accessions file name
- `metadata_root` (``):   Specify a parent folder location to store metadata.The project name will be added as a subfolder [Default: $SRAMETA:]
- `metadata_folder` (``):  Specify an absolute folder location to store metadata. No subfolder will be added.Overrides value of --metadata-root [Default: Not used (--metadata-root is used by default)]
- `just_metadata` (``):  If set, don't actually run downloads, just create metadata
- `refresh_metadata` (``):  If set, re-download metadata even if it exists.
- `config_template` (``):  Project config yaml file template.
- `pipeline_samples` (``):  Specify one or more filepaths to SAMPLES pipeline interface yaml files.These will be added to the project config file to make it immediately compatible with looper. [Default: null]
- `pipeline_project` (``):  Specify one or more filepaths to PROJECT pipeline interface yaml files.These will be added to the project config file to make it immediately compatible with looper. [Default: null]
- `acc_anno` (``):   Produce annotation sheets for each accession.Project combined PEP for the whole project won't be produced.
- `discard_soft` (``):  Create project without downloading soft files on the disc
- `add_dotfile` (``):  Add .pep.yaml file that points .yaml PEP file
- `disable_progressbar` (``):  Set true to disable progressbar




```python
def fetch_all(self, input: str, name: str = None) -> Union[NoReturn, peppy.project.Project]
```

Main function driver/workflow Function that search, filters, downloads and save data and metadata from  GEO and SRA
#### Parameters:

- `input` (``):  GSE or input file with gse's
- `name` (``):  Name of the project


#### Returns:

- ``:  NoReturn or peppy Project




```python
def fetch_processed_one(self, gse_file_content: list, gsm_file_content: list, gsm_filter_list: dict) -> Tuple
```

Fetche one processed GSE project and return its metadata
#### Parameters:

- `gsm_file_content` (``):  gse soft file content
- `gse_file_content` (``):  gsm soft file content
- `gsm_filter_list` (``):  list of gsm that have to be downloaded


#### Returns:

- ``:  Tuple of project list of gsm samples and gse samples




```python
def get_projects(self, input: str, just_metadata: bool = True, discard_soft: bool = True) -> dict
```

Function for fetching projects from GEO|SRA and receiving peppy project
#### Parameters:

- `input` (``):  GSE number, or path to file of GSE numbers
- `just_metadata` (``):  process only metadata
- `discard_soft` (``):   clean run, without downloading soft files


#### Returns:

- ``:  peppy project or list of project, if acc_anno is set.







*Version Information: `geofetch` v0.12.5, generated by `lucidoc` v0.4.4*