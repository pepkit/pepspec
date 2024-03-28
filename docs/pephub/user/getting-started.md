# Getting started with PEPhub
*Use PEPhub to collaborate on sample-intensive biological projects.*
## What is PEPhub?
Just like GitHub allows you to share and edit projects that you are tracking with `git`, PEPhub allows you to share and edit **biological metadata** that is formatted as a **PEP** (a Portable Encapsulated Project). PEPhub allows you to:

- **Upload** your metadata to a central database
- **Edit** your metadata in a web interface
- **Share** your metadata with collaborators

## What is a PEP?
Portable Encapsulated Projects (PEPs) are standard format for biological sample metadata.  A PEP is simply a **yaml** + **csv** file (or just csv) -- the CSV file is a sample table, while the YAML file provides project-level metadata and sample modifiers. PEPs are a common input for running workflows using tools such as [Snakemake](https://snakemake.readthedocs.io/en/stable/), [Common Workflow Language](https://www.commonwl.org/), [Looper](http://pep.databio.org/looper), and other workflow systems. For more details, read the [PEP specification](http://pep.databio.org/spec/simple-example).

## How PEPhub and PEPs work together
Storing files in a central location is a key feature of PEPhub. Local, individualized storage of PEPs can quickly become intractable for large teams. To that end, PEPhub allows you to store these in a database that is accessible to anyone through a web interface. This allows for easy sharing and collaboration on projects.

In short, PEPs are the standard format for biological metadata, and PEPhub is the platform that allows you to store, edit, and share these PEPs. Through the API, one can easily access and retrieve PEPs for use in workflows and analyses.

## Ready to get started?
To get started storing metadata on PEPhub, you will need to log in. Click the button below to learn more about getting an account and logging in.

[Logging into PEPhub](/pephub/user/accounts){ .md-button .md-button--primary }