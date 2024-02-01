# How to write a PEP schema

If you are a tool developer, we recommend you write a PEP schema that describes what sample and project attributes are required for your tool to work. PEP schemas use the [JSON Schema](https://json-schema.org/) vocabulary, plus some additional features. This guide will walk you through everything you need to know to write your own schema. It assumes you already have a basic familiarity with JSON Schema.


## Importing the base PEP schema

One of the features added by `eido` is the `imports` attribute. This allows you to extend existing schemas. We recommend your new PEP schema start by importing the [base PEP schema](http://schema.databio.org/pep/2.0.0.yaml). This will ensure that the putative PEP at least follows the basic PEP specification, which you will then build on with your tool-specific requirements. Here's how we'll start with importing the generic base PEP schema:

```yaml
description: A example schema for a pipeline.
imports:
  - http://schema.databio.org/pep/2.0.0.yaml
```

You can also use the `imports` to build other schemas that subclass your own schemas.

## Project and sample sections

Like the PEP itself, the schema is divided into two sections, one for the project config, and one for the samples. So, base PEP schema defines an object with two components: a `config` object, and a `samples` array:


```yaml
description: A example schema for a pipeline.
imports:
  - http://schema.databio.org/pep/2.0.0.yaml
properties:
  config:
    type: object
  samples:
    type: array
required:
  - samples
  - config
```


## Required sample attributes

Let's say you're writing a PEP-compatible tool that requires 3 arguments: `read1`, `read2`, and `genome`, and also offers optional argument `read_length`.  Validating the generic PEP specification will not confirm all required attributes, so you want to write an extended schema. Starting from the base above, we're not changing the `config` section so we can drop that, and we add new parameters for the required sample attributes like this:

```yaml
description: A example schema for a pipeline.
imports:
  - http://schema.databio.org/pep/2.0.0.yaml
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

## Required input files

In the above example, we listed `read1` and `read2` attributes as *required*. This will enforce that these attributes must be defined on the samples, but for this example, this is not enough -- these also must *point to files that exist*. Checking for files is outside the scope of JSON Schema, which only validates JSON documents, so eido extends JSON Schema with the ability to specify which attributes should point to files.

Eido provides two ways to do it: `files` and `required_files`. The basic `files` is simply used to specify which attributes point to files, which are not required to exist. This is useful for tools that want to calculate the total size of any provided inputs, for example. The `required_files` list specifies that the attributes point to files that *must exist*, otherwise the PEP doesn't validate. Here's an example of specifying an optional and required input attribute:

```yaml
description: A PEP for ATAC-seq samples for the PEPATAC pipeline.
imports:
  - http://schema.databio.org/pep/2.0.0.yaml
properties:
  samples:
    type: array
    items:
      type: object
      properties:
        sample_name:
          type: string
          description: "Name of the sample"
        organism:
          type: string
          description: "Organism"
        protocol:
          type: string
          description: "Must be an ATAC-seq or DNAse-seq sample"
        genome:
          type: string
          description: "Refgenie genome registry identifier"
        read_type:
          type: string
          description: "Is this single or paired-end data?"
          enum: ["SINGLE", "PAIRED"]
        read1:
          type: string
          description: "Fastq file for read 1"
        read2:
          type: string
          description: "Fastq file for read 2 (for paired-end experiments)"
      required_files:
        - read1
      files:
        - read1
        - read2
```

This could a valid example for a pipeline that accepts either single-end or paired-end data, so `read1` must point to a file, whereas `read2` isn't required, but if it does point to a file, then this file is also to be considered an input file.


## Example schemas

If you need more information, it would be a good idea to look at [example schemas](example-schemas.md) for ideas.
