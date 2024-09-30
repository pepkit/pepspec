---
title: Remove genome from sample table
---

# How to remove genome from a sample table

Many sample tables include identifiers like a genome or transcriptome assembly (*e.g.* `hg38`) that really are an aspect of an analysis, rather than an attribute of a particular sample. If you store these attributes within the sample table, you reduce its portability because those attributes only apply to that particular analysis. If samples are only used for as single analysis, that's fine, but the point of PEP is to encourage re-use of data, so we'd like our sample tables to be as portable as possible. Instead, if you store these variables in the project configuration file, *the sample table could be re-used across projects with different analysis settings*. 

One way to solve this is to use an `append` modifier to add a `genome` attribute to each sample from the project config file.

```
sample_modifiers:
  append:
    genome: "hg38"
```

This way, we've moved the 'genome' attribute out of the sample table. Another analysis that could run on this same set of input data could now use the sample table without issue. In fact, we could even include these two analyses in the same project config file using an amendment:

```
sample_modifiers:
  append:
    genome: "hg38"

project_modifiers:
  amend:
    hg19_alignment:
      sample_modifiers:
        append:
          genome: "hg19"
```

Now, when loading this project, if you run `amendments=hg19_alignment`, the project will align to hg19 instead of hg38.


### Example with multiple species

The `append` modifier will add the same value to all samples; if your project requires that some samples be aligned to different assemblies, you'll need more power. The `imply` sample modifier allows you to create new sample attributes whose value depends on the *value* of another attribute. Here's an example that adds a genome attribute with a value that depends on another attribute:


```
sample_modifiers:
  imply:
    - if:
        organism: "human"
      then:
        genome: "hg38"
        macs_genome_size: "hs"
    - if:
        organism: "mouse"
      then:
        genome: "mm10"
        macs_genome_size: "mm"
```

In this example, if my `organism` attribute is `human`, this implies a few other project-specific attributes. For one project, I want to set `genome` to `hg38` and `macs_genome_size` to `hs`. Of course, I could just define columns called `genome` and `macs_genome_size`, but this has several disadvantages: First, changing the aligned genome would require changing every sample in the sample table. Second, the genome is now tied to the sample table, so it could not be used in a different project that used a different genome. A better way would be handle these attributes at the project level using `imply`.

Instead of hard-coding `genome` and `macs_genome_size` in the sample table, you can simply specify that the attribute `organism` **implies** additional attribute-value pairs (which may vary by sample based on the value of the `organism` attribute). This lets you specify the genome, transcriptome, genome size, and other similar variables all in your project configuration file. After all, a reference genome assembly is really not an inherent property of a sample, but of a sample in respect to a particular project or alignment.


