#<img src="img/pephub_logo_big.svg" class="img-header">

<p align="center">
<a href="https://pep.databio.org" alt="PEP compatible"><img src="https://pepkit.github.io/img/PEP-compatible-green.svg"/></a>
<a href="https://github.com/pepkit/eido" alt="GitHub source code"><img src="https://img.shields.io/badge/source-github-354a75?logo=github"/></a>
</p>

PEPhub is a database, web interface, and API for sharing, retrieving, and validating sample metadata. PEPhub takes advantage of the Portable Encapsulated Projects (PEP) biological metadata standard to store, edit, and access your PEPs in one place. You can view the deployed public instance at <https://pephub.databio.org>.

---

**Deployed public instance**: <a href="https://pephub.databio.org/" target="_blank">https://pephub.databio.org/</a>

**API**: <a href="https://pephub-api.databio.org/api/v1/docs" target="_blank">https://pephub-api.databio.org/api/v1/docs</a>

**Documentation**: <a href="https://pep.databio.org/pephub" target="_blank">https://pep.databio.org/pephub</a>

**Source Code**: <a href="https://github.com/pepkit/pephub" target="_blank">https://github.com/pepkit/pephub</a>

----
## Overview

### What is PEP?
Portable Encapsulated Projects, commonly known as PEP, represents a collaborative initiative aimed at enhancing the reusability of sample metadata. It is simply **yaml** + **csv** files (or just csv) that contains samples and project metadata. The CSV file, known as the sample table, contains details about individual samples, while the YAML configuration file provides metadata related to projects, amendments, and other sample modifiers.
PEPs serve as a standardized format for running workflows using tools such as [Snakemake](https://snakemake.readthedocs.io/en/stable/), [Common Workflow Language](https://www.commonwl.org/), [Looper](http://pep.databio.org/looper), and other workflow systems.
For further details about PEP and its usage, please visit: [http://pep.databio.org/](http://pep.databio.org/)

### Validation

PEPhub offers automated project validation through [EIDO](http://pep.databio.org/eido). Users can specify a schema to which the PEP should adhere. All schemas are available on the official website: [https://schema.databio.org/](https://schema.databio.org/). Schemas are particularly useful before running pipelines, as validation provides essential information about PEP compatibility with specific pipelines and highlights any errors in the PEP structure.

### Search
PEPhub has semantic search functionality. The vector database is populated with important information extracted from the PEP config file. Through the search capability, users can efficiently locate projects, POPs, and Namespaces related to the string they provide.
More information can be found in the [semantic-search](https://pep.databio.org/pephub/semantic-search/).


### Authorization
One of the key features of PEPhub is the empowerment of users to submit and edit their own PEPs. To facilitate this, we have implemented a robust user authorization system. Users are required to authenticate via GitHub to access PEPhub.
Once authorized, users gain access to a range of features, including the ability to upload, modify, and delete PEPs, and star projects. Authorized users can also designate projects as private, ensuring that only they have visibility, with restricted access for others.
Moreover, users have the capability to modify projects within organizational namespaces, which correspond to the GitHub organizations they belong to. This feature facilitates collaborative efforts within organizational groups.

### PEP of PEPs (POP)
The PEP of PEPs, often referred to as a Project of Projects or simply POP, is a specialized project that encompasses multiple projects as samples. Essentially, a POP can be thought of as a grouping of PEPs, allowing users to organize projects for various purposes. This approach offers several advantages: all PEPs related to a specific topic can be consolidated in one central location, streamlining organization and accessibility.


### GEO data
PEPhub has a namespace called GEO. This namespace contains projects from [Gene Expression Omnibus](https://www.ncbi.nlm.nih.gov/geo/) that are downloaded and processed using [GEOfetch](https://geofetch.databio.org/en/latest/). GEOfetch produces a standardized PEP sample table with GSM (GEO sample) and a YAML config that has metadata from GSE (GEO project). Nearly 99% of projects are downloaded to PEPhub. Users can utilize the namespace search to find projects by accession ID and description.
GEO namespace link: [https://pephub.databio.org/geo](https://pephub.databio.org/geo).
Moreover, users can download all project as `tar file` from the GEO namespace using the link available on the geo namespace page.
PEPhub doesn't store actual files in the database. Because of this, if you want to download files, there are two options:

 - Use links to the files that are stored in the project sample table.
 - Use geofetch on a local machine to download these files.
Example: `geofetch -i GSE95654 --processed`, where `--processed` indicates that you want to download processed data, not SRA. More information about PEP can be found on the official website [GEOfetch](https://geofetch.databio.org/en/latest/).


## PEPHubClient (phc)

PEPhub provides an additional command-line tool and Python API, connecting Python to the PEPhub. The dedicated Python package for this integration is called PEPHubClient, and it is compatible with Linux, Windows, and Mac systems.

Key features of PEPHubClient include:

- **Authorization**: Users can log in to PEPhub using PEPHubClient, enabling the loading of private projects and the ability to upload projects to PEPhub.
- **Load and Download**: PEPHubClient facilitates the loading and downloading of PEPs directly from PEPhub.
- **Push**: Users can push PEPs from their local environment to PEPhub.

More information is available in the pephubclient docs: [PEPHubClient](https://pep.databio.org/pephub/pephubclient).