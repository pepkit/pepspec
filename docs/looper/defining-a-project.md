# How to define a project

## Start with a basic PEP

To start, you need a project defined in the [standard Portable Encapsulated Project (PEP) format](http://pep.databio.org). Start by [creating a PEP](https://pep.databio.org/spec/simple-example/).

## Specify the Sample Annotation within the Project Config

This information generally lives in a `project_config.yaml` file and corresponds to data in the `sample_annotation.csv` file.

Simplest example of a `project_config.yaml` file:
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

A more complicated example taken from [PEPATAC](https://pepatac.databio.org/en/latest/) of a `project_config.yaml` file:

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

## Sample annotation sheet

The above examples focus on the project config file. However, there is a second component, the sample annotation sheet.
The *sample annotation sheet* is a csv file containing information about all samples in a project, e.g. `sample_annotation.csv`.
This should be regarded as static and a project's most important metadata.

**One row corresponds to one pipeline run** (if there's just one pipeline run per sample, there's 1:1 correspondence between rows and samples as well.)

A sample annotation sheet may contain any number of columns you need for your project.
You can think of these columns as *sample attributes*, and you may use these columns later in your pipelines or analysis.
For example, you could define a column called `organism` and use the resulting attribute on a sample to adjust the assembly used by a pipeline through which it's run.

### Special columns

Certain keyword columns are required or provide `looper`-specific features.
Any additional columns become attributes of your sample and will be part of the project's metadata for the samples.
Mostly, you have control over any other column names you want to add, but there are a few reserved column names:

- `sample_name` - a **unique** string<sup>1</sup> identifying each sample. This is **required** for `Sample` construction,
but it's the *only required column*.
- `organism` - a string identifying the organism ("human", "mouse", "mixed"). ***Recommended** but not required*.
- `library` - While not needed to build a `Sample`, this column is required for submission of job(s).
It specifies the source of data for the sample (e.g. ATAC-seq, RNA-seq, RRBS).
`looper` uses this information to determine which pipelines are relevant for the `Sample`.
- `data_source` - This column is used by default to specify the location of the input data file.
Usually you want your annotation sheet to specify the locations of files corresponding to each sample.
You can use this to simplify pointing to file locations with a neat string-replacement method that keeps things clean and portable.
For more details, see the [derived columns section](#derived-columns).
Really, you just need any column specifying at least 1 data file for input. This is **required** for `looper` to submit job(s) for a `Sample`.
- `toggle` - If the value of this column is not 1, `looper` will not submit the pipeline for that sample.
This enables you to submit a subset of samples.

Here's an **example** annotation sheet:

```CSV
sample_name, library, organism, flowcell, lane, BSF_name, data_source
"albt_0h", "RRBS", "albatross", "BSFX0190", "1", "albt_0h", "bsf_sample"
"albt_1h", "RRBS", "albatross", "BSFX0190", "1", "albt_1h", "bsf_sample"
"albt_2h", "RRBS", "albatross", "BSFX0190", "1", "albt_2h", "bsf_sample"
"albt_3h", "RRBS", "albatross", "BSFX0190", "1", "albt_3h", "bsf_sample"
"frog_0h", "RRBS", "frog", "", "", "", "frog_data"
"frog_1h", "RRBS", "frog", "", "", "", "frog_data"
"frog_2h", "RRBS", "frog", "", "", "", "frog_data"
"frog_3h", "RRBS", "frog", "", "", "", "frog_data"

```

<sup>1</sup> The sample name should contain no whitespace. If it does, an error will be thrown.
Similarly, `looper` will not allow any duplicate entries under sample_name.


### Derived columns

On your sample sheet, you will need to point to the input file or files for each sample.
Of course, you could just add a column with the file path, like `/path/to/input/file.fastq.gz`. For example:

A ***bad* example**:

```CSV
sample_name,library,organism,time,file_path
pig_0h,RRBS,pig,0,/data/lab/project/pig_0h.fastq
pig_1h,RRBS,pig,1,/data/lab/project/pig_1h.fastq
frog_0h,RRBS,frog,0,/data/lab/project/frog_0h.fastq
frog_1h,RRBS,frog,1,/data/lab/project/frog_1h.fastq
```

This is common, and it works in a pinch with Looper, but what if the data get moved, or your file system changes, or you switch servers or move institutes?
Will this data still be there in 2 years? Do you want long file paths cluttering your annotation sheet?
What if you have 2 or 3 input files? Do you want to manually manage these unwieldy absolute paths?

Looper makes it really easy to do better. You can make one or your annotation columns into a flexible *derived column*
that will be populated based on a source template you specify in the project configuration file.
What was originally `/long/path/to/sample.fastq.gz` would instead contain just a key, like `source1`.
Columns that use a key like this are called *derived columns*.
Here's an example of the same sheet using a derived column (`file_path`):

A ***good* example**:
```CSV
sample_name,library,organism,time,file_path
pig_0h,RRBS,pig,0,source1
pig_1h,RRBS,pig,1,source1
frog_0h,RRBS,frog,0,source1
frog_1h,RRBS,frog,1,source1
```

For this to succeed, your project config file must specify two things:
- Which columns are to be derived (in this case, ``file_path``)
- A `data_sources` section mapping keys to strings that will construct your path, like this:
    ```yaml
    derived_columns: [file_path]
    data_sources:
      source1: /data/lab/project/{sample_name}.fastq
      source2: /path/from/collaborator/weirdNamingScheme_{external_id}.fastq
    ```

That's it! The source string can use other sample attributes (columns) using braces, as in `{sample_name}`.
The attributes will be automatically populated separately for each sample.
To take this a step further, you'd get the same result with this config file,
which substitutes `{sample_name}` for other sample attributes, `{organism}` and `{time}`:

```yaml
derived_columns: [file_path]
data_sources:
  source1: /data/lab/project/{organism}_{time}h.fastq
  source2: /path/from/collaborator/weirdNamingScheme_{external_id}.fastq
```

As long as your file naming system is systematic, you can easily deal with any external naming scheme, no problem at all.
The idea is this: don't put *absolute* paths to files in your annotation sheet.
Instead, specify a data source and then provide a regex in the config file.

Then if your data change locations (which happens more often than we would like), or you change servers,
or you want to share or publish the project, you just have to change the config file and not update paths in the annotation sheet.
This makes the annotation sheet universal across environments, users, publication, etc. The whole project is now portable.

You can specify as many derived columns as you want. An expression including any sample attributes (using `{attribute}`) will be populated for each of those columns.

Think of each sample as belonging to a certain type (for simple experiments, the type will be the same).
Then define the location of these samples in the project configuration file.
As a side bonus, you can easily include samples from different locations, and you can also use the same sample annotation sheet on different environments
(i.e. servers or users) by having multiple project config files (or, better yet, by defining a `subproject` for each environment).
The only thing you have to change is the project-level expression describing the location, not any sample attributes.
Plus, you get to eliminate those annoying `long/path/arguments/in/your/sample/annotation/sheet`.



### Implied columns

At some point, you may have a situation where you need a single sample attribute (or column)
to populate several different pipeline arguments with different values.
In other words, the value of a given attribute may *imply* values for other attributes.
It would be nice if you didn't have to enumerate all of these secondary, implied attributes,
and could instead just infer them from the value of the original attribute.

For example, if my `organism` attribute is `human`, this implies a few other secondary attributes
(which may be project-specific): For one project, I want to set `genome` to `hg38` and `macs_genome_size` to `hs`.
Of course, I could just define columns called `genome` and `macs_genome_size`, but these would be constant across samples, so it feels inefficient and unwieldy.
Plus, changing the aligned genome would require changing the sample annotation sheet (every sample, in fact).
You can certainly do this with `looper`, but a better way is to handle these things at the project level.

As a more elegant alternative, in a project config file `looper` will recognize a section called `implied_columns`.
Instead of hard-coding `genome` and `macs_genome_size` in the sample annotation sheet,
you can simply specify that the attribute `organism` *implies* additional attribute-value pairs
(which may vary by sample based on the value of the `organism` attribute).
This lets you specify assemblies, genome size, and other similar variables all in your project config file.

To do this, just add an `implied_columns` section to your project_config.yaml file. Example:

```yaml
implied_columns:
  organism:
    human:
      genome: "hg38"
      macs_genome_size: "hs"
    mouse:
      genome: "mm10"
      macs_genome_size: "mm"
```

There are 3 levels in the `implied_columns` hierarchy.
The first (directly under `implied_columns`; here, `organism`), are primary columns from which new attributes will be inferred.
The second layer (here, `human` or `mouse`) are possible values your samples may take in the primary column.
The third layer (`genome` and `macs_genome_size`) are the key-value pair of new, implied columns
for any samples with the required value for that primary column.

In this example, any samples with organism set to `"human"` will automatically also have attributes for `genome` (`"hg38"`) and for `macs_genome_size` (`"hs"`).
Any samples with `organism` set to `"mouse"` will have the corresponding values.
A sample with `organism` set to `"frog"` would lack attributes for `genome` and `macs_genome_size`, since those columns are not implied by `"frog"`.

This system essentially lets you set global, species-level attributes at the project level instead of duplicating
that information for every sample that belongs to a species.
Even better, it's generic, so you can do this for any partition of samples (just replace `organism` with whatever you like).

This makes your project more portable and does a better job conceptually with separating sample attributes from project attributes.
After all, a reference assembly is not a property of a sample, but is part of the broader project context.

