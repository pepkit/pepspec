![Run pytests](https://github.com/pepkit/geopephub/workflows/Run%20installation%20test/badge.svg)
[![Github badge](https://img.shields.io/badge/source-github-354a75?logo=github)](https://github.com/pepkit/geopephub)



<h1 align="center">geopephub</h1>

### Automatic uploader of GEO metadata projects to [PEPhub](https://pephub.databio.org/geo).


This repository contains `geopephub` CLI, that enables to automatic upload GEO projects to PEPhub based on date and scheduled automatic uploading using GitHub actions. 
Additionally, the CLI includes a download command, enabling users to retrieve projects from specified namespace directly from the PEPhub database. This feature is particularly helpful for downloading all GEO projects at once.

---

**Documentation**: <a href="https://pep.databio.org/pephub" target="_blank">https://pep.databio.org/pephub</a>

**Source Code**: <a href="https://github.com/pepkit/geopephub" target="_blank">https://github.com/pepkit/geopephub</a>

---


## Installation
To install `geopephub` use this command: 
```
pip install git+https://github.com/pepkit/geopephub.git
```

# Overview:
The `geopephub` consists of 4 main functionalities:

1) Queuer: This module comprises functions that scan for new projects in **GEO**, generate a new cycle for the current run, and log details for each GEO project. It sets the project status to `queued` and adds it to the database.
2) Uploader: Checks if there are any queued cycles in the `cycle_status` table. It retrieves a list of queued projects, executes `GEOfetch` to download them, and uploads the results to PEPhub database using `pepdbagent`. `geopephub` updates the project upload status at each step, allowing for later checks to determine why the upload failed and what occurred.
3) Checker: This component examines previous cycles, verifies their status, and determines if they were executed. If a cycle was not executed or was unsuccessful, it triggers a rerun. In cases where only one project was unsuccessful, it attempts to upload it again. Additionally, if the cycle does not exist, it creates one using the queuer and uploads files using the uploader.
4) Downloader: Retrieves projects from the specified namespace, filters by uploading or updating date, and optionally sorts by name or date. It also allows setting a limit on the number of downloaded projects. Projects can be downloaded locally or to a specified S3 bucket. For more information, use the  `geopephub --help` command


More information about these processes can be found in the flowcharts and overview below.

![geopephub](../img/populator_overview.svg)

## Queuer Flowchart:
```mermaid
%%{init: {'theme':'forest'}}%%
stateDiagram-v2
    s1 --> s2 
    s2 --> s3
    s3 --> s4
    s4 --> s5
    s1: Create a new cycle
    s2: Find GEO updated projects with geofetch Finder
    s3: Add projects to the queue in sample status table
    s4: Change cycle status to queued
    s5: Exit
```

## Uploader Flowchart:

```mermaid
%%{init: {'theme':'forest'}}%%
stateDiagram-v2
    s1 --> s2 
    s2 --> s3
    s3 --> s4
    s4 --> s5
    s5 --> s6
    s6 --> s7
    s7 --> s8

    s7 --> s2
    s6 --> s3

    s1: Get queued cycles by specifying namespace
    s2: Change status of the cycle
    s2: Get each element from list of queued cycle
    s3: Get each project (GSE) from one cycle
    s4: Change status of the project in project_status_table
    s5: Get specified project by running Geofetcher
    s6: Using pepdbagent add project to the DB
    s6: Change status of the project in project_status_table
    s7: Change status of cycle in cycle_status_table
    s8: Exit
```

## Checker Flowchart:
```mermaid
graph TD
    A[Choose cycle to check] --> B{Did it run?}
    B -->|Yes| C{Was it successful?}
    B -->|No| D[Run Queuer for the cycle]
    C -->|Yes| E{Did all samples succeed?}
    C -->|No| D

    D --> D1[Run Uploader for the cycle]
    D1 --> K

    E --> |Yes| K[Exit]
    E --> |No| G[Retrieve failed samples]

    G --> H[Run Queuer for samples]
    H --> F[Run Uploader for queued samples]
    
    F --> I[Change samples status in the table]

    I --> J[Change cycle status in the table]

    J --> K[Exit]

```
