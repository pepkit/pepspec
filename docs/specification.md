---
title: PEP specification
---

<!-- Table of contents: 
* The generated Toc will be an unordered list
{:toc} -->

<h1>PEP specification</h1>

Table of contents:

[TOC]

## Introduction

Organizing and annotating sample data is an important task in data-intensive bioinformatics, but each dataset is typically annotated uniquely. Furthermore, data processing tools typically expect a unique format for sample annotation. There is no standard way to represent metadata that spans projects and tools. This restricts the portability and reusability of annotated datasets and software that processes them.

*Portable Encapsulated Projects* (*PEP* for short) seeks to make datasets and related software more portable and reusable by specifying a metadata structure. PEPs are typically data-intensive bioinformatics projects with many samples (which could be individual experiments, organisms, cell lines, *etc.*). However, the concepts are generic and could be applied to any collection of metadata represented in tabular form. The PEP specification also provides features that make metadata more portable, across both computing environments and processing tools. 

## Terminology and components of a PEP

In PEP parlance, **a *project* is a collection of metadata that annotates a set of samples.** A **sample** is loosely defined as any unit that can be collected together in a project. The **PEP specification** is a way to organize project and sample metadata in files, and a **PEP** is a project that follows the specification. The PEP specification divides metadata into two components: sample metadata, which can vary by sample, and project metadata, which applies to all samples. These two components are stored in separate files. A complete PEP consists of up to 3 files:

- **Project config file** - REQUIRED. a `yaml` file containing project-level metadata
- **Sample table** - RECOMMENDED. a `csv` file of sample metadata, with 1 row per sample
- **Subsample table** - OPTIONAL. A `csv` file of sample  with multiple rows for each sample, used to specify sample attributes with multiple values.

This document describes each of these 3 files in detail.

## Goals and benefits of using a PEP

The PEP specification has 2 primary goals:

1. To make sample-heavy sample annotations more reusable. By making it easy to decouple analysis-specific or environment-specific information from the sample metadata, it becomes eas

2. To make software that analyzes multi-sample datasets more reusable. applying tools to external data. 

3. To provide a way to formalize required metadata and validate it. The PEP specification provides a generic schema and an easy to way to extend it so that tool developers can formally describe what sample and project metadata their tool requires. Users can then use validation to identify which software is compatible with their data.

## Validating a PEP

