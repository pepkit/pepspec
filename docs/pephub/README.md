#<img src="img/pephub_logo_big.svg" class="img-header">

<p align="center">
<a href="https://pep.databio.org" alt="PEP compatible"><img src="https://pepkit.github.io/img/PEP-compatible-green.svg"/></a>
<a href="https://github.com/pepkit/pephub" alt="GitHub source code"><img src="https://img.shields.io/badge/source-github-354a75?logo=github"/></a>
</p>



PEPhub is a database, web interface, and API for sharing, retrieving, and validating sample metadata. PEPhub takes advantage of the Portable Encapsulated Projects (PEP) biological metadata standard to store, edit, and access your PEPs in one place. PEPhub consists of two components:

- **Deployed public user interface**: <a href="https://pephub.databio.org/" target="_blank">https://pephub.databio.org/</a>
- **API**: <a href="https://pephub-api.databio.org/api/v1/docs" target="_blank">https://pephub-api.databio.org/api/v1/docs</a>

----


## How to use this documentation
We have two types of documentation for PEPhub: **user** and **developer** documentation. The user documentation is intended for users who want to learn how to use PEPhub. The developer documentation is intended for developers who want to contribute to the PEPhub codebase or build on top of the PEPhub API and deploy their own instance.

### Users
- **[Getting started](user/getting-started.md)**: Learn how to create an account, log in, and upload your first PEP.
- **[Creating an account and logging in](user/accounts.md)**: Learn how to create an account and log in to PEPhub.
- **[Uploading your first PEP](user/uploading.md)**: Learn how to upload your first PEP to PEPhub.
- **[Editing a PEP](user/editing.md)**: Learn how to edit a PEP in PEPhub.
- **[Sharing your PEP](user/sharing.md)**: Learn how to share your PEP via the PEPhub API.
- **[Use a PEP in an existing pipeline](user/pipelines.md)**: Learn how to incorporate PEPhub into an existing pipeline.
- **[Validating PEPs](user/validation.md)**: Learn how to validate PEPs in PEPhub.
- **[Version control](user/version-control.md)**: Learn how to use version control in PEPhub.
- **[Semantic search](user/semantic-search.md)**: Learn how to use the semantic search functionality in PEPhub.
- **[Building POPs](user/pops.md)**: Learn how to build a PEP of PEPs (POP) in PEPhub.

### Developers
- **[Setup](developer/organization.md)**: Learn how to set up the PEPhub development environment.
- **[Development](developer/api.md)**: Learn about developing the PEPhub API and user interface.
- **[Deployment](developer/deployment.md)**: Learn how to deploy PEPhub.
- **[Authentication](developer/authentication.md)**: Learn about the authentication methods used in PEPhub.
- **[Device authentication](developer/authentication-device.md)**: Learn about the device authentication method used in PEPhub.
- **[Semantic search](developer/semantic-search.md)**: Learn about the semantic search functionality in PEPhub.
- **[Server settings](developer/server-settings.md)**: Learn about the server settings in PEPhub.
- **[PEPembed](developer/pepembed/README.md)**: Learn about `pepembed`, the PEP embedding tool for PEPhub.
- **[pepdbagent](developer/pepdbagent/README.md)**: Learn about `pepdbagent`, the database driver for PEPhub.
- **[PEPhubClient](developer/pephubclient/README.md)**: Learn about `PEPhubClient`, the command-line tool and Python API for PEPhub.
- **[geopephub](developer/geopephub/README.md)**: Learn about PEPhubs GEO namespace for the gene expression omnibus.