---
title: Specify multi-value attributes
---

# How to specify multiple input files

Occasionally, a sample needs to have more than one value for an attribute. For example, you may have multiple input files for one sample, such as a single library that was spread across multiple sequencing lanes. This doesn't fit naturally into a tabular data format because it requires a one-to-many relationship. For these kinds of attributes, the PEP specification provides three possibilities:

1. Use shell expansion characters (like `*` or `[]`) in a `derived.source` definition (good for situations where the multi-valued attributes are file paths)
2. Specify a *subsample table* (infinitely customizable for more complicated merges).
3. Use a multiple rows per sample (useful when a single sample table is required).

To explain how this works, we'll use the most common example case of needing it: a single sample with an attribute that points to a file, but there are multiple input files for that attribute.

## Option 1: wildcards

To use wildcards, just use asterisks in your data source specifications, like this:

```{yaml}
derive:
  sources:
    data_R1: "${DATA}/{id}_S{nexseq_num}_L00*_R1_001.fastq.gz"
    data_R2: "${DATA}/{id}_S{nexseq_num}_L00*_R2_001.fastq.gz"
```

PEP will automatically glob these to whatever files are on disk, and use those as the multiple values for the attribute. This only works if:

1. the attribute with multiple values is a file,
2. the file paths are systematic, computable with a shell wildcard, and 
3. the file system is local to the PEP and can be computed at runtime.

## Option 2: the subsample table

A subsample table is a table with *one row per attribute* -- so a single sample appears multiple times in the table. Just provide a subsample table in your project config:

```{yaml}
sample_table: annotation.csv
subsample_table: subsample_table.csv
```

Make sure the `sample_name` column of this table match the `sample_name` column in your sample_table, and then include any columns that require multiple values. `PEP` will automatically include all of these values as appropriate. 

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

This sets up a simple relational database that maps multiple files to each sample. You can also combine these multi-value attributes with derived columns; columns will first be derived, and then merged. Let's now look at a slightly more complex example that has two multi-value attributes (such as the case with a paired-end sequencing experiment with multiple files for each R1 and R2):

The sample table is:

```{csv}
sample_name	library
frog_1	anySampleType
frog_2	anySampleType
```

And the subsample table is:

```{csv}
sample_name,read1,read2
frog_1,data/frog1a_R1.txt,data/frog1a_R2.txt
frog_1,data/frog1b_R1.txt,data/frog1b_R2.txt
frog_1,data/frog1c_R1.txt,data/frog1c_R2.txt
frog_2,data/frog2a_R1.txt,data/frog2a_R2.txt
frog_2,data/frog2b_R1.txt,data/frog2b_R2.txt
```

This yields 2 samples, each with a single-valued attribute of `library`, and multi-valued attributes of `read1` and `read2`.

## Option 3: Multiple rows per sample

In PEP v2.1.0, we relaxed the constraint that each sample must correspond to exactly one row in the sample table, and introduce the possibility of encoding multi-valued samples with multiple rows. The same data as the two-table approach above can be represented like this:

```{csv}
sample_name,library,read1,read2
frog_1,anySampleType,data/frog1a_R1.txt,data/frog1a_R2.txt
frog_1,,data/frog1b_R1.txt,data/frog1b_R2.txt
frog_1,,data/frog1c_R1.txt,data/frog1c_R2.txt
frog_2,anySampleType,data/frog2a_R1.txt,data/frog2a_R2.txt
frog_2,,data/frog2b_R1.txt,data/frog2b_R2.txt
```

Now, this is the `sample_table`, but the `sample_name` column is not unique -- the first row has values for any single-valued attributes (`library` in the example), and then other columns can be specified in multiple rows. The PEP processor will integrate these samples in correctly represent this as two samples.

## Further thoughts

- There are pros and cons to each of these approaches. Representing a single sample with multiple rows in the sample table can cause conceptual and analytical challenges. There is value in the simplicity of being able to see each row as a separate sample, which is preserved in the subsample table approach. However, this leads to the requirement of an additional file to represent samples, which can be problematic in other settings. One advantage of PEP is that either approach can be used, so you can use the approach that fits your situation best.

- Subsample tables are intended to handle multiple values *of the same type*. To handle different *classes* of input files, like read1 and read2, these are *not* the same type, and are therefore *not* put into a subsample table. Instead, these should be handled as different columns in the main sample annotation sheet (and therefore different arguments to the pipeline). It is possible that you will want to have read1 and read2, and then each of these could have multiple inputs, which would then be placed in the subsample table.

- If your project has some samples with subsample entries, but others without, then you only need to include samples in the subsample table if they have subsample attributes. Other samples can just be included in the primary annotation table. However, this means you'll need to make sure you provide the correct columns in the primary `sample_table` sheet; the simple example above assumes every sample has subsample attributes, so it doesn't need to define `file` in the `sample_table`. If you had samples without attributes specified in the subsample table, you'd need to specify that column in the primary sheet.

- In practice, we've found that most projects can be solved using wildcards, and subsample tables are not necessary. If you start to think about how to use subsample tables, first double-check that you can't solve the problem using a simple wildcard; that makes it much easier to think about, and it should be possible as long as the files are named systematically.

- **Don't combine these approaches**.  Using both wildcards and a subsample table simultaneously for the same sample can lead to recursion. Using a subsample table requires your sample table to have unique sample names, which precludes the possibility of multi-row samples. So, just pick an approach and stick to it.

- Keep in mind: **subsample tables is for files of the same type**. A paired-end sequencing experiment, for example, yields two input files for each sample (read1 and read2). These are *not equivalent*, so **you do not use subsample tables to put read1 and read2 files into the same attribute**; instead, you would list in a subsample table all files (perhaps from different lanes) for read1, and then, separately, all files for read2. This is two separate attributes, which each 