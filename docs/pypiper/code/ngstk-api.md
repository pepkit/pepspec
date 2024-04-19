<script>
document.addEventListener('DOMContentLoaded', (event) => {
  document.querySelectorAll('h3 code').forEach((block) => {
    hljs.highlightBlock(block);
  });
});
</script>

<style>
h3 .content { 
    padding-left: 22px;
    text-indent: -15px;
 }
h3 .hljs .content {
    padding-left: 20px;
    margin-left: 0px;
    text-indent: -15px;
    martin-bottom: 0px;
}
h4 .content, table .content, p .content, li .content { margin-left: 30px; }
h4 .content { 
    font-style: italic;
    font-size: 1em;
    margin-bottom: 0px;
}

</style>


# Package `pypiper` Documentation

## <a name="NGSTk"></a> Class `NGSTk`
Class to hold functions to build command strings used during pipeline runs. Object can be instantiated with a string of a path to a yaml `pipeline config file`. Since NGSTk inherits from `AttMapEcho`, the passed config file and its elements will be accessible through the NGSTk object as attributes under `config` (e.g. `NGSTk.tools.java`). In case no `config_file` argument is passed, all commands will be returned assuming the tool is in the user's $PATH.

#### Parameters:

- `config_file` (`str`):  Path to pipeline yaml config file (optional).
- `pm` (`pypiper.PipelineManager`):  A PipelineManager with which to associate this toolkit instance;that is, essentially a source from which to grab paths to tools, resources, etc.


#### Examples:

```console
    from pypiper.ngstk import NGSTk as tk
    tk = NGSTk()
    tk.samtools_index("sample.bam")
    # returns: samtools index sample.bam

    # Using a configuration file (custom executable location):
    from pypiper.ngstk import NGSTk
    tk = NGSTk("pipeline_config_file.yaml")
    tk.samtools_index("sample.bam")
    # returns: /home/.local/samtools/bin/samtools index sample.bam
```


```python
def __init__(self, config_file=None, pm=None)
```

Initialize self.  See help(type(self)) for accurate signature.



```python
def add_track_to_hub(self, sample_name, track_url, track_hub, colour, five_prime='')
```



```python
def bam2fastq(self, input_bam, output_fastq, output_fastq2=None, unpaired_fastq=None)
```

Create command to convert BAM(s) to FASTQ(s).
#### Parameters:

- `input_bam` (`str`):  Path to sequencing reads file to convert
- `output_fastq` (``):  Path to FASTQ to write
- `output_fastq2` (``):  Path to (R2) FASTQ to write
- `unpaired_fastq` (``):  Path to unpaired FASTQ to write


#### Returns:

- `str`:  Command to convert BAM(s) to FASTQ(s)




```python
def bam_conversions(self, bam_file, depth=True)
```

Sort and index bam files for later use.
#### Parameters:

- `depth` (`bool`):  also calculate coverage over each position




```python
def bam_to_bed(self, input_bam, output_bed)
```



```python
def bam_to_bigwig(self, input_bam, output_bigwig, genome_sizes, genome, tagmented=False, normalize=False, norm_factor=1000)
```

Convert a BAM file to a bigWig file.
#### Parameters:

- `input_bam` (`str`):  path to BAM file to convert
- `output_bigwig` (`str`):  path to which to write file in bigwig format
- `genome_sizes` (`str`):  path to file with chromosome size information
- `genome` (`str`):  name of genomic assembly
- `tagmented` (`bool`):  flag related to read-generating protocol
- `normalize` (`bool`):  whether to normalize coverage
- `norm_factor` (`int`):  number of bases to use for normalization


#### Returns:

- `list[str]`:  sequence of commands to execute




```python
def bam_to_fastq(self, bam_file, out_fastq_pre, paired_end)
```

Build command to convert BAM file to FASTQ file(s) (R1/R2).
#### Parameters:

- `bam_file` (`str`):  path to BAM file with sequencing reads
- `out_fastq_pre` (`str`):  path prefix for output FASTQ file(s)
- `paired_end` (`bool`):  whether the given file contains paired-endor single-end sequencing reads


