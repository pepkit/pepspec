---
title: "Write my own PEP schema"
---

# How to write my own PEP schema

## Validating a generic PEP

You can validate a PEP against a PEP schema using the [peppy Python package](http://peppy.databio.org) like this:

```
peppy validate path/to/your/PEP_config.yaml -s https://schema.databio.org/pep/2.0.0.yaml
```

## Validating a PEP for a specific tool

Most tools will require more attributes than a base PEP provides. For example, a tool may require a `genome` attribute for each sample and we need to validate a PEP against a stricter schema. You would do this in the same way, just using the more specialized schema:

```console
peppy validate path/to/project_config.yaml -s SCHEMA
```

Where SCHEMA is a URL or local file. The author of the tool you are using should provide this schema so that you can make sure you are providing the correct metadata for the tool.


## Writing a PEP schema

If you are a tool developer, we recommend you write a PEP schema that describes what sample and project attributes are required for your tool to work. PEP schemas use the [JSON-schema](https://json-schema.org/) vocabulary. Like the PEP itself, the schema is divided into two sections, one for the project config, and one for the samples. So, the base PEP schema defines an object with two components: a `config` object, and a `samples` array:

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

Let's say you're writing a PEP-compatible tool that requires 3 arguments: `read1`, `read2`, and `genome`, and also offers optional argument, `read_length`.  Validating the generic PEP specification will not confirm all required attributes, so you want to write an extended schema. Starting from the base above, we're not changing the `config` section so we can drop that, and we add new parameters for the required sample attributes like this:

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
