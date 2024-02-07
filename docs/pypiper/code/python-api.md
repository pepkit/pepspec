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

## <a name="EchoAttMap"></a> Class `EchoAttMap`
An AttMap that returns key/attr if it has no set value.


## <a name="IllegalPipelineDefinitionError"></a> Class `IllegalPipelineDefinitionError`
General pipeline error.


## <a name="IllegalPipelineExecutionError"></a> Class `IllegalPipelineExecutionError`
Represent cases of illogical start/stop run() declarations.


## <a name="MissingCheckpointError"></a> Class `MissingCheckpointError`
Represent case of expected but absent checkpoint file.


```python
def __init__(self, checkpoint, filepath)
```

Initialize self.  See help(type(self)) for accurate signature.



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




## <a name="Pipeline"></a> Class `Pipeline`
Generic pipeline framework.

Note that either a PipelineManager or an output folder path is required
to create the Pipeline. If both are provided, the output folder path is
ignored and that of the PipelineManager that's passed is used instead.

#### Parameters:

- `name` (`str`):  Name for the pipeline; arbitrary, just used for messaging;this is required if and only if a manager is not provided.
- `manager` (`pypiper.PipelineManager`):  The pipeline manager to use forthis pipeline; this is required if and only if name or output folder is not provided.
- `outfolder` (`str`):  Path to main output folder for this pipeline
- `args` (`argparse.Namespace`):  command-line options and arguments for PipelineManager
- `pl_mgr_kwargs` (`Mapping`):  Additional keyword arguments for pipeline manager.


#### Raises:

- `TypeError`:  Either pipeline manager or output folder path must beprovided, and either pipeline manager or name must be provided.
- `ValueError`:  Name of pipeline manager cannot be
- `pypiper.IllegalPipelineDefinitionError`:  Definition of collection ofstages must be non-empty.


```python
def __init__(self, name=None, manager=None, outfolder=None, args=None, **pl_mgr_kwargs)
```

Initialize self.  See help(type(self)) for accurate signature.



```python
def checkpoint(self, stage, msg='')
```

Touch checkpoint file for given stage and provide timestamp message.
#### Parameters:

- `stage` (`pypiper.Stage`):  Stage for which to mark checkpoint
- `msg` (`str`):  Message to embed in timestamp.


#### Returns:

- `bool`:  Whether a checkpoint file was written.




```python
def completed_stage(self, stage)
```

Determine whether the pipeline's completed the stage indicated.
#### Parameters:

- `stage` (`pypiper.Stage`):  Stage to check for completion status.


#### Returns:

- `bool`:  Whether this pipeline's completed the indicated stage.


#### Raises:

- `UnknownStageException`:  If the stage name given is undefinedfor the pipeline, a ValueError arises.




```python
def halt(self, **kwargs)
```

Halt the pipeline



```python
def list_flags(self, only_name=False)
```

Determine the flag files associated with this pipeline.
#### Parameters:

- `only_name` (`bool`):  Whether to return only flag file name(s) (True),or full flag file paths (False); default False (paths)


#### Returns:

- `list[str]`:  flag files associated with this pipeline.




```python
def outfolder(self)
```

Determine the path to the output folder for this pipeline instance.
#### Returns:

- `str`:  Path to output folder for this pipeline instance.




```python
def run(self, start_point=None, stop_before=None, stop_after=None)
```

Run the pipeline, optionally specifying start and/or stop points.
#### Parameters:

- `start_point` (`str`):  Name of stage at which to begin execution.
- `stop_before` (`str`):  Name of stage at which to cease execution;exclusive, i.e. this stage is not run
- `stop_after` (`str`):  Name of stage at which to cease execution;inclusive, i.e. this stage is the last one run


#### Raises:

- `IllegalPipelineExecutionError`:  If both inclusive (stop_after)and exclusive (stop_before) halting points are provided, or if that start stage is the same as or after the stop stage, raise an IllegalPipelineExecutionError.




```python
def stage_names(self)
```

Fetch the pipeline's stage names as specified by the pipeline class author (i.e., not necessarily those that are used for the checkpoint files)
#### Returns:

- `list[str]`:  Sequence of names of this pipeline's defined stages.




```python
def stages(self)
```

Define the names of pipeline processing stages.
#### Returns:

- `Iterable[str]`:  Collection of pipeline stage names.




```python
def wrapup(self)
```

Final mock stage to run after final one finishes.



## <a name="PipelineError"></a> Class `PipelineError`
General pipeline error.