#### Returns:

- `str`:  file conversion command, ready to run




```python
def bam_to_fastq_awk(self, bam_file, out_fastq_pre, paired_end, zipmode=False)
```

This converts bam file to fastq files, but using awk. As of 2016, this is much faster than the standard way of doing this using Picard, and also much faster than the bedtools implementation as well; however, it does no sanity checks and assumes the reads (for paired data) are all paired (no singletons), in the correct order.
#### Parameters:

- `zipmode` (`bool`):  Should the output be zipped?




```python
def bam_to_fastq_bedtools(self, bam_file, out_fastq_pre, paired_end)
```

Converts bam to fastq; A version using bedtools



```python
def bowtie2_map(self, input_fastq1, output_bam, log, metrics, genome_index, max_insert, cpus, input_fastq2=None)
```



```python
def calc_frip(self, input_bam, input_bed, threads=4)
```

Calculate fraction of reads in peaks.

A file of with a pool of sequencing reads and a file with peak call
regions define the operation that will be performed. Thread count
for samtools can be specified as well.
#### Parameters:

- `input_bam` (`str`):  sequencing reads file
- `input_bed` (`str`):  file with called peak regions
- `threads` (`int`):  number of threads samtools may use


#### Returns:

- `float`:  fraction of reads in peaks defined in given peaks file




```python
def calculate_frip(self, input_bam, input_bed, output, cpus=4)
```



```python
def center_peaks_on_motifs(self, peak_file, genome, window_width, motif_file, output_bed)
```



```python
def check_command(self, command)
```

Check if command can be called.



```python
def check_fastq(self, input_files, output_files, paired_end)
```

Returns a follow sanity-check function to be run after a fastq conversion. Run following a command that will produce the fastq files.

This function will make sure any input files have the same number of reads as the
output files.



```python
def check_trim(self, trimmed_fastq, paired_end, trimmed_fastq_R2=None, fastqc_folder=None)
```

Build function to evaluate read trimming, and optionally run fastqc.

This is useful to construct an argument for the 'follow' parameter of
a PipelineManager's 'run' method.
#### Parameters:

- `trimmed_fastq` (`str`):  Path to trimmed reads file.
- `paired_end` (`bool`):  Whether the processing is being done withpaired-end sequencing data.
- `trimmed_fastq_R2` (`str`):  Path to read 2 file for the paired-end case.
- `fastqc_folder` (`str`):  Path to folder within which to place fastqcoutput files; if unspecified, fastqc will not be run.


#### Returns:

- `callable`:  Function to evaluate read trimming and possibly runfastqc.




```python
def count_concordant(self, aligned_bam)
```

Count only reads that "aligned concordantly exactly 1 time."
#### Parameters:

- `aligned_bam` (`str`):  File for which to count mapped reads.




```python
def count_fail_reads(self, file_name, paired_end)
```

Counts the number of reads that failed platform/vendor quality checks.
#### Parameters:

- `paired_end` (``):  This parameter is ignored; samtools automatically correctly responds dependingon the data in the bamfile. We leave the option here just for consistency, since all the other counting functions require the parameter. This makes it easier to swap counting functions during pipeline development.




```python
def count_flag_reads(self, file_name, flag, paired_end)
```

Counts the number of reads with the specified flag.
#### Parameters:

- `file_name` (`str`):  name of reads file
- `flag` (`str`):  sam flag value to be read
- `paired_end` (`bool`):  This parameter is ignored; samtools automatically correctly responds dependingon the data in the bamfile. We leave the option here just for consistency, since all the other counting functions require the parameter. This makes it easier to swap counting functions during pipeline development.




```python
def count_lines(self, file_name)
```

Uses the command-line utility wc to count the number of lines in a file. For MacOS, must strip leading whitespace from wc.
#### Parameters:

- `file_name` (`str`):  name of file whose lines are to be counted




```python
def count_lines_zip(self, file_name)
```

Uses the command-line utility wc to count the number of lines in a file. For MacOS, must strip leading whitespace from wc. For compressed files.
#### Parameters:

- `file` (``):  file_name




