#<img src="img/pephub_logo_big.svg" class="img-header">

<p align="center">
<a href="https://pep.databio.org" alt="PEP compatible"><img src="https://pepkit.github.io/img/PEP-compatible-green.svg"/></a>
<a href="https://github.com/pepkit/pephub" alt="GitHub source code"><img src="https://img.shields.io/badge/source-github-354a75?logo=github"/></a>
</p>



PEPhub is an open-source database, web interface, and API for sharing, retrieving, and validating metadata. PEPhub consists of:

- **Public user interface**: <a href="https://pephub.databio.org/" target="_blank">https://pephub.databio.org/</a>
- **API**: <a href="https://pephub-api.databio.org/api/v1/docs" target="_blank">https://pephub-api.databio.org/api/v1/docs</a>


## Features at-a-glance


- **Validation**. PEPhub validates sample metadata with [eido](../eido/README.md). Users can specify a schema to which the PEP should adhere. All schemas are available on the official website: [https://schema.databio.org/](https://schema.databio.org/). Schemas are particularly useful before running pipelines, as validation provides essential information about PEP compatibility with specific pipelines and highlights any errors in the PEP structure.

- **Semantic search**. PEPhub has semantic search functionality based on cutting-edge semantic machine learning. Information from each PEP is encoded using a sentence transformer and stored in a fast vector database. The PEPhub search interface then provides an extremely fast and powerful semantic search of sample metadata.

- **Authorization**. PEPhub has a robust user authorization system to allow users to submit and edit their own PEPs.  Users authenticate via GitHub, and then may upload, modify, and delete PEPs, and star projects. You can  also set projects as private to restrict access. PEPhub also provides group-level permissions using GitHub organization membership, providing organizational namespaces that correspond to GitHub organizations to make it possible to collaborate on PEPs.

- **Group PEPs with using a PEP of PEPs (POP)**. A PEP of PEPs, or simply a POP, is a specific type of PEP in which each row is itself a PEP. Essentially, a POP is a structure to group PEPs, allowing users to organize projects. This allows PEPs related to a specific topic to be consolidated, streamlining organization and accessibility.

- **Re-processing of GEO metadata**. The public PEPhub instance [geo namespace](https://pephub.databio.org/geo)  holds metadata from nearly 99% of the [Gene Expression Omnibus](https://www.ncbi.nlm.nih.gov/geo/). PEPhub is updated weekly using [GEOfetch](../geofetch/README.md) to produce standardized PEP sample tables, providing a convenient API interface to GEO metadata.

- **PEPHubClient (phc)**. PEPhubClient is a command-line tool and Python API, which allows users to authenticate with PEPhub, download and upload public or private projects. For more information, see the [PEPHubClient documentation](developer/pephubclient/README.md).

## Next steps

Choose your adventure:

<div class="grid cards" markdown>

- :fontawesome-regular-user:  [**User guide**](user/getting-started.md)  
  Teaches you how to use PEPhub to manage, share, and validate your sample metadata.

- :fontawesome-solid-code: [**Developer guide**](developer/setup.md)  
  Teaches you how to contribute to PEPhub, build tools on the PEPhub API, or deploy your own instance.

</div>

