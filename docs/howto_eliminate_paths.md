---
title: Eliminate paths from sample table
redirect_from: "/docs/derived_attributes/"
---

The `derive` sample modifier, allows you to add new sample attributes that are derived from existing sample attributes.

## Example

```
sample_modifiers:
  derive: 
    attributes: [file_path]
    sources:
      source1: /data/lab/project/{organism}_{time}h.fastq
      source2: /path/from/collaborator/weirdNamingScheme_{external_id}.fastq
```

In this example, the samples' `file_path` attribute will be derived with one of two different paths, depending on the original value of the attribute (`source1` or `source2`). 

## Rationale

Sample tables often point to an input file or files for each sample. Of course, you could just add a column with the file path, like ``/path/to/input/file.fastq.gz``. For example:

```
"sample_name", "library", "organism", "time", "file_path"
"pig_0h", "RRBS", "pig", "0", "/data/lab/project/pig_0h.fastq"
"pig_1h", "RRBS", "pig", "1", "/data/lab/project/pig_1h.fastq"
"frog_0h", "RRBS", "frog", "0", "/data/lab/project/frog_0h.fastq"
"frog_1h", "RRBS", "frog", "1", "/data/lab/project/frog_1h.fastq"
```

This is common, but what if the data get moved, the filesystem changes, or you switch servers? Will this data still be there in 2 years? Do you want long file paths cluttering your sample table? What if you have 2 or 3 input files? Do you want to manually manage these unwieldy absolute paths?

The PEP specification makes it really easy to do better with the `derived` section of `sample_modifiers`. Derived attributes allow you to populate sample attributes based on a source template you specify in the `derived_sources` attribute. What was originally `/long/path/to/sample.fastq.gz` as a derived attribute would instead contain just a key, like `source1`. Here's an example of the same sample table using a `derived attribute` for `file_path`:

```
"sample_name", "library", "organism", "time", "file_path"
"pig_0h", "RRBS", "pig", "0", "source1"
"pig_1h", "RRBS", "pig", "1", "source1"
"frog_0h", "RRBS", "frog", "0", "source1"
"frog_1h", "RRBS", "frog", "1", "source1"
```

To do this, your project config file must specify two things: First, which attributes are derived (in this case, `file_path`); and second, a `derived_sources` section mapping keys to strings that will construct your path from other sample or project attributes, like this:


```
sample_modifiers:
  derive:
    attributes: [file_path]
    sources:
      source1: /data/lab/project/{sample_name}.fastq
      source2: /path/from/collaborator/weirdNamingScheme_{external_id}.fastq
```

That's it! The source string can use other sample attributes (columns) using braces, as in `{sample_name}`. The attributes will be automatically populated separately for each sample. To take this a step further, you'd get the same result with this config file, which substitutes `{sample_name}` for other sample attributes, `{organism}` and `{time}`:

```
sample_modifiers:
  derive:
    attributes: [file_path]
    sources:
      source1: /data/lab/project/{organism}_{time}h.fastq
      source2: /path/from/collaborator/weirdNamingScheme_{external_id}.fastq
```

As long as your file naming system is systematic, you can easily deal with any external naming scheme. You can specify as many derived columns as you want.

## Tips

Don't put absolute paths to files in your sample table. Instead, specify a source and then provide a template in the config file. This way if your data changes locations (which happens more often than we would like), or you change servers, or you want to share or publish the project, you just have to change the config file and not update paths in the sample table; this makes the sample table universal across environments, users, publication, etc. The whole project is now portable.

Think of each sample as belonging to a certain type (for simple experiments, the type will be the same); then define the location of these samples in the project configuration file. As a side bonus, you can easily include samples from different locations, and you can also share the same sample sample table on different environments (i.e. servers or users) by having multiple project config files (or, better yet, by defining a subproject for each environment). The only thing you have to change is the project-level expression describing the location, not any sample attributes (plus, you get to eliminate those annoying long/path/arguments/in/your/sample/annotation/sheet).