```python
def count_mapped_reads(self, file_name, paired_end)
```

Mapped_reads are not in fastq format, so this one doesn't need to accommodate fastq, and therefore, doesn't require a paired-end parameter because it only uses samtools view. Therefore, it's ok that it has a default parameter, since this is discarded.
#### Parameters:

- `file_name` (`str`):  File for which to count mapped reads.
- `paired_end` (`bool`):  This parameter is ignored; samtools automatically correctly responds dependingon the data in the bamfile. We leave the option here just for consistency, since all the other counting functions require the parameter. This makes it easier to swap counting functions during pipeline development.


#### Returns:

- `int`:  Either return code from samtools view command, or -1 to indicate an error state.




```python
def count_multimapping_reads(self, file_name, paired_end)
```

Counts the number of reads that mapped to multiple locations. Warning: currently, if the alignment software includes the reads at multiple locations, this function will count those more than once. This function is for software that randomly assigns, but flags reads as multimappers.
#### Parameters:

- `file_name` (`str`):  name of reads file
- `paired_end` (``):  This parameter is ignored; samtools automatically correctly responds dependingon the data in the bamfile. We leave the option here just for consistency, since all the other counting functions require the parameter. This makes it easier to swap counting functions during pipeline development.




```python
def count_reads(self, file_name, paired_end)
```

Count reads in a file.

Paired-end reads count as 2 in this function.
For paired-end reads, this function assumes that the reads are split
into 2 files, so it divides line count by 2 instead of 4.
This will thus give an incorrect result if your paired-end fastq files
are in only a single file (you must divide by 2 again).
#### Parameters:

- `file_name` (`str`):  Name/path of file whose reads are to be counted.
- `paired_end` (`bool`):  Whether the file contains paired-end reads.




```python
def count_unique_mapped_reads(self, file_name, paired_end)
```

For a bam or sam file with paired or or single-end reads, returns the number of mapped reads, counting each read only once, even if it appears mapped at multiple locations.
#### Parameters:

- `file_name` (`str`):  name of reads file
- `paired_end` (`bool`):  True/False paired end data


#### Returns:

- `int`:  Number of uniquely mapped reads.




```python
def count_unique_reads(self, file_name, paired_end)
```

Sometimes alignment software puts multiple locations for a single read; if you just count those reads, you will get an inaccurate count. This is _not_ the same as multimapping reads, which may or may not be actually duplicated in the bam file (depending on the alignment software). This function counts each read only once. This accounts for paired end or not for free because pairs have the same read name. In this function, a paired-end read would count as 2 reads.



```python
def count_uniquelymapping_reads(self, file_name, paired_end)
```

Counts the number of reads that mapped to a unique position.
#### Parameters:

- `file_name` (`str`):  name of reads file
- `paired_end` (`bool`):  This parameter is ignored.




```python
def fastqc(self, file, output_dir)
```

Create command to run fastqc on a FASTQ file
#### Parameters:

- `file` (`str`):  Path to file with sequencing reads
- `output_dir` (`str`):  Path to folder in which to place output


#### Returns:

- `str`:  Command with which to run fastqc




```python
def fastqc_rename(self, input_bam, output_dir, sample_name)
```

Create pair of commands to run fastqc and organize files.

The first command returned is the one that actually runs fastqc when
it's executed; the second moves the output files to the output
folder for the sample indicated.
#### Parameters:

- `input_bam` (`str`):  Path to file for which to run fastqc.
- `output_dir` (`str`):  Path to folder in which fastqc output will bewritten, and within which the sample's output folder lives.
- `sample_name` (`str`):  Sample name, which determines subfolder withinoutput_dir for the fastqc files.


#### Returns:

- `list[str]`:  Pair of commands, to run fastqc and then move the files totheir intended destination based on sample name.




```python
def filter_peaks_mappability(self, peaks, alignability, filtered_peaks)
```



```python
def filter_reads(self, input_bam, output_bam, metrics_file, paired=False, cpus=16, Q=30)
```

Remove duplicates, filter for >Q, remove multiple mapping reads. For paired-end reads, keep only proper pairs.



