## Overview
## What is PEP?


### Validation

PEPhub valides sample metadata with [eido](/eido). Users can specify a schema to which the PEP should adhere. All schemas are available on the official website: [https://schema.databio.org/](https://schema.databio.org/). Schemas are particularly useful before running pipelines, as validation provides essential information about PEP compatibility with specific pipelines and highlights any errors in the PEP structure.

### Search
PEPhub has semantic search functionality. The vector database is populated with important information extracted from the PEP config file. Through the search capability, users can efficiently locate projects, POPs, and Namespaces related to the string they provide.
More information can be found in [PEPhub semantic search docs](semantic-search.md).


### Authorization

A key feature of PEPhub is that users can submit and edit their own PEPs. To facilitate this, we have implemented a robust user authorization system. Users authenticate via GitHub, which provides  access to a range of features, including the ability to upload, modify, and delete PEPs, and star projects. Authorized users can also designate projects as private, ensuring that only they have visibility, with restricted access for others.
Moreover, users have the capability to modify projects within organizational namespaces, which correspond to the GitHub organizations they belong to. This feature facilitates collaborative efforts within organizational groups.

### PEP of PEPs (POP)

The PEP of PEPs, often referred to as a Project of Projects or simply POP, is a specific type of PEP in which each sample is itself a PEP. Essentially, a POP can be thought of as a grouping of PEPs, allowing users to organize projects for various purposes. This approach offers several advantages: all PEPs related to a specific topic can be consolidated in one central location, streamlining organization and accessibility.

### GEO data

PEPhub has a namespace called GEO. This namespace contains projects from [Gene Expression Omnibus](https://www.ncbi.nlm.nih.gov/geo/) that are downloaded and processed using [GEOfetch](/geofetch). GEOfetch produces a standardized PEP sample table with GSM (GEO sample) and a YAML config that has metadata from GSE (GEO project). Nearly 99% of projects are downloaded to PEPhub. Users can utilize the namespace search to find projects by accession ID and description.
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
