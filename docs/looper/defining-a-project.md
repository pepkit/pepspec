# How to define a project

## 1. Start with a basic PEP

To start, you need a project defined in the [standard Portable Encapsulated Project (PEP) format](http://pep.databio.org). Start by [creating a PEP](https://pep.databio.org/spec/simple-example/).

## 2. Specify the Sample Annotation

This information generally lives in a `project_config.yaml` file.

Simplest example:
```yaml
pep_version: 2.0.0
sample_table: sample_annotation.csv
```

You can also add sample modifiers to the project file `derive` or `imply` attributes:

For example:
If you have a project that contains samples of different types, then you can use an `imply` modifier in your PEP to select which pipelines you want to run on which samples, like this:


```yaml
sample_modifiers:
  imply:
    - if:
        protocol: "RRBS"
      then:
        pipeline_interfaces: "/path/to/pipeline_interface.yaml"
    - if:
        protocol: "ATAC"
      then:
        pipeline_interfaces: "/path/to/pipeline_interface2.yaml"
```

You can also use `derive` to derive attributes from the PEP:

```yaml
sample_modifiers:
  derive:
    attributes: [read1, read2]
    sources:
      # Obtain tutorial data from http://big.databio.org/pepatac/ then set
      # path to your local saved files
      R1: "${TUTORIAL}/tools/pepatac/examples/data/{sample_name}_r1.fastq.gz"
      R2: "${TUTORIAL}/tools/pepatac/examples/data/{sample_name}_r2.fastq.gz"

```

A more complicated example taken from [PEPATAC](https://pepatac.databio.org/en/latest/):

```yaml
pep_version: 2.0.0
sample_table: tutorial.csv

sample_modifiers:
  derive:
    attributes: [read1, read2]
    sources:
      # Obtain tutorial data from http://big.databio.org/pepatac/ then set
      # path to your local saved files
      R1: "${TUTORIAL}/tools/pepatac/examples/data/{sample_name}_r1.fastq.gz"
      R2: "${TUTORIAL}/tools/pepatac/examples/data/{sample_name}_r2.fastq.gz"
  imply:
    - if: 
        organism: ["human", "Homo sapiens", "Human", "Homo_sapiens"]
      then: 
        genome: hg38
        prealignment_names: ["rCRSd"]
        deduplicator: samblaster # Default. [options: picard]
        trimmer: skewer          # Default. [options: pyadapt, trimmomatic]
        peak_type: fixed         # Default. [options: variable]
        extend: "250"            # Default. For fixed-width peaks, extend this distance up- and down-stream.
        frip_ref_peaks: None     # Default. Use an external reference set of peaks instead of the peaks called from this run
```


## 3. Customize looper

You can also customize things further. Under the `looper` section, you can provide a `cli` keyword to specify any command line (CLI) options from within the project config file. The subsections within this section direct the arguments to the respective `looper` subcommands. So, to specify, e.g. sample submission limit for a `looper run` command use:

```yaml
looper:
  output_dir: "/path/to/output_dir"
  cli:
    run:
      limit: 2
```

or, to pass this argument to any subcommand:

```yaml
looper:
  output_dir: "/path/to/output_dir"
  all:
    limit: 2
```

Keys in the `cli.<subcommand>` section *must* match the long argument parser option strings, so `command-extra`, `limit`, `dry-run` and so on. For more CLI options refer to the subcommands [usage](usage.md).
