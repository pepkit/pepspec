# geofetch tutorial for raw data

The [GSE67303 data set](https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE67303) has about 250 mb of data across 4 samples, so it's a quick download for a test case. Let's take a quick peek at the geofetch version:


```bash
geofetch --version
```

    geofetch 0.10.1


To see your CLI options, invoke `geofetch -h`:


```bash
geofetch -h
```

    usage: geofetch [-h] [-V] -i INPUT [-n NAME] [-m METADATA_ROOT]
                    [-u METADATA_FOLDER] [--just-metadata] [-r]
                    [--config-template CONFIG_TEMPLATE]
                    [--pipeline-samples PIPELINE_SAMPLES]
                    [--pipeline-project PIPELINE_PROJECT] [-k SKIP] [--acc-anno]
                    [--discard-soft] [--const-limit-project CONST_LIMIT_PROJECT]
                    [--const-limit-discard CONST_LIMIT_DISCARD]
                    [--attr-limit-truncate ATTR_LIMIT_TRUNCATE] [--add-dotfile]
                    [-p] [--data-source {all,samples,series}] [--filter FILTER]
                    [--filter-size FILTER_SIZE] [-g GEO_FOLDER] [-x]
                    [-b BAM_FOLDER] [-f FQ_FOLDER] [--use-key-subset] [--silent]
                    [--verbosity V] [--logdev]
    
    Automatic GEO and SRA data downloader
    
    optional arguments:
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
                            --metadata-root [Default: Not used (--metadata-root is
                            used by default)]
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
      -k SKIP, --skip SKIP  Skip some accessions. [Default: no skip].
      --acc-anno            Optional: Produce annotation sheets for each
                            accession. Project combined PEP for the whole project
                            won't be produced.
      --discard-soft        Optional: After creation of PEP files, all soft and
                            additional files will be deleted
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


Calling geofetch will do 4 tasks: 

1. download all `.sra` files from `GSE#####` into your SRA folder (wherever you have configured `sratools` to stick data).
2. download all metadata from GEO and SRA and store in your metadata folder.
2. produce a PEP-compatible sample table, `PROJECT_NAME_annotation.csv`, in your metadata folder.
3. produce a PEP-compatible project configuration file, `PROJECT_NAME_config.yaml`, in your metadata folder.

Complete details about geofetch outputs is cataloged in the [metadata outputs reference](../metadata_output.md).

## Download the data

First, create the metadata:


```bash
geofetch -i GSE67303 -n red_algae -m `pwd` --just-metadata
```

    Metadata folder: /home/bnt4me/Virginia/repos/geof2/geofetch/docs_jupyter/red_algae
    Trying GSE67303 (not a file) as accession...
    Skipped 0 accessions. Starting now.
    [38;5;200mProcessing accession 1 of 1: 'GSE67303'[0m
    --2022-07-08 12:39:24--  https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?targ=gse&acc=GSE67303&form=text&view=full
    Resolving www.ncbi.nlm.nih.gov (www.ncbi.nlm.nih.gov)... 2607:f220:41e:4290::110, 130.14.29.110
    Connecting to www.ncbi.nlm.nih.gov (www.ncbi.nlm.nih.gov)|2607:f220:41e:4290::110|:443... connected.
    HTTP request sent, awaiting response... 200 OK
    Length: unspecified [geo/text]
    Saving to: ‘/home/bnt4me/Virginia/repos/geof2/geofetch/docs_jupyter/red_algae/GSE67303_GSE.soft’
    
    /home/bnt4me/Virgin     [ <=>                ]   3.19K  --.-KB/s    in 0s      
    
    2022-07-08 12:39:24 (134 MB/s) - ‘/home/bnt4me/Virginia/repos/geof2/geofetch/docs_jupyter/red_algae/GSE67303_GSE.soft’ saved [3266]
    
    --2022-07-08 12:39:24--  https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?targ=gsm&acc=GSE67303&form=text&view=full
    Resolving www.ncbi.nlm.nih.gov (www.ncbi.nlm.nih.gov)... 2607:f220:41e:4290::110, 130.14.29.110
    Connecting to www.ncbi.nlm.nih.gov (www.ncbi.nlm.nih.gov)|2607:f220:41e:4290::110|:443... connected.
    HTTP request sent, awaiting response... 200 OK
    Length: unspecified [geo/text]
    Saving to: ‘/home/bnt4me/Virginia/repos/geof2/geofetch/docs_jupyter/red_algae/GSE67303_GSM.soft’
    
    /home/bnt4me/Virgin     [ <=>                ]  10.70K  --.-KB/s    in 0.05s   
    
    2022-07-08 12:39:24 (218 KB/s) - ‘/home/bnt4me/Virginia/repos/geof2/geofetch/docs_jupyter/red_algae/GSE67303_GSM.soft’ saved [10956]
    
    Processed 4 samples.
    Found SRA Project accession: SRP056574
    Downloading SRP056574 sra metadata
    Parsing SRA file to download SRR records
    sample_name does not exist, creating new...
    Getting SRR: SRR1930183 (SRX969073)
    Dry run (no raw data will be download)
    sample_name does not exist, creating new...
    Getting SRR: SRR1930184 (SRX969074)
    Dry run (no raw data will be download)
    sample_name does not exist, creating new...
    Getting SRR: SRR1930185 (SRX969075)
    Dry run (no raw data will be download)
    sample_name does not exist, creating new...
    Getting SRR: SRR1930186 (SRX969076)
    Dry run (no raw data will be download)
    Finished processing 1 accession(s)
    Creating complete project annotation sheets and config file...
    Sample annotation sheet: /home/bnt4me/Virginia/repos/geof2/geofetch/docs_jupyter/red_algae/GSE67303_annotation.csv
    Writing: /home/bnt4me/Virginia/repos/geof2/geofetch/docs_jupyter/red_algae/GSE67303_annotation.csv
      Config file: /home/bnt4me/Virginia/repos/geof2/geofetch/docs_jupyter/red_algae/GSE67303_config.yaml


The `-m` parameter specifies to use the current directory, storing the data according to the name (`-n`) parameter. So, we'll now have a `red_alga` subfolder, where the results will be saved. Inside that folder you'll see the output of the command:


```bash
ls red_algae
```

    GSE67303_annotation.csv  GSE67303_GSE.soft  GSE67303_SRA.csv
    GSE67303_config.yaml     GSE67303_GSM.soft


The `.soft` files are the direct output from GEO, which contain all the metadata as stored by GEO, for both the experiment (`_GSE`) and for the individual samples (`_GSM`). Geofetch also produces a `csv` file with the SRA metadata. The filtered version (ending in `_filt`) would contain only the specified subset of the samples if we didn't request them all, but in this case, since we only gave an accession, it is identical to the complete file.

Finally, there are the 2 files that make up the PEP: the `_config.yaml` file and the `_annotation.csv` file. Let's see what's in these files now.


```bash
cat red_algae/GSE67303_config.yaml
```

    # Autogenerated by geofetch
    
    name: GSE67303
    pep_version: 2.1.0
    sample_table: GSE67303_annotation.csv
    subsample_table: null
    
    looper:
      output_dir: GSE67303
      pipeline_interfaces: {pipeline_interfaces}
    
    sample_modifiers:
      append:
        Sample_growth_protocol_ch1: Cyanidioschyzon merolae cells were grown in 2xMA media
        Sample_data_processing: Supplementary_files_format_and_content: Excel spreadsheet includes FPKM values for Darkness and Blue-Light exposed samples with p and q values of cuffdiff output.
        Sample_extract_protocol_ch1: RNA libraries were prepared for sequencing using standard Illumina protocols
        Sample_treatment_protocol_ch1: Cells were exposed to blue-light (15 µmole m-2s-1) for 30 minutes
        SRR_files: SRA
        
      derive:
        attributes: [read1, read2, SRR_files]
        sources:
          SRA: "${SRABAM}/{SRR}.bam"
          FQ: "${SRAFQ}/{SRR}.fastq.gz"
          FQ1: "${SRAFQ}/{SRR}_1.fastq.gz"
          FQ2: "${SRAFQ}/{SRR}_2.fastq.gz"      
      imply:
        - if: 
            organism: "Mus musculus"
          then:
            genome: mm10
        - if: 
            organism: "Homo sapiens"
          then:
            genome: hg38          
        - if: 
            read_type: "PAIRED"
          then:
            read1: FQ1
            read2: FQ2          
        - if: 
            read_type: "SINGLE"
          then:
            read1: FQ1
    
    project_modifiers:
      amend:
        sra_convert:
          looper:
            results_subdir: sra_convert_results
          sample_modifiers:
            append:
              SRR_files: SRA
              pipeline_interfaces: ${CODE}/geofetch/pipeline_interface_convert.yaml
            derive:
              attributes: [read1, read2, SRR_files]
              sources:
                SRA: "${SRARAW}/{SRR}.sra"
                FQ: "${SRAFQ}/{SRR}.fastq.gz"
                FQ1: "${SRAFQ}/{SRR}_1.fastq.gz"
                FQ2: "${SRAFQ}/{SRR}_2.fastq.gz"


There are two important things to note in his file: First, see in the PEP that `sample_table` points to the csv file produced by geofetch. Second, look at the amendment called `sra_convert`. This adds a pipeline interface to the sra conversion pipeline, and adds derived attributes for SRA files and fastq files that rely on environment variables called `$SRARAW` and `$SRAFQ`. These environment variables should point to folders where you store your raw .sra files and the converted fastq files.

Now let's look at the first 100 characters of the csv file:


```bash
cut -c -100 red_algae/GSE67303_annotation.csv
```

    sample_name,protocol,organism,read_type,data_source,SRR,SRX,Sample_title,Sample_geo_accession,Sample
    Cm_BlueLight_Rep1,cDNA,Cyanidioschyzon merolae strain 10D,PAIRED,SRA,SRR1930183,SRX969073,Cm_BlueLig
    Cm_BlueLight_Rep2,cDNA,Cyanidioschyzon merolae strain 10D,PAIRED,SRA,SRR1930184,SRX969074,Cm_BlueLig
    Cm_Darkness_Rep1,cDNA,Cyanidioschyzon merolae strain 10D,PAIRED,SRA,SRR1930185,SRX969075,Cm_Darkness
    Cm_Darkness_Rep2,cDNA,Cyanidioschyzon merolae strain 10D,PAIRED,SRA,SRR1930186,SRX969076,Cm_Darkness


Now let's download the actual data.


```bash
geofetch -i GSE67303 -n red_algae -m `pwd`
```

    Metadata folder: /home/bnt4me/Virginia/repos/geof2/geofetch/docs_jupyter/red_algae
    Trying GSE67303 (not a file) as accession...
    Skipped 0 accessions. Starting now.
    [38;5;200mProcessing accession 1 of 1: 'GSE67303'[0m
    Found previous GSE file: /home/bnt4me/Virginia/repos/geof2/geofetch/docs_jupyter/red_algae/GSE67303_GSE.soft
    Found previous GSM file: /home/bnt4me/Virginia/repos/geof2/geofetch/docs_jupyter/red_algae/GSE67303_GSM.soft
    Processed 4 samples.
    Found SRA Project accession: SRP056574
    Found SRA metadata, opening..
    Parsing SRA file to download SRR records
    sample_name does not exist, creating new...
    Getting SRR: SRR1930183 (SRX969073)
    
    2022-07-08T16:40:20 prefetch.2.11.2: Current preference is set to retrieve SRA Normalized Format files with full base quality scores.
    2022-07-08T16:40:20 prefetch.2.11.2: 1) Downloading 'SRR1930183'...
    2022-07-08T16:40:20 prefetch.2.11.2: SRA Normalized Format file is being retrieved, if this is different from your preference, it may be due to current file availability.
    2022-07-08T16:40:20 prefetch.2.11.2:  Downloading via HTTPS...
    2022-07-08T16:41:28 prefetch.2.11.2:  HTTPS download succeed
    2022-07-08T16:41:28 prefetch.2.11.2:  'SRR1930183' is valid
    2022-07-08T16:41:28 prefetch.2.11.2: 1) 'SRR1930183' was downloaded successfully
    2022-07-08T16:41:28 prefetch.2.11.2: 'SRR1930183' has 0 unresolved dependencies
    sample_name does not exist, creating new...
    Getting SRR: SRR1930184 (SRX969074)
    
    2022-07-08T16:41:39 prefetch.2.11.2: Current preference is set to retrieve SRA Normalized Format files with full base quality scores.
    2022-07-08T16:41:40 prefetch.2.11.2: 1) Downloading 'SRR1930184'...
    2022-07-08T16:41:40 prefetch.2.11.2: SRA Normalized Format file is being retrieved, if this is different from your preference, it may be due to current file availability.
    2022-07-08T16:41:40 prefetch.2.11.2:  Downloading via HTTPS...
    2022-07-08T16:42:43 prefetch.2.11.2:  HTTPS download succeed
    2022-07-08T16:42:43 prefetch.2.11.2:  'SRR1930184' is valid
    2022-07-08T16:42:43 prefetch.2.11.2: 1) 'SRR1930184' was downloaded successfully
    2022-07-08T16:42:43 prefetch.2.11.2: 'SRR1930184' has 0 unresolved dependencies
    sample_name does not exist, creating new...
    Getting SRR: SRR1930185 (SRX969075)
    
    2022-07-08T16:42:54 prefetch.2.11.2: Current preference is set to retrieve SRA Normalized Format files with full base quality scores.
    2022-07-08T16:42:55 prefetch.2.11.2: 1) Downloading 'SRR1930185'...
    2022-07-08T16:42:55 prefetch.2.11.2: SRA Normalized Format file is being retrieved, if this is different from your preference, it may be due to current file availability.
    2022-07-08T16:42:55 prefetch.2.11.2:  Downloading via HTTPS...
    2022-07-08T16:45:00 prefetch.2.11.2:  HTTPS download succeed
    2022-07-08T16:45:00 prefetch.2.11.2:  'SRR1930185' is valid
    2022-07-08T16:45:00 prefetch.2.11.2: 1) 'SRR1930185' was downloaded successfully
    2022-07-08T16:45:00 prefetch.2.11.2: 'SRR1930185' has 0 unresolved dependencies
    sample_name does not exist, creating new...
    Getting SRR: SRR1930186 (SRX969076)
    
    2022-07-08T16:45:11 prefetch.2.11.2: Current preference is set to retrieve SRA Normalized Format files with full base quality scores.
    2022-07-08T16:45:12 prefetch.2.11.2: 1) Downloading 'SRR1930186'...
    2022-07-08T16:45:12 prefetch.2.11.2: SRA Normalized Format file is being retrieved, if this is different from your preference, it may be due to current file availability.
    2022-07-08T16:45:12 prefetch.2.11.2:  Downloading via HTTPS...
    2022-07-08T16:46:49 prefetch.2.11.2:  HTTPS download succeed
    2022-07-08T16:46:49 prefetch.2.11.2:  'SRR1930186' is valid
    2022-07-08T16:46:49 prefetch.2.11.2: 1) 'SRR1930186' was downloaded successfully
    2022-07-08T16:46:49 prefetch.2.11.2: 'SRR1930186' has 0 unresolved dependencies
    Finished processing 1 accession(s)
    Creating complete project annotation sheets and config file...
    Sample annotation sheet: /home/bnt4me/Virginia/repos/geof2/geofetch/docs_jupyter/red_algae/GSE67303_annotation.csv
    Writing: /home/bnt4me/Virginia/repos/geof2/geofetch/docs_jupyter/red_algae/GSE67303_annotation.csv
      Config file: /home/bnt4me/Virginia/repos/geof2/geofetch/docs_jupyter/red_algae/GSE67303_config.yaml



## Finalize the project config and sample annotation

That's basically it! `geofetch` will have produced a general-purpose PEP for you, but you'll need to modify it for whatever purpose you have. For example, one common thing is to link to the pipeline you want to use by adding a `pipeline_interface` to the project config file. You may also need to adjust the `sample_annotation` file to make sure you have the right column names and attributes needed by the pipeline you're using. GEO submitters are notoriously bad at getting the metadata correct.


## Selecting samples to download.

By default, `geofetch` downloads all the data for one accession of interest. If you need more fine-grained control, either because you have multiple accessions or you need a subset of samples within them, you can use the [file-based sample specification](file-specification.md).


## Tips

* Set an environment variable for `$SRABAM` (where `.bam` files will live), and `geofetch` will check to see if you have an already-converted bamfile there before issuing the command to download the `sra` file. In this way, you can delete old `sra` files after conversion and not have to worry about re-downloading them. 

* The config template uses an environment variable `$SRARAW` for where `.sra` files will live. If you set this variable to the same place you instructed `sratoolkit` to download `sra` files, you won't have to tweak the config file. For more information refer to the [`sratools` page](howto-location.md).

You can find a complete example of [using `geofetch` for RNA-seq data](https://github.com/databio/example-projects/tree/master/rna-seq). 