## <a name="PipelineHalt"></a> Class `PipelineHalt`
Execution-stopping exception for halting a pipeline.

This is useful for stopping execution of a truly script-like pipeline.
That is, a pipeline that doesn't bundle/define stages or wrap run() calls
in functions. In this case, we want to be able to stop the Python process
as it chugs through a pipeline script, and we can do that by having a
PipelineManager's halt method raise this exception.


```python
def __init__(self, checkpoint=None, finished=None)
```

Initialize self.  See help(type(self)) for accurate signature.



## <a name="PipelineManager"></a> Class `PipelineManager`
Base class for instantiating a PipelineManager object, the main class of Pypiper.

#### Parameters:

- `name` (`str`):  Choose a name for your pipeline;it's used to name the output files, flags, etc.
- `outfolder` (`str`):  Folder in which to store the results.
- `args` (`argparse.Namespace`):  Optional args object from ArgumentParser;Pypiper will simply record these arguments from your script
- `multi` (`bool`):  Enables running multiple pipelines in one scriptor for interactive use. It simply disables the tee of the output, so you won't get output logged to a file.
- `dirty` (`bool`):  Overrides the pipeline's clean_add()manual parameters, to *never* clean up intermediate files automatically. Useful for debugging; all cleanup files are added to manual cleanup script.
- `recover` (`bool`):  Specify recover mode, to overwrite lock files.If pypiper encounters a locked target, it will ignore the lock and recompute this step. Useful to restart a failed pipeline.
- `new_start` (`bool`):  start over and run every command even if output exists
- `force_follow` (`bool`):  Force run all follow functionseven if  the preceding command is not run. By default, following functions  are only run if the preceding command is run.
- `cores` (`int`):  number of processors to use, default 1
- `mem` (`str`):  amount of memory to use. Default units are megabytes unlessspecified using the suffix [K|M|G|T]."
- `config_file` (`str`):  path to pipeline configuration file, optional
- `output_parent` (`str`):  path to folder in which output folder will live
- `overwrite_checkpoints` (`bool`):  Whether to override the stage-skippinglogic provided by the checkpointing system. This is useful if the calls to this manager's run() method will be coming from a class that implements pypiper.Pipeline, as such a class will handle checkpointing logic automatically, and will set this to True to protect from a case in which a restart begins upstream of a stage for which a checkpoint file already exists, but that depends on the upstream stage and thus should be rerun if it's "parent" is rerun.


#### Raises:

- `TypeError`:  if start or stop point(s) are provided both directly andvia args namespace, or if both stopping types (exclusive/prospective and inclusive/retrospective) are provided.


```python
def __init__(self, name, outfolder, version=None, args=None, multi=False, dirty=False, recover=False, new_start=False, force_follow=False, cores=1, mem='1000M', config_file=None, output_parent=None, overwrite_checkpoints=False, logger_kwargs=None, pipestat_project_name=None, pipestat_sample_name=None, pipestat_schema=None, pipestat_results_file=None, pipestat_config=None, pipestat_result_formatter=None, **kwargs)
```

Initialize self.  See help(type(self)) for accurate signature.



```python
def callprint(self, cmd, shell=None, lock_file=None, nofail=False, container=None)
```

Prints the command, and then executes it, then prints the memory use and return code of the command.

Uses python's subprocess.Popen() to execute the given command. The shell argument is simply
passed along to Popen(). You should use shell=False (default) where possible, because this enables memory
profiling. You should use shell=True if you require shell functions like redirects (>) or stars (*), but this
will prevent the script from monitoring memory use. The pipes (|) will be used to split the command into
subprocesses run within python, so the memory profiling is possible.
cmd can also be a series (a dict object) of multiple commands, which will be run in succession.
#### Parameters:

- `cmd` (`str | Iterable[str]`):  Bash command(s) to be run.
- `lock_file` (`str`):  a lock file name
- `nofail` (`bool`):  FalseNofail can be used to implement non-essential parts of the pipeline; if these processes fail, they will not cause the pipeline to bail out.
- `shell` (`bool`):  None (will tryto determine based on the command)
- `container` (``):  Named Docker container in which to execute.
- `container` (``):  str




```python
def checkprint(self, cmd, shell=None, nofail=False)
```

Just like callprint, but checks output -- so you can get a variable in python corresponding to the return value of the command you call. This is equivalent to running subprocess.check_output() instead of subprocess.call().
#### Parameters:

