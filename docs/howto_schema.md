---
title: "Write my own PEP schema"
---

## Validating a generic PEP

You can validate a PEP for the generic PEP format like this:

```
peppy validate path/to/project_config.yaml -s https://schema.databio.org/pep/2.0.0.yaml
```

## Validating a PEP for a specific tool

Even more useful than this is to validate your PEP against a more strict schema, like one for a particular pipeline or workflow. Now, most tools will require more information than is provided by a generic, minimal PEP. For example, a particular tool may need to have a specific attribute set for each sample, such as `genome`. 

## Writing a PEP schema

We recommend that workflow authors write a PEP schema that describes what sample and project attributes are required for their tool to work.

Here, we should describe how to go about writing a schema for your tool.

Let's say you're writing a tool that requires 3 arguments: `read1`, `read2`, and `genome`. It also offers optional argument called `read_length`. Your tool uses `peppy` so it expects the project metadata to be organized as a PEP. A project that validates with the generic PEP specification will not necessarily contain the attributes needed by your pipeline, so you want to write an extended schema to validate more strictly.

Example JSON-schema:

```
description: A example schema for a pipeline.
imports: http://schema.databio.org/pep/2.0.0.yaml
properties:
  samples:
    type: array
    items:
      type: object
      properties:
        read1:
          type: string
          description: "Fastq file for read 1"
        read2:
          type: string
          description: "Fastq file for read 2"
        genome:
          type: string
          description: "Refgenie genome registry identifier"          
        read_length:
          type: integer
          description: "Length of the Unique Molecular Identifier, if any"
      required:
        - read1
        - read2
        - genome
required:
  - samples
```

This document