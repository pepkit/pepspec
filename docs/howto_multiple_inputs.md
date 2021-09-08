---
title: Specify multiple input files
---

# How to specify multiple input files

Occasionally, a sample needs to have more than one value for an attribute. This doesn't fit naturally into a tabular data format because it requires a one-to-many relationship that is better handled by a relational database. For these kinds of attributes, the PEP specification uses a second table called `subsample_table`, which is added as an attribute in the project config file. To explain how this works, we'll use the most common example case of needing it: a single sample with multiple input files.

Sometimes you have multiple input files for one sample. For example, perhaps you have technical replicates that you want merged before running a pipeline. Or, a common use case is a single library that was spread across multiple sequencing lanes, yielding multiple input files. Rather than putting multiple lines in your sample table, which causes conceptual and analytical challenges, there are two ways to do this:

1. Use shell expansion characters (like `*` or `[]`) in your `derived.source` definition or filename (good for simple merges)
2. Specify a *subsample table* (formerly called a *merge table*), which maps input files to samples for samples with more than one input file (infinitely customizable for more complicated merges).


## Option 1: wildcards

To do the first option, just change your data source specifications, like this:

```{yaml}
derive:
  sources:
    data_R1: "${DATA}/{id}_S{nexseq_num}_L00*_R1_001.fastq.gz"
    data_R2: "${DATA}/{id}_S{nexseq_num}_L00*_R2_001.fastq.gz"
```

This only works if the attribute with multiple values is a file, and if you can process them with a shell wildcard. Other cases can be accommodated by the subsample table option.

## Option 2: the subsample table

A subsample table is a table with *one row per attribute* -- so a single sample appears multiple times in the table. Just provide a subsample table in your project config:

```{yaml}
sample_table: annotation.csv
subsample_table: subsample_table.csv
```

Make sure the `sample_name` column of this table matche the `sample_name` column in your sample_table, and then include any columns that require multiple values. `PEP` will automatically include all of these values as appropriate. 

Here's a simple example of a PEP that uses subsamples. If you define `annotation.csv` like this:

```{csv}
sample_name,library
frog_1,anySampleType
frog_2,anySampleType
```

Then point `subsample_table.csv` to the following, which maps `sample_name` to a new column called `file`

```{csv}
sample_name,file
frog_1,data/frog1a_data.txt
frog_1,data/frog1b_data.txt
frog_1,data/frog1c_data.txt
frog_2,data/frog2a_data.txt
frog_2,data/frog2b_data.txt
```

This sets up a simple relational database that maps multiple files to each sample. You can also combine merged columns with derived columns; columns will first be derived and then merged, leading to a very flexible way to point to any files you need to merge. Let's now look at a slightly more complex example that has two attributes we want to merge (such as the case with a paired-end sequencing experiment with multiple files for each R1 and R2):

```{csv}
sample_name	library
frog_1	anySampleType
frog_2	anySampleType
```

```{csv}
sample_name,read1,read2
frog_1,data/frog1a_R1.txt,data/frog1a_R2.txt
frog_1,data/frog1b_R1.txt,data/frog1b_R2.txt
frog_1,data/frog1c_R1.txt,data/frog1c_R2.txt
frog_2,data/frog2a_R1.txt,data/frog2a_R2.txt
frog_2,data/frog2b_R1.txt,data/frog2b_R2.txt
```

You can find more examples of projects that use merging in the examples at [PEP in practice](pep_in_practice.md).

A few tidbits you may need to consider when using subsample_table tables:

- Subsample tables are intended to handle multiple values *of the same type*. To handle different *classes* of input files, like read1 and read2, these are *not* the same type, and are therefore *not* put into a subsample table. Instead, these should be handled as different columns in the main sample annotation sheet (and therefore different arguments to the pipeline). It is possible that you will want to have read1 and read2, and then each of these could have multiple inputs, which would then be placed in the subsample table.

- If your project has some samples with subsample entries, but others without, then you only need to include samples in the subsample table if they have subsample attributes. Other samples can just be included in the primary annotation table. However, this means you'll need to make sure you provide the correct columns in the primary `sample_table` sheet; the simple example above assumes every sample has subsample attributes, so it doesn't need to define `file` in the `sample_table`. If you had samples without attributes specified in the subsample table, you'd need to specify that column in the primary sheet.

- In practice, we've found that almost every project can be solved using wildcards, and subsample tables are not necessary. If you start to think about how to use subsample tables, first double-check that you can't solve the problem using a simple wildcard; that makes it much easier to think about, and it should be possible as long as the files are named systematically.

- Warning: While you may use both wildcards and subsample tables for different samples within a project; **do not use both wildcards and a subsample table simultaneously for the same sample**, as it may lead to recursion.

- Keep in mind: **subsample tables is for files of the same type**. A paired-end sequencing experiment, for example, yields two input files for each sample (read1 and read2). These are *not equivalent*, so **you do not use subsample tables to put read1 and read2 files into the same attribute**; instead, you would list in a subsample table all files (perhaps from different lanes) for read1, and then, separately, all files for read2. This is two separate attributes, which each may have multiple files -- it's the multiple files that are accommodated by the subsample table, not the separate attributes.
