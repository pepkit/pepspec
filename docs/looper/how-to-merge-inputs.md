# How to handle multiple input files

*Dealing with multiple input files is described in detail in the [PEP documentation](https://pep.databio.org/spec/howto-multi-value-attributes/).*

Briefly:

Sometimes you have multiple input files that you want to merge for one sample. For example, a common use case is a single library that was spread across multiple sequencing lanes, yielding multiple input files that need to be merged, and then run through the pipeline as one. Rather than putting multiple lines in your sample annotation sheet, which causes conceptual and analytical challenges, PEP has two ways to merge these:

1. Use shell expansion characters (like `*` or `[]`) in your file path definitions (good for simple merges)
2. Specify a *sample subannotation tables* which maps input files to samples for samples with more than one input file (infinitely customizable for more complicated merges).

To accommodate complex merger use cases, this is infinitely customizable.

To do the first option, simply change the data source specification:

```yaml
data_sources:
  data_R1: "${DATA}/{id}_S{nexseq_num}_L00*_R1_001.fastq.gz"
  data_R2: "${DATA}/{id}_S{nexseq_num}_L00*_R2_001.fastq.gz"
```

For the second option, provide *in the `metadata` section* of your project config file a path to merge table file:

```yaml
metadata:
  merge_table: mergetable.csv
```

Make sure the `sample_name` column of this table matches, and then include any columns needed to point to the data.
Looper will automatically include all of these files as input passed to the pipelines.

***Warning***: do not use *both* of these options for the same sample at the same time; that will lead to multiple mergers.

**Note**: mergers are *not* the way to handle different functional/conceptual *kinds* of input files (e.g., `read1` and `read2` for a sample sequenced with a paired-end protocol).
Such cases should be handled as *separate derived columns* in the main sample annotation sheet if they're different arguments to the pipeline.




## Multi-value sample attributes behavior in the pipeline interface command templates

Both sample subannotation tables and shell expansion characters lead to sample attributes with multiple values, stored in a list of strings (`multi_attr1` and `multi_attr1`), as opposed to a standard scenario, where a single value is stored as a string (`single_attr`):

```
Sample
sample_name: sample1
subsample_name: ['0', '1', '2']
multi_attr1: ['one', 'two', 'three']
multi_attr2: ['four', 'five', 'six']
single_attr: test_val
```

### Access individual elements in lists

Pipeline interface author can leverage that fact and access the individual elements, e.g iterate over them and append to a string using the Jinja2 syntax:

```bash
pipeline_name: test_iter
pipeline_type: sample
command_template: >
  --input-iter {%- for x in sample.multi_attr1 -%} --test-individual {x} {% endfor %} # iterate over multiple values
  --input-single {sample.single_attr} # use the single value as is

```

This results in a submission script that includes the following command:
```bash
--input-iter  --test-individual one  --test-individual two  --test-individual three
--input-single  test_val
```

### Concatenate elements in lists

The most common use case is just concatenating the multiple values and separate them with space -- **providing multiple input values to a single argument on the command line**. Therefore, all the multi-value sample attributes that have not been processed with Jinja2 logic are automatically concatenated. For instance, the following command template in a pipeline interface will result in the submission script presented below:

Pipeline interface:
```bash
pipeline_name: test_concat
pipeline_type: sample
command_template: >
  --input-concat {sample.multi_attr1} # concatenate all the values
```

Command in the submission script:
```bash
--input-concat  one two three
```