```python
def genome_wide_coverage(self, input_bam, genome_windows, output)
```



```python
def get_chrs_from_bam(self, file_name)
```

Uses samtools to grab the chromosomes from the header that are contained in this bam file.



```python
def get_file_size(self, filenames)
```

Get size of all files in string (space-separated) in megabytes (Mb).
#### Parameters:

- `filenames` (`str`):  a space-separated string of filenames




```python
def get_fragment_sizes(self, bam_file)
```



```python
def get_frip(self, sample)
```

Calculates the fraction of reads in peaks for a given sample.
#### Parameters:

- `sample` (`pipelines.Sample`):  Sample object with "peaks" attribute.




```python
def get_input_ext(self, input_file)
```

Get the extension of the input_file. Assumes you're using either .bam or .fastq/.fq or .fastq.gz/.fq.gz.



```python
def get_mitochondrial_reads(self, bam_file, output, cpus=4)
```



```python
def get_peak_number(self, sample)
```

Counts number of peaks from a sample's peak file.
#### Parameters:

- `sample` (`pipelines.Sample`):  Sample object with "peaks" attribute.




```python
def get_read_type(self, bam_file, n=10)
```

Gets the read type (single, paired) and length of bam file.
#### Parameters:

- `bam_file` (`str`):  Bam file to determine read attributes.
- `n` (`int`):  Number of lines to read from bam file.


#### Returns:

- `str, int`:  tuple of read type and read length




```python
def homer_annotate_pPeaks(self, peak_file, genome, motif_file, output_bed)
```



```python
def homer_find_motifs(self, peak_file, genome, output_dir, size=150, length='8,10,12,14,16', n_motifs=12)
```



```python
def htseq_count(self, input_bam, gtf, output)
```



```python
def index_bam(self, input_bam)
```



```python
def input_to_fastq(self, input_file, sample_name, paired_end, fastq_folder, output_file=None, multiclass=False, zipmode=False)
```

Builds a command to convert input file to fastq, for various inputs.

Takes either .bam, .fastq.gz, or .fastq input and returns
commands that will create the .fastq file, regardless of input type.
This is useful to made your pipeline easily accept any of these input
types seamlessly, standardizing you to fastq which is still the
most common format for adapter trimmers, etc. You can specify you want
output either zipped or not.
Commands will place the output fastq file in given `fastq_folder`.
#### Parameters:

- `input_file` (`str`):  filename of input you want to convert to fastq
- `multiclass` (`bool`):  Are both read1 and read2 included in a singlefile? User should not need to set this; it will be inferred and used in recursive calls, based on number files, and the paired_end arg.
- `zipmode` (`bool`):  Should the output be .fastq.gz? Otherwise, just fastq


#### Returns:

- `str`:  A command (to be run with PipelineManager) that will ensureyour fastq file exists.




```python
def kallisto(self, input_fastq, output_dir, output_bam, transcriptome_index, cpus, input_fastq2=None, size=180, b=200)
```



```python
def link_to_track_hub(self, track_hub_url, file_name, genome)
```



```python
def macs2_call_peaks(self, treatment_bams, output_dir, sample_name, genome, control_bams=None, broad=False, paired=False, pvalue=None, qvalue=None, include_significance=None)
```

Use MACS2 to call peaks.
#### Parameters:

- `treatment_bams` (`str | Iterable[str]`):  Paths to files with data toregard as treatment.
- `output_dir` (`str`):  Path to output folder.
- `sample_name` (`str`):  Name for the sample involved.
- `genome` (`str`):  Name of the genome assembly to use.
- `control_bams` (`str | Iterable[str]`):  Paths to files with data toregard as control
- `broad` (`bool`):  Whether to do broad peak calling.
- `paired` (`bool`):  Whether reads are paired-end
- `pvalue` (`float | NoneType`):  Statistical significance measure topass as --pvalue to peak calling with MACS
- `qvalue` (`float | NoneType`):  Statistical significance measure topass as --qvalue to peak calling with MACS
- `include_significance` (`bool | NoneType`):  Whether to pass astatistical significance argument to peak calling with MACS; if omitted, this will be True if the peak calling is broad or if either p-value or q-value is specified; default significance specification is a p-value of 0.001 if a significance is to be specified but no value is provided for p-value or q-value.