This document describes a specification for a generic PEP, which is formally described with a schema at [schema.databio.org/PEP/pep_v2.yaml](https://schema.databio.org/PEP/pep_v2.yaml). You can validate a PEP against a PEP schema using the `peppy` Python package, which is also the reference implementation of the PEP specification. Validate a generic PEP like this:

```
peppy validate path/to/your/PEP_config.yaml -s https://schema.databio.org/PEP/pep_v2.yaml
```

PEP schemas use an extended version of the [JSON-schema](https://json-schema.org/) vocabulary. The generic schema may be easily extended into a more specific schema that adds new requirements or optional attributes, requires input files, and so forth. You can find more detail about how to extend and use these schemas in the [How to guide for PEP validation](/docs/validation).

## Project config file specification

The project config file is the source of project-level information. It is the only required file and must be in `yaml` format. The config file includes six recognized project attributes, most being optional:

- `pep_format_version` - REQUIRED
- `sample_table`- RECOMMENDED
- `subsample_table`- OPTIONAL
- `sample_modifiers` - OPTIONAL
- `amendments` - OPTIONAL
- `imports` - OPTIONAL

These attributes may appear in any order.

Example

```
pep_version: 2.0.0
sample_table: "path/to/sample_table.csv"
subsample_table: "path/to/subsample_table.csv"
sample_modifiers:
  append:
    attribute1: value
    attr2: val2	
  duplicate:
    oldattr: newattr
  imply:
    - if:
        genome: ["hg18", "hg19", "hg38"]
      then:
        organism: "human"
  derive:
    attributes: [read1, read2, other_attr]
    sources:
      key1: "path/to/derived/value/{sample.attribute}/{project.attribute}"
      key2: "path/to/derived/value/{sample.attribute}/{project.attribute}"

amendments:
  variant1:
    sample_table: "path/to/alternative_table.csv"

imports:
  - external_pep.yaml
  - http://url.com/pep.yaml
```

### Project attribute: `pep_version`

The only required project attribute, which documents the version of the PEP specification this PEP complies with. For PEP version 2.0.0, this must be the string `"2.0.0"`.

### Project attribute: `sample_table`

The `sample_table` is a path (string) to the sample csv file. It can be absolute or relative; relative paths are assumed relative to the location of the `project_config.yaml` file. The target file is expected to comply with the PEP specification for the sample table, described later.

### Project attribute: `subsample_table`

The `subsample_table` is a path (string) to the subsample csv file. Like with the sample_table attribute, relative paths are assumed relative to the location of the `project_config.yaml` file. The target file is expected to comply with the PEP specification for the subsample table.

### Project attribute: `sample_modifiers`

The sample modifiers allows you to modify sample attributes from within the project configuration file. You can use this to add new attributes to samples in a variety of ways, including attributes whose value varies depending on values of existing attributes, or whose values are composed of existing attribute values. This is a key feature of PEP that allows you to make the sample tables more portable. There are 4 subsections corresponding to 4 types of sample modifier: `append`, `duplicate`, `imply`, and `derive`.

The samples will be modified in this order: append, duplicate, imply, derive. Within each modifiers, samples will be modified in the order in which the commands are listed.

#### *sample_modifiers.append*

The `append` modifier adds additional sample attributes with a *constant value across all samples*. 

Example:

```yaml
sample_modifiers:
  append:
    read_type: SINGLE
```

This example would add an attribute named `read_type` to each sample, and the value would be `SINGLE` for all samples. This modifier is useful alone to add constant attributes, and can also be  combined with `derive` and/or `imply`.


#### *sample_modifiers.duplicate*

The `duplicate` modifier copies an existing sample attribute to a new attributes with a different name. This can be useful if you need to tweak a PEP to work under a different tool that specifies a different schema for the same data.

Example:

```yaml
sample_modifiers:
  duplicate:
    old_attribute_name: new_attribute_name
```

This example would copy the value of `old_attribute_name` to a new attribute called `new_attribute_name`.


#### *sample_modifiers.imply*

The `imply` modifier adds sample attributes with values that depends on the *value* of an existing attribute. Under the `imply` keyword is a list of items. Each item has an `if` section and an `then` section. The `if` section defines one or more attributes, each with one or more possible values. If *all* attributes listed have *any* of the values in the list for that attribute, then the sample passes the conditional and the new attributes will be implied. One or more attributes to imply are listed under the `then` section, with the key specifying the name of the attribute and the value its value.

Example:

```yaml
sample_modifiers:
  imply:
    - if:
        organism: "human"
      then:
        genome: "hg38"
        macs_genome_size: "hs"
```

This example will take any sample with `organism` attribute set to the string "human" and add attributes of `genome` (with value "hg38") and `macs_genome_size` (with value "hs"). This example shows only 1 implication, but you can include as many as you like.

Implied attributes can be useful for pipeline arguments. For instance, it may that one sample attribute implies several more. Rather than encoding these each as separate columns in the annotation sheet for a particular pipeline, you may simply indicate in the `project_config.yaml` that samples of a certain type should automatically inherit additional attributes. For more details, see [implied attributes](/docs/implied_attributes).

#### *sample_modifiers.derive*

The `derive` sample modifier provides converts existing sample attribute values into new values derived from other existing sample attribute values. It contains two sections; in `attributes` is a list of existing attributes that should be derived; in `sources` is a mapping of key-value pairs that defines the templates used to derive the new attribute values.

Example:

```yaml
sample_modifiers:
  derive:
    attributes: [read1, read2, data_1]
    sources:
      key1: "/path/to/{sample_name}_{sample_type}.bam"
      key2: "/path/from/collaborator/weirdNamingScheme_{external_id}.fastq"
      key3: "${HOME}/{test_id}.fastq"
```

In this example, the samples should already have attributes named `read1`, `read2`, and `data_1`, which are flagged as attributes to derive. These attribute values should originally be set to one of the keys in the `sources` section: `key1`, `key2`, or `key3`. The `derive` modifier will replace any samples set as `key1` with the specified string (`"/path/to/{sample_name}_{sample_type}.bam"`), but with variables like `{sample_name}` populated with the values of other sample attributes. The variables in the file paths are formatted as `{variable}`, and are populated by sample attributes (columns in the sample annotation sheet). For example, your files may be stored in `/path/to/{sample_name}.fastq`, where `{sample_name}` will be populated individually for each sample in your PEP. You can also use shell environment variables (like ``${HOME}``).

Using `derive` is a powerful and flexible way to point to data files on disk. This enables you to point to more than one input file for each sample. For more details and a complete example, see [derived attributes](/docs/derived_attributes).

### Project attribute: `amendments`

The `amendments` project attribute specifies variations of a project within one file. When a PEP is parsed, you may specify one or more included amendments, which will amend the values in the processed PEP.

For example:


```yaml
sample_table: annotation.csv
amendments:
  my_project2:
    sample_table: annotation2.csv
  my_project3:
    sample_table: annotation3.csv
...
```

If you load this configuration file, by default it sets `sample_table` to `annotation.csv`. If you don't activate any amendments, they are ignored. But if you choose, you may activate one of the two amendments, which are called `my_project2` and `my_project3`. If you activate `my_project2`, by passing `amendments=my_project2` when parsing the PEP, the resulting object will use the `annotation2.csv` sample_table instead of the default `annotation.csv`. All other project settings will be the same as if no amendment was activated because there are no other values specified in the `my_project2` amendment.

Amendments are useful to define multiple similar projects within a single project config file. Under the amendments key, you specify names of amendments, and then underneath these you specify any project config variables that you want to override for that particular amendment. It is also possible to activate more than one amendment in priority order, which allows you to combine different project features on-the-fly. For more details, see [amendments](/docs/amendments).


### Project attribute: `imports`

The `imports` key allows the config file to import other PEP config files. The values in the imported files will be overridden by the corresponding entries in the current config file. Imports are recursive, so an imported file that imports another file is allowed; the imports are resolved in cascading order with the most distant imports happening first, so the closest configuration options override the more distant ones.

Example:

```yaml
imports:
  - path/to/parent_project_config.yaml
```

## Sample table specification

The `sample_table` is a `.csv` file containing information about all samples (or pieces of data) in a project. **One row corresponds to one sample**. A sample table may contain any number of columns with any column names. Each columns corresponds to an attribute of a sample. For this reason, we sometimes use the word `column` and `attribute` interchangeably. 

The only requirement for the column names is that the table **MUST** include a column named `sample_name`, which should specify a **unique** string identifying each sample. This should be a string without whitespace (space, tabs, etc...). Any additional columns become attributes of your sample and will be part of the project's metadata for the samples. 

**Example:**
```
"sample_name", "protocol", "organism", "flowcell", "lane",  "data_source"
"albt_0h", "RRBS", "albatross", "BSFX0190", "1", "bsf_sample"
"albt_1h", "RRBS", "albatross", "BSFX0190", "1", "bsf_sample"
"albt_2h", "RRBS", "albatross", "BSFX0190", "1", "bsf_sample"
"albt_3h", "RRBS", "albatross", "BSFX0190", "1", "bsf_sample"
"frog_0h", "RRBS", "frog", "", "", "frog_data"
"frog_1h", "RRBS", "frog", "", "", "frog_data"
"frog_2h", "RRBS", "frog", "", "", "frog_data"
"frog_3h", "RRBS", "frog", "", "", "frog_data"
```

## Subsample table specification

The `subsample_table` is a `.csv` file that annotates multi-value sample attributes. Multiple values for an attribute are specified as multiple rows with the same sample name. The subsample table contains a column named `sample_name` that **must** map to the column of the same name in the sample table.

Here's a simple example. If you define the `sample_table` like this:

```{csv}
sample_name,library
frog_1,anySampleType
frog_2,anySampleType
```

Then point `subsample_table` to the following, which maps `sample_name` to a new column called `file`

```{csv}
sample_name,file
frog_1,data/frog1a_data.txt
frog_1,data/frog1b_data.txt
frog_1,data/frog1c_data.txt
frog_2,data/frog2a_data.txt
frog_2,data/frog2b_data.txt
```

This sets up a simple relational database that maps multiple files to each sample. You can also combine a subsample table with derived attributes; attributes will first be derived and then merged, leading to a very flexible way to point to many files of a given type for single sample.