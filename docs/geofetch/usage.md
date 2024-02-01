# <img src="./img/geofetch_logo.svg" class="img-header">  usage reference

`geofetch` command-line usage instructions:



`geofetch --help`
```{console}
usage: geofetch [<args>]

The example how to use geofetch (to download GSE573030 just metadata):
    geofetch -i GSE67303 -m <folder> --just-metadata

To download all processed data of GSE57303:
    geofetch -i GSE67303 --processed --geo-folder <folder> -m <folder>

Automatic GEO and SRA data downloader

options:
  -h, --help            show this help message and exit
  -V, --version         show program's version number and exit
  -i INPUT, --input INPUT
                        required: a GEO (GSE) accession, or a file with a list
                        of GSE numbers
  -n NAME, --name NAME  Specify a project name. Defaults to GSE number
  -m METADATA_ROOT, --metadata-root METADATA_ROOT
                        Specify a parent folder location to store metadata.
                        The project name will be added as a subfolder
                        [Default: $SRAMETA:]
  -u METADATA_FOLDER, --metadata-folder METADATA_FOLDER
                        Specify an absolute folder location to store metadata.
                        No subfolder will be added. Overrides value of
                        --metadata-root.
  --just-metadata       If set, don't actually run downloads, just create
                        metadata
  -r, --refresh-metadata
                        If set, re-download metadata even if it exists.
  --config-template CONFIG_TEMPLATE
                        Project config yaml file template.
  --pipeline-samples PIPELINE_SAMPLES
                        Optional: Specify one or more filepaths to SAMPLES
                        pipeline interface yaml files. These will be added to
                        the project config file to make it immediately
                        compatible with looper. [Default: null]
  --pipeline-project PIPELINE_PROJECT
                        Optional: Specify one or more filepaths to PROJECT
                        pipeline interface yaml files. These will be added to
                        the project config file to make it immediately
                        compatible with looper. [Default: null]
  --disable-progressbar
                        Optional: Disable progressbar
  -k SKIP, --skip SKIP  Skip some accessions. [Default: no skip].
  --acc-anno            Optional: Produce annotation sheets for each
                        accession. Project combined PEP for the whole project
                        won't be produced.
  --discard-soft        Optional: After creation of PEP files, all .soft files
                        will be deleted
  --const-limit-project CONST_LIMIT_PROJECT
                        Optional: Limit of the number of the constant sample
                        characters that should not be in project yaml.
                        [Default: 50]
  --const-limit-discard CONST_LIMIT_DISCARD
                        Optional: Limit of the number of the constant sample
                        characters that should not be discarded [Default: 250]
  --attr-limit-truncate ATTR_LIMIT_TRUNCATE
                        Optional: Limit of the number of sample characters.Any
                        attribute with more than X characters will truncate to
                        the first X, where X is a number of characters
                        [Default: 500]
  --add-dotfile         Optional: Add .pep.yaml file that points .yaml PEP
                        file
  --max-soft-size MAX_SOFT_SIZE
                        Optional: Max size of soft file. [Default: 1GB].
                        Supported input formats : 12B, 12KB, 12MB, 12GB.
  --max-prefetch-size MAX_PREFETCH_SIZE
                        Argument to pass to prefetch program's --max-size
                        option, if prefetch will be used in this run of
                        geofetch; for reference: https://github.com/ncbi/sra-
                        tools/wiki/08.-prefetch-and-fasterq-dump#check-the-
                        maximum-size-limit-of-the-prefetch-tool
  --silent              Silence logging. Overrides verbosity.
  --verbosity V         Set logging level (1-5 or logging module level name)
  --logdev              Expand content of logging message format.

processed:
  -p, --processed       Download processed data [Default: download raw data].
  --data-source {all,samples,series}
                        Optional: Specifies the source of data on the GEO
                        record to retrieve processed data, which may be
                        attached to the collective series entity, or to
                        individual samples. Allowable values are: samples,
                        series or both (all). Ignored unless 'processed' flag
                        is set. [Default: samples]
  --filter FILTER       Optional: Filter regex for processed filenames
                        [Default: None].Ignored unless 'processed' flag is
                        set.
  --filter-size FILTER_SIZE
                        Optional: Filter size for processed files that are
                        stored as sample repository [Default: None]. Works
                        only for sample data. Supported input formats : 12B,
                        12KB, 12MB, 12GB. Ignored unless 'processed' flag is
                        set.
  -g GEO_FOLDER, --geo-folder GEO_FOLDER
                        Optional: Specify a location to store processed GEO
                        files. Ignored unless 'processed' flag is
                        set.[Default: $GEODATA:]

raw:
  -x, --split-experiments
                        Split SRR runs into individual samples. By default,
                        SRX experiments with multiple SRR Runs will have a
                        single entry in the annotation table, with each run as
                        a separate row in the subannotation table. This
                        setting instead treats each run as a separate sample
  -b BAM_FOLDER, --bam-folder BAM_FOLDER
                        Optional: Specify folder of bam files. Geofetch will
                        not download sra files when corresponding bam files
                        already exist. [Default: $SRABAM:]
  -f FQ_FOLDER, --fq-folder FQ_FOLDER
                        Optional: Specify folder of fastq files. Geofetch will
                        not download sra files when corresponding fastq files
                        already exist. [Default: $SRAFQ:]
  --use-key-subset      Use just the keys defined in this module when writing
                        out metadata.
  --add-convert-modifier
                        Add looper SRA convert modifier to config file.
```