- `cmd` (`str | Iterable[str]`):  Bash command(s) to be run.
- `shell` (`bool | str`):  If command requires should be run in its own shell. Optional.Default: "guess" -- `run()` will try to guess if the command should be run in a shell (based on the presence of a pipe (|) or redirect (>), To force a process to run as a direct subprocess, set `shell` to False; to force a shell, set True.
- `nofail` (`bool`):  FalseNofail can be used to implement non-essential parts of the pipeline; if these processes fail, they will not cause the pipeline to bail out.


#### Returns:

- `str`:  text output by the executed subprocess (check_output)




```python
def clean_add(self, regex, conditional=False, manual=False)
```

Add files (or regexs) to a cleanup list, to delete when this pipeline completes successfully. When making a call with run that produces intermediate files that should be deleted after the pipeline completes, you flag these files for deletion with this command. Files added with clean_add will only be deleted upon success of the pipeline.
#### Parameters:

- `regex` (`str`):   A unix-style regular expression that matches files to delete(can also be a file name).
- `conditional` (`bool`):  True means the files will only be deleted if no otherpipelines are currently running; otherwise they are added to a manual cleanup script called {pipeline_name}_cleanup.sh
- `manual` (`bool`):  True means the files will just be added to a manual cleanup script.




```python
def complete(self)
```

Stop a completely finished pipeline.



```python
def critical(self, msg, *args, **kwargs)
```



```python
def debug(self, msg, *args, **kwargs)
```



```python
def error(self, msg, *args, **kwargs)
```



```python
def fail_pipeline(self, exc: Exception, dynamic_recover: bool=False)
```

If the pipeline does not complete, this function will stop the pipeline gracefully. It sets the status flag to failed and skips the normal success completion procedure.
#### Parameters:

- `exc` (`Exception`):  Exception to raise.
- `dynamic_recover` (`bool`):  Whether to recover e.g. for job termination.




```python
def fatal(self, msg, *args, **kwargs)
```



```python
def get_container(self, image, mounts)
```



```python
def get_elapsed_time(self)
```

Parse the pipeline profile file, collect the unique and last duplicated runtimes and sum them up. In case the profile is not found, an estimate is calculated (which is correct only in case the pipeline was not rerun)
#### Returns:

- `int`:  sum of runtimes in seconds




```python
def get_stat(self, key)
```

Returns a stat that was previously reported. This is necessary for reporting new stats that are derived from two stats, one of which may have been reported by an earlier run. For example, if you first use report_result to report (number of trimmed reads), and then in a later stage want to report alignment rate, then this second stat (alignment rate) will require knowing the first stat (number of trimmed reads); however, that may not have been calculated in the current pipeline run, so we must retrieve it from the stats.yaml output file. This command will retrieve such previously reported stats if they were not already calculated in the current pipeline run.
#### Parameters:

- `key` (``):  key of stat to retrieve




```python
def halt(self, checkpoint=None, finished=False, raise_error=True)
```

Stop the pipeline before completion point.
#### Parameters:

- `checkpoint` (`str`):  Name of stage just reached or just completed.
- `finished` (`bool`):  Whether the indicated stage was just finished(True), or just reached (False)
- `raise_error` (`bool`):  Whether to raise an exception to trulyhalt execution.




```python
def halted(self)
```

Is the managed pipeline in a paused/halted state?
#### Returns:

- `bool`:  Whether the managed pipeline is in a paused/halted state.




```python
def info(self, msg, *args, **kwargs)
```



```python
def make_sure_path_exists(path)
```

Creates all directories in a path if it does not exist.
#### Parameters:

- `path` (`str`):  Path to create.


#### Raises:

- `Exception`:  if the path creation attempt hits an error witha code indicating a cause other than pre-existence.




```python
def pipestat(self)
```

`pipestat.PipestatManager` object to use for pipeline results reporting and status management

Depending on the object configuration it can report to
a YAML-formatted file or PostgreSQL database. Please refer to pipestat
documentation for more details: http://pipestat.databio.org/
#### Returns:

- `pipestat.PipestatManager`:  object to use for results reporting




```python
def process_counter(self)
```

Increments process counter with regard to the follow state: if currently executed command is a follow function of another one, the counter is not incremented.
#### Returns:

- `str | int`:  current counter state, a number if the counter has beed incremented or a numberof the previous process plus "f" otherwise




```python
def remove_container(self, container)
```



```python
def report_object(self, key, filename, anchor_text=None, anchor_image=None, annotation=None, nolog=False, result_formatter=None, force_overwrite=False)
```

Writes a key:value pair to self.pipeline_stats_file. Note: this function will be deprecated. Using report_result is recommended.
#### Parameters:

- `key` (`str`):  name (key) of the object
- `filename` (`str`):  relative path to the file (relative to parentoutput dir)
- `anchor_text` (`str`):  text used as the link anchor test or caption torefer to the object. If not provided, defaults to the key.
- `anchor_image` (`str`):  a path to an HTML-displayable image thumbnail(so, .png or .jpg, for example). If a path, the path should be relative to the parent output dir.
- `annotation` (`str`):  By default, the figures will be annotated withthe pipeline name, so you can tell which pipeline records which figures. If you want, you can change this.
- `nolog` (`bool`):  Turn on this flag to NOT print this result in thelogfile. Use sparingly in case you will be printing the result in a different format.
- `result_formatter` (`str`):  function for formatting via pipestat backend
- `force_overwrite` (`bool`):  overwrite results if they already exist?


#### Returns:

- `str reported_result`:  the reported result is returned as a list of formatted strings.




```python
def report_result(self, key, value, nolog=False, result_formatter=None, force_overwrite=False)
```

Writes a key:value pair to self.pipeline_stats_file.
#### Parameters:

- `key` (`str`):  name (key) of the stat
- `value` (`dict`):  value of the stat to report.
- `nolog` (`bool`):  Turn on this flag to NOT print this result in thelogfile. Use sparingly in case you will be printing the result in a different format.
- `result_formatter` (`str`):  function for formatting via pipestat backend
- `force_overwrite` (`bool`):  overwrite results if they already exist?


#### Returns:

- `str reported_result`:  the reported result is returned as a list of formatted strings.




```python
def run(self, cmd, target=None, lock_name=None, shell=None, nofail=False, clean=False, follow=None, container=None, default_return_code=0)
```

The primary workhorse function of PipelineManager, this runs a command.

This is the command  execution function, which enforces
race-free file-locking, enables restartability, and multiple pipelines
can produce/use the same files. The function will wait for the file
lock if it exists, and not produce new output (by default) if the
target output file already exists. If the output is to be created,
it will first create a lock file to prevent other calls to run
(for example, in parallel pipelines) from touching the file while it
is being created. It also records the memory of the process and
provides some logging output.
#### Parameters:

- `cmd` (`str | list[str]`):  Shell command(s) to be run.
- `target` (`str | Sequence[str]`):  Output file(s) to produce, optional.If all target files exist, the command will not be run. If no target is given, a lock_name must be provided.
- `lock_name` (`str`):  Name of lock file. Optional.
- `shell` (`bool`):  If command requires should be run in its own shell.Optional. Default: None --will try to determine whether the command requires a shell.
- `nofail` (`bool`):  Whether the pipeline proceed past a nonzero return froma process, default False; nofail can be used to implement non-essential parts of the pipeline; if a 'nofail' command fails, the pipeline is free to continue execution.
- `clean` (`bool`):  True means the target file will be automatically addedto an auto cleanup list. Optional.
- `follow` (`callable`):  Function to call after executing (each) command.
- `container` (`str`):  Name for Docker container in which to run commands.
- `default_return_code` (`Any`):  Return code to use, might be used to discriminatebetween runs that did not execute any commands and runs that did.


#### Returns:

- `int`:  Return code of process. If a list of commands is passed,this is the maximum of all return codes for all commands.




```python
def start_pipeline(self, args=None, multi=False)
```

Initialize setup. Do some setup, like tee output, print some diagnostics, create temp files. You provide only the output directory (used for pipeline stats, log, and status flag files).



```python
def stop_pipeline(self, status='completed')
```

Terminate the pipeline.

This is the "healthy" pipeline completion function.
The normal pipeline completion function, to be run by the pipeline
at the end of the script. It sets status flag to completed and records
some time and memory statistics to the log file.



```python
def time_elapsed(time_since)
```

Returns the number of seconds that have elapsed since the time_since parameter.
#### Parameters:

- `time_since` (`float`):  Time as a float given by time.time().




```python
def timestamp(self, message='', checkpoint=None, finished=False, raise_error=True)
```

Print message, time, and time elapsed, perhaps creating checkpoint.

This prints your given message, along with the current time, and time
elapsed since the previous timestamp() call.  If you specify a
HEADING by beginning the message with "###", it surrounds the message
with newlines for easier readability in the log file. If a checkpoint
is designated, an empty file is created corresponding to the name
given. Depending on how this manager's been configured, the value of
the checkpoint, and whether this timestamp indicates initiation or
completion of a group of pipeline steps, this call may stop the
pipeline's execution.
#### Parameters:

- `message` (`str`):  Message to timestamp.
- `checkpoint` (`str`):  Name of checkpoint; this tends to be somethingthat reflects the processing logic about to be or having just been completed. Provision of an argument to this parameter means that a checkpoint file will be created, facilitating arbitrary starting and stopping point for the pipeline as desired.
- `finished` (`bool`):  Whether this call represents the completion of aconceptual unit of a pipeline's processing
- `raise_error` (``):  Whether to raise exception ifcheckpoint or current state indicates that a halt should occur.




```python
def warning(self, msg, *args, **kwargs)
```



## <a name="Stage"></a> Class `Stage`
Single stage/phase of a pipeline; a logical processing "unit". A stage is a collection of commands that is checkpointed.


```python
def __init__(self, func, f_args=None, f_kwargs=None, name=None, checkpoint=True)
```

A function, perhaps with arguments, defines the stage.
#### Parameters:

- `func` (`callable`):  The processing logic that defines the stage
- `f_args` (`tuple`):  Positional arguments for func
- `f_kwargs` (`dict`):  Keyword arguments for func
- `name` (`str`):  name for the phase/stage
- `func` (`callable`):  Object that defines how the stage will execute.




```python
def checkpoint_name(self)
```

Determine the checkpoint name for this Stage.
#### Returns:

- `str | NoneType`:  Checkpoint name for this stage; null if thisStage is designated as a non-checkpoint.




```python
def run(self, *args, **kwargs)
```

Alternate form for direct call; execute stage.



## <a name="SubprocessError"></a> Class `SubprocessError`
Common base class for all non-exit exceptions.


## <a name="UnknownPipelineStageError"></a> Class `UnknownPipelineStageError`
Triggered by use of unknown/undefined name for a pipeline stage.

#### Parameters:

- `stage_name` (`str`):  Name of the stage triggering the exception.
- `pipeline` (`pypiper.Pipeline`):  Pipeline for which the stage is unknown/undefined.


```python
def __init__(self, stage_name, pipeline=None)
```

Initialize self.  See help(type(self)) for accurate signature.



## <a name="UnsupportedFiletypeException"></a> Class `UnsupportedFiletypeException`
Restrict filetype domain.


```python
def add_logging_options(parser)
```

Augment a CLI argument parser with this package's logging options.
#### Parameters:

- `parser` (`argparse.ArgumentParser`):  CLI options and argument parser toaugment with logging options.


#### Returns:

- `argparse.ArgumentParser`:  the input argument, supplemented with thispackage's logging options.




```python
def add_pypiper_args(parser, groups=('pypiper',), args=None, required=None, all_args=False)
```

Use this to add standardized pypiper arguments to your python pipeline.

There are two ways to use `add_pypiper_args`: by specifying argument groups,
or by specifying individual arguments. Specifying argument groups will add
multiple arguments to your parser; these convenient argument groupings
make it easy to add arguments to certain types of pipeline. For example,
to make a looper-compatible pipeline, use `groups = ["pypiper", "looper"]`.
#### Parameters:

- `parser` (`argparse.ArgumentParser`):  ArgumentParser object from a pipeline
- `groups` (`str | Iterable[str]`):  Adds arguments belong to specified groupof args. Options: pypiper, config, looper, resources, common, ngs, all.
- `args` (`str | Iterable[str]`):  You may specify a list of specific arguments one by one.
- `required` (`Iterable[str]`):  Arguments to be flagged as 'required' by argparse.
- `all_args` (`bool`):  Whether to include all of pypiper's arguments defined here.


#### Returns:

- `argparse.ArgumentParser`:  A new ArgumentParser object, with selectedpypiper arguments added




```python
def build_command(chunks)
```

Create a command from various parts.

The parts provided may include a base, flags, option-bound arguments, and
positional arguments. Each element must be either a string or a two-tuple.
Raw strings are interpreted as either the command base, a pre-joined
pair (or multiple pairs) of option and argument, a series of positional
arguments, or a combination of those elements. The only modification they
undergo is trimming of any space characters from each end.
#### Parameters:

- `chunks` (`Iterable[str | (str, str | NoneType)]`):  the collection of thecommand components to interpret, modify, and join to create a single meaningful command


#### Returns:

- `str`:  the single meaningful command built from the given components


#### Raises:

- `ValueError`:  if no command parts are provided




```python
def check_all_commands(cmds, get_bad_result=<function <lambda> at 0x7f2b0d6c50d0>, handle=None)
```

Determine whether all commands are callable
#### Parameters:

- `cmds` (`Iterable[str] | str`):  collection of commands to check forcallability
- `get_bad_result` (`function(Iterable[(str, str)]) -> object`):  how tocreate result when at least one command is uncallable
- `handle` (`function(object) -> object`):  how to handle with result offailed check


#### Returns:

- `bool`:  whether all commands given appear callable


#### Raises:

- `TypeError`:  if error handler is provided but isn't callable orisn't a single-argument function




```python
def determine_uncallable(commands, transformations=((<function <lambda> at 0x7f2b0d6c51f0>, <function <lambda> at 0x7f2b0d6c5280>),), accumulate=False)
```

Determine which commands are not callable.
#### Parameters:

- `commands` (`Iterable[str] | str`):  commands to check for callability
- `transformations` (`Iterable[(function(str) -> bool, function(str) -> str)]`): pairs in which first element is a predicate and second is a transformation to apply to the input if the predicate is satisfied
- `accumulate` (`bool`):  whether to accumulate transformations (more thanone possible per command)


#### Returns:

- `list[(str, str)]`:  collection of commands that appear uncallable;each element is a pair in which the first element is the original 'command' and the second is what was actually assessed for callability.


#### Raises:

- `TypeError`:  if transformations are provided but are argument is astring or is non-Iterable
- `Exception`:  if accumulation of transformation is False but thecollection of transformations is unordered




```python
def get_first_value(param, param_pools, on_missing=None, error=True)
```

Get the value for a particular parameter from the first pool in the provided priority list of parameter pools.
#### Parameters:

- `param` (`str`):  Name of parameter for which to determine/fetch value.
- `param_pools` (`Sequence[Mapping[str, object]]`):  Ordered (priority)collection of mapping from parameter name to value; this should be ordered according to descending priority.
- `on_missing` (`object | function(str) -> object`):  default value oraction to take if the requested parameter is missing from all of the pools. If a callable, it should return a value when passed the requested parameter as the one and only argument.
- `error` (`bool`):  Whether to raise an error if the requested parameteris not mapped to a value AND there's no value or strategy provided with 'on_missing' with which to handle the case of a request for an unmapped parameter.


#### Returns:

- `object`:  Value to which the requested parameter first mapped inthe (descending) priority collection of parameter 'pools,' or a value explicitly defined or derived with 'on_missing.'


#### Raises:

- `KeyError`:  If the requested parameter is unmapped in all of theprovided pools, and the argument to the 'error' parameter evaluates to True.




```python
def head(obj)
```

Facilitate syntactic uniformity for notion of "object-or-first-item."
#### Parameters:

- `obj` (`object | Iterable[object]`):  single item or collection of items.


#### Returns:

- `obj`:  object itself if non-Iterable, otherwise the first elementif one exists


#### Raises:

- `ValueError`:  if the given object is an empty Iterable




```python
def is_fastq(file_name)
```

Determine whether indicated file appears to be in FASTQ format.
#### Parameters:

- `file_name` (`str`):  Name/path of file to check as FASTQ.


#### Returns:

- `bool`:  Whether indicated file appears to be in FASTQ format, zippedor unzipped.




```python
def is_gzipped_fastq(file_name)
```

Determine whether indicated file appears to be a gzipped FASTQ.
#### Parameters:

- `file_name` (`str`):  Name/path of file to check as gzipped FASTQ.


#### Returns:

- `bool`:  Whether indicated file appears to be in gzipped FASTQ format.




```python
def is_sam_or_bam(file_name)
```

Determine whether a file appears to be in a SAM format.
#### Parameters:

- `file_name` (`str`):  Name/path of file to check as SAM-formatted.


#### Returns:

- `bool`:  Whether file appears to be SAM-formatted




```python
def load_yaml(filepath)
```

Load a yaml file into a python dict



```python
def logger_via_cli(opts, **kwargs)
```

Build and initialize logger from CLI specification.
#### Parameters:

- `opts` (`argparse.Namespace`):  parse of command-line interface
- `kwargs` (``):  keyword arguments to pass along to underlying logmuse function


#### Returns:

- `logging.Logger`:  newly created and configured logger




```python
def result_formatter_markdown(pipeline_name, record_identifier, res_id, value) -> str
```

Returns Markdown formatted value as string

# Pipeline_name and record_identifier should be kept because pipestat needs it






*Version Information: `pypiper` v0.14.0a1, generated by `lucidoc` v0.4.3*