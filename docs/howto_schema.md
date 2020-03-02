---
title: "Write my own PEP schema"
---

# How to write my own PEP schema

## Validating a generic PEP

You can validate a PEP for the generic PEP format like this:

```console
peppy validate path/to/project_config.yaml -s https://schema.databio.org/pep/2.0.0.yaml
```

## Validating a PEP for a specific tool

Now, most tools will require more information than is provided by a generic, minimal PEP. For example, a particular tool may require the `genome` attribute is set for each sample. So, more useful than validating a generic PEP is to validate a PEP against a more strict schema, like one for a particular pipeline or workflow. You would do this in the same way, just using the more specialized schema:

```console
peppy validate path/to/project_config.yaml -s SCHEMA
```

Where SCHEMA is a URL or local file. The author of the tool you are using should provide this schema so that you can make sure you are providing the correct metadata for the tool.

If you are a tool developer and want to write your own schema, here's how to do it:

## Writing a PEP schema

We recommend that workflow authors write a PEP schema that describes what sample and project attributes are required for their tool to work.

PEP schemas use the [JSON-schema](https://json-schema.org/) vocabulary. Like the PEP itself, the schema is divided into two sections, one for the project config, and one for the samples. So, the base PEP schema defines an object with two components: `samples` array, and a `config` object:

```yaml
description: A example schema for a pipeline.
imports: http://schema.databio.org/pep/2.0.0.yaml
properties:
  config
    type: object
  samples:
    type: array
required:
  - samples
  - config
```

Let's say you're writing a tool that reads PEPs and requires 3 arguments: `read1`, `read2`, and `genome`. It also offers optional argument called `read_length`.  A project that validates with the generic PEP specification will not necessarily contain the attributes needed by your pipeline, so you want to write an extended schema to validate more strictly. Starting from the base above, we're not changing the `config` section so we can drop that out, and we add new parameters for the required sample attributes like this:

```yaml
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

This document defines the required an optional sample attributes for this pipeline. That's all you need to do, and your users can validate an existing PEP to see if it meets the requirements of your tool.