#### Returns:

- `str`:  Command to run.




```python
def macs2_call_peaks_atacseq(self, treatment_bam, output_dir, sample_name, genome)
```



```python
def macs2_plot_model(self, r_peak_model_file, sample_name, output_dir)
```



```python
def make_dir(self, path)
```

Forge path to directory, creating intermediates as needed.
#### Parameters:

- `path` (`str`):  Path to create.




```python
def make_sure_path_exists(self, path)
```

Alias for make_dir



```python
def mark_duplicates(self, aligned_file, out_file, metrics_file, remove_duplicates='True')
```



```python
def merge_bams(self, input_bams, merged_bam, in_sorted='TRUE', tmp_dir=None)
```

Combine multiple files into one.

The tmp_dir parameter is important because on poorly configured
systems, the default can sometimes fill up.
#### Parameters:

- `input_bams` (`Iterable[str]`):  Paths to files to combine
- `merged_bam` (`str`):  Path to which to write combined result.
- `in_sorted` (`bool | str`):  Whether the inputs are sorted
- `tmp_dir` (`str`):  Path to temporary directory.




```python
def merge_bams_samtools(self, input_bams, merged_bam)
```



```python
def merge_fastq(self, inputs, output, run=False, remove_inputs=False)
```

Merge FASTQ files (zipped or not) into one.
#### Parameters:

- `inputs` (`Iterable[str]`):  Collection of paths to files to merge.
- `output` (`str`):  Path to single output file.
- `run` (`bool`):  Whether to run the command.
- `remove_inputs` (`bool`):  Whether to keep the original files.


#### Returns:

- `NoneType | str`:  Null if running the command, otherwise thecommand itself


#### Raises:

- `ValueError`:  Raise ValueError if the call is such thatinputs are to be deleted but command is not run.




```python
def merge_or_link(self, input_args, raw_folder, local_base='sample')
```

Standardizes various input possibilities by converting either .bam, .fastq, or .fastq.gz files into a local file; merging those if multiple files given.
#### Parameters:

- `input_args` (`list`):  This is a list of arguments, each one is aclass of inputs (which can in turn be a string or a list). Typically, input_args is a list with 2 elements: first a list of read1 files; second an (optional!) list of read2 files.
- `raw_folder` (`str`):  Name/path of folder for the merge/link.
- `local_base` (`str`):  Usually the sample name. This (plus fileextension) will be the name of the local file linked (or merged) by this function.




```python
def move_file(self, old, new)
```



```python
def parse_bowtie_stats(self, stats_file)
```

Parses Bowtie2 stats file, returns series with values.
#### Parameters:

- `stats_file` (`str `):  Bowtie2 output file with alignment statistics.




```python
def parse_duplicate_stats(self, stats_file)
```

Parses sambamba markdup output, returns series with values.
#### Parameters:

- `stats_file` (`str`):  sambamba output file with duplicate statistics.




```python
def parse_qc(self, qc_file)
```

Parse phantompeakqualtools (spp) QC table and return quality metrics.
#### Parameters:

- `qc_file` (`str`):  Path to phantompeakqualtools output file, whichcontains sample quality measurements.




```python
def picard_mark_duplicates(self, input_bam, output_bam, metrics_file, temp_dir='.')
```



```python
def plot_atacseq_insert_sizes(self, bam, plot, output_csv, max_insert=1500, smallest_insert=30)
```

Heavy inspiration from here: https://github.com/dbrg77/ATAC/blob/master/ATAC_seq_read_length_curve_fitting.ipynb



```python
def preseq_coverage(self, bam_file, output_prefix)
```



```python
def preseq_curve(self, bam_file, output_prefix)
```



```python
def preseq_extrapolate(self, bam_file, output_prefix)
```



```python
def remove_file(self, file_name)
```



```python
def run_spp(self, input_bam, output, plot, cpus)
```

Run the SPP read peak analysis tool.
#### Parameters:

- `input_bam` (`str`):  Path to reads file
- `output` (`str`):  Path to output file
- `plot` (`str`):  Path to plot file
- `cpus` (`int`):  Number of processors to use


#### Returns:

- `str`:  Command with which to run SPP




```python
def sam_conversions(self, sam_file, depth=True)
```

Convert sam files to bam files, then sort and index them for later use.
#### Parameters:

- `depth` (`bool`):  also calculate coverage over each position




```python
def sambamba_remove_duplicates(self, input_bam, output_bam, cpus=16)
```



```python
def samtools_index(self, bam_file)
```

Index a bam file.



```python
def samtools_view(self, file_name, param, postpend='')
```

Run samtools view, with flexible parameters and post-processing.

This is used internally to implement the various count_reads functions.
#### Parameters:

- `file_name` (`str`):  file_name
- `param` (`str`):  String of parameters to pass to samtools view
- `postpend` (`str`):  String to append to the samtools command;useful to add cut, sort, wc operations to the samtools view output.




```python
def shift_reads(self, input_bam, genome, output_bam)
```



```python
def simple_frip(self, input_bam, input_bed, threads=4)
```



```python
def skewer(self, input_fastq1, output_prefix, output_fastq1, log, cpus, adapters, input_fastq2=None, output_fastq2=None)
```

Create commands with which to run skewer.
#### Parameters:

- `input_fastq1` (`str`):  Path to input (read 1) FASTQ file
- `output_prefix` (`str`):  Prefix for output FASTQ file names
- `output_fastq1` (`str`):  Path to (read 1) output FASTQ file
- `log` (`str`):  Path to file to which to write logging information
- `cpus` (`int | str`):  Number of processing cores to allow
- `adapters` (`str`):  Path to file with sequencing adapters
- `input_fastq2` (`str`):  Path to read 2 input FASTQ file
- `output_fastq2` (`str`):  Path to read 2 output FASTQ file


#### Returns:

- `list[str]`:  Sequence of commands to run to trim reads withskewer and rename files as desired.




```python
def slurm_footer(self)
```



```python
def slurm_header(self, job_name, output, queue='shortq', n_tasks=1, time='10:00:00', cpus_per_task=8, mem_per_cpu=2000, nodes=1, user_mail='', mail_type='end')
```



```python
def slurm_submit_job(self, job_file)
```



```python
def sort_index_bam(self, input_bam, output_bam)
```



```python
def spp_call_peaks(self, treatment_bam, control_bam, treatment_name, control_name, output_dir, broad, cpus, qvalue=None)
```

Build command for R script to call peaks with SPP.
#### Parameters:

- `treatment_bam` (`str`):  Path to file with data for treatment sample.
- `control_bam` (`str`):  Path to file with data for control sample.
- `treatment_name` (`str`):  Name for the treatment sample.
- `control_name` (`str`):  Name for the control sample.
- `output_dir` (`str`):  Path to folder for output.
- `broad` (`str | bool`):  Whether to specify broad peak calling mode.
- `cpus` (`int`):  Number of cores the script may use.
- `qvalue` (`float`):  FDR, as decimal value


#### Returns:

- `str`:  Command to run.




```python
def topHat_map(self, input_fastq, output_dir, genome, transcriptome, cpus)
```



```python
def trimmomatic(self, input_fastq1, output_fastq1, cpus, adapters, log, input_fastq2=None, output_fastq1_unpaired=None, output_fastq2=None, output_fastq2_unpaired=None)
```



```python
def validate_bam(self, input_bam)
```

Wrapper for Picard's ValidateSamFile.
#### Parameters:

- `input_bam` (`str`):  Path to file to validate.


#### Returns:

- `str`:  Command to run for the validation.




```python
def zinba_call_peaks(self, treatment_bed, control_bed, cpus, tagmented=False)
```



```python
def ziptool(self)
```

Returns the command to use for compressing/decompressing.
#### Returns:

- `str`:  Either 'gzip' or 'pigz' if installed and multiple cores







*Version Information: `pypiper` v0.14.1, generated by `lucidoc` v0.4.4*