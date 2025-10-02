# `eido` command line usage

To use the command line application one just needs a path to a project configuration file. It is a positional argument in the `eido` command.

For this tutorial, let's grab a PEP from a public example repository that describes a few PRO-seq test samples:


```bash
rm -rf ppqc
git clone https://github.com/databio/ppqc.git --branch cfg2
```

    Cloning into 'ppqc'...
    remote: Enumerating objects: 154, done.[K
    remote: Counting objects: 100% (20/20), done.[K
    remote: Compressing objects: 100% (15/15), done.[K
    remote: Total 154 (delta 7), reused 17 (delta 5), pack-reused 134[K
    Receiving objects: 100% (154/154), 81.69 KiB | 3.27 MiB/s, done.
    Resolving deltas: 100% (82/82), done.



```bash
cd ppqc
export DATA=$HOME
export SRAFQ=$HOME
```

## PEP inspection

First, let's use `eido inspect` to inspect a PEP. 

 - To inspect the entire `Project` object just provide the path to the project configuration file.


```bash
eido inspect peppro_paper.yaml
```

    Project 'PEPPRO' (peppro_paper.yaml)
    47 samples (showing first 20): K562_PRO-seq_02, K562_PRO-seq_04, K562_PRO-seq_06, K562_PRO-seq_08, K562_PRO-seq_10, K562_PRO-seq_20, K562_PRO-seq_30, K562_PRO-seq_40, K562_PRO-seq_50, K562_PRO-seq_60, K562_PRO-seq_70, K562_PRO-seq_80, K562_PRO-seq_90, K562_PRO-seq_100, K562_RNA-seq_0, K562_RNA-seq_10, K562_RNA-seq_20, K562_RNA-seq_30, K562_RNA-seq_40, K562_RNA-seq_50
    Sections: name, pep_version, sample_table, looper, sample_modifiers


 - To inspect a specific sample, one needs to provide the sample name (via `-n`/`--sample-name` optional argument)


```bash
eido inspect peppro_paper.yaml -n K562_PRO-seq K562_RNA-seq_10
```

    Sample 'K562_RNA-seq_10' in Project (peppro_paper.yaml)
    
    sample_name:         K562_RNA-seq_10
    sample_desc:         90% K562 PRO-seq + 10% K562 RNA-seq
    treatment:           70M total reads
    protocol:            PRO
    organism:            human
    read_type:           SINGLE
    umi_len:             0
    read1:               /Users/mstolarczyk/K562_10pctRNA.fastq.gz
    srr:                 K562_10pctRNA
    pipeline_interfaces: $CODE/peppro/sample_pipeline_interface.yaml
    genome:              hg38
    
    ...                (showing first 10)
    
    


## PEP validation

Next, let's use `eido` to validate this project against the generic PEP schema. You just need to provide a path to the project config file and schema as an input.


```bash
eido validate peppro_paper.yaml -s http://schema.databio.org/pep/2.0.0.yaml -e
```

    Validation successful


Any PEP should validate against that schema, which describes generic PEP format. We can go one step further and validate it against the PEPPRO schema, which describes Proseq projects specifically for this pipeline:


```bash
eido validate peppro_paper.yaml -s http://schema.databio.org/pipelines/ProseqPEP.yaml
```

    Validation successful


This project would *not* validate against a different pipeline's schema.

Following `jsonschema`, `eido` produces comprehensive error messages that include the objects that did not pass validation. When validating PEPs that include lots of samples one can use option `-e`/`--exclude-case` to limit the error output just to the human readable message. This is the option used in the example below:


```bash
eido validate peppro_paper.yaml -s http://schema.databio.org/pipelines/bedmaker.yaml -e
```

    Traceback (most recent call last):
      File "/usr/local/bin/eido", line 8, in <module>
        sys.exit(main())
      File "/usr/local/lib/python3.9/site-packages/eido/cli.py", line 89, in main
        validate_project(p, args.schema, args.exclude_case)
      File "/usr/local/lib/python3.9/site-packages/eido/validation.py", line 45, in validate_project
        _validate_object(project_dict, preprocess_schema(schema_dict), exclude_case)
      File "/usr/local/lib/python3.9/site-packages/eido/validation.py", line 30, in _validate_object
        raise jsonschema.exceptions.ValidationError(e.message)
    jsonschema.exceptions.ValidationError: 'input_file_path' is a required property




Optionally, to validate just the config part of the PEP or a specific sample, `-n`/`--sample-name` or `-c`/`--just-config` arguments should be used, respectively. Please refer to the help for more details:


```bash
eido validate -h
```

    usage: eido validate [-h] -s S [-e] [-n S | -c] PEP
    
    Validate the PEP or its components.
    
    positional arguments:
      PEP                   Path to a PEP configuration file in yaml format.
    
    optional arguments:
      -h, --help            show this help message and exit
      -s S, --schema S      Path to a PEP schema file in yaml format.
      -e, --exclude-case    Whether to exclude the validation case from an error.
                            Only the human readable message explaining the error
                            will be raised. Useful when validating large PEPs.
      -n S, --sample-name S
                            Name or index of the sample to validate. Only this
                            sample will be validated.
      -c, --just-config     Whether samples should be excluded from the
                            validation.


## PEP conversion

Let's use `eido convert` command to convert PEPs to a variety of different formats. `eido` supports a plugin system, which can be used by other tool developers to create Python plugin functions that save PEPs in a desired format. Please refer to the documentation for more details. For now let's focus on a couple of plugins that are built-in in `eido`.

To see what plugins are currently available in your Python environment call:


```bash
eido filters
```

    Available filters:
     - basic
     - csv
     - yaml
     - yaml-samples



```bash
eido convert peppro_paper.yaml --format basic
```

    Running plugin basic
    Project 'PEPPRO' (peppro_paper.yaml)
    47 samples (showing first 20): K562_PRO-seq_02, K562_PRO-seq_04, K562_PRO-seq_06, K562_PRO-seq_08, K562_PRO-seq_10, K562_PRO-seq_20, K562_PRO-seq_30, K562_PRO-seq_40, K562_PRO-seq_50, K562_PRO-seq_60, K562_PRO-seq_70, K562_PRO-seq_80, K562_PRO-seq_90, K562_PRO-seq_100, K562_RNA-seq_0, K562_RNA-seq_10, K562_RNA-seq_20, K562_RNA-seq_30, K562_RNA-seq_40, K562_RNA-seq_50
    Sections: name, pep_version, sample_table, looper, sample_modifiers



```bash
eido convert peppro_paper.yaml --format csv
```

    Running plugin csv
    sample_name,genome,organism,pipeline_interfaces,prealignments,protocol,read1,read_type,sample_desc,sample_name,srr,treatment,umi_len,read2
    K562_PRO-seq_02,hg38,human,['$CODE/peppro/sample_pipeline_interface.yaml'],human_rDNA,PRO,/Users/mstolarczyk/K562_PRO_2pct.fastq.gz,SINGLE,2% subsample of K562 PRO-seq,K562_PRO-seq_02,K562_PRO_2pct,2% subsample,0,
    K562_PRO-seq_04,hg38,human,['$CODE/peppro/sample_pipeline_interface.yaml'],human_rDNA,PRO,/Users/mstolarczyk/K562_PRO_4pct.fastq.gz,SINGLE,4% subsample of K562 PRO-seq,K562_PRO-seq_04,K562_PRO_4pct,4% subsample,0,
    K562_PRO-seq_06,hg38,human,['$CODE/peppro/sample_pipeline_interface.yaml'],human_rDNA,PRO,/Users/mstolarczyk/K562_PRO_6pct.fastq.gz,SINGLE,6% subsample of K562 PRO-seq,K562_PRO-seq_06,K562_PRO_6pct,6% subsample,0,
    K562_PRO-seq_08,hg38,human,['$CODE/peppro/sample_pipeline_interface.yaml'],human_rDNA,PRO,/Users/mstolarczyk/K562_PRO_8pct.fastq.gz,SINGLE,8% subsample of K562 PRO-seq,K562_PRO-seq_08,K562_PRO_8pct,8% subsample,0,
    K562_PRO-seq_10,hg38,human,['$CODE/peppro/sample_pipeline_interface.yaml'],human_rDNA,PRO,/Users/mstolarczyk/K562_PRO_10pct.fastq.gz,SINGLE,10% subsample of K562 PRO-seq,K562_PRO-seq_10,K562_PRO_10pct,10% subsample,0,
    K562_PRO-seq_20,hg38,human,['$CODE/peppro/sample_pipeline_interface.yaml'],human_rDNA,PRO,/Users/mstolarczyk/K562_PRO_20pct.fastq.gz,SINGLE,20% subsample of K562 PRO-seq,K562_PRO-seq_20,K562_PRO_20pct,20% subsample,0,
    K562_PRO-seq_30,hg38,human,['$CODE/peppro/sample_pipeline_interface.yaml'],human_rDNA,PRO,/Users/mstolarczyk/K562_PRO_30pct.fastq.gz,SINGLE,30% subsample of K562 PRO-seq,K562_PRO-seq_30,K562_PRO_30pct,30% subsample,0,
    K562_PRO-seq_40,hg38,human,['$CODE/peppro/sample_pipeline_interface.yaml'],human_rDNA,PRO,/Users/mstolarczyk/K562_PRO_40pct.fastq.gz,SINGLE,40% subsample of K562 PRO-seq,K562_PRO-seq_40,K562_PRO_40pct,40% subsample,0,
    K562_PRO-seq_50,hg38,human,['$CODE/peppro/sample_pipeline_interface.yaml'],human_rDNA,PRO,/Users/mstolarczyk/K562_PRO_50pct.fastq.gz,SINGLE,50% subsample of K562 PRO-seq,K562_PRO-seq_50,K562_PRO_50pct,50% subsample,0,
    K562_PRO-seq_60,hg38,human,['$CODE/peppro/sample_pipeline_interface.yaml'],human_rDNA,PRO,/Users/mstolarczyk/K562_PRO_60pct.fastq.gz,SINGLE,60% subsample of K562 PRO-seq,K562_PRO-seq_60,K562_PRO_60pct,60% subsample,0,
    K562_PRO-seq_70,hg38,human,['$CODE/peppro/sample_pipeline_interface.yaml'],human_rDNA,PRO,/Users/mstolarczyk/K562_PRO_70pct.fastq.gz,SINGLE,70% subsample of K562 PRO-seq,K562_PRO-seq_70,K562_PRO_70pct,70% subsample,0,
    K562_PRO-seq_80,hg38,human,['$CODE/peppro/sample_pipeline_interface.yaml'],human_rDNA,PRO,/Users/mstolarczyk/K562_PRO_80pct.fastq.gz,SINGLE,80% subsample of K562 PRO-seq,K562_PRO-seq_80,K562_PRO_80pct,80% subsample,0,
    K562_PRO-seq_90,hg38,human,['$CODE/peppro/sample_pipeline_interface.yaml'],human_rDNA,PRO,/Users/mstolarczyk/K562_PRO_90pct.fastq.gz,SINGLE,90% subsample of K562 PRO-seq,K562_PRO-seq_90,K562_PRO_90pct,90% subsample,0,
    K562_PRO-seq_100,hg38,human,['$CODE/peppro/sample_pipeline_interface.yaml'],human_rDNA,PRO,/Users/mstolarczyk/SRR155431[1-2].fastq.gz,SINGLE,Unsampled K562 PRO-seq,K562_PRO-seq_100,SRR155431[1-2],none,0,
    K562_RNA-seq_0,hg38,human,['$CODE/peppro/sample_pipeline_interface.yaml'],human_rDNA,PRO,/Users/mstolarczyk/K562_0pctRNA.fastq.gz,SINGLE,100% K562 PRO-seq + 0% K562 RNA-seq,K562_RNA-seq_0,K562_0pctRNA,70M total reads,0,
    K562_RNA-seq_10,hg38,human,['$CODE/peppro/sample_pipeline_interface.yaml'],human_rDNA,PRO,/Users/mstolarczyk/K562_10pctRNA.fastq.gz,SINGLE,90% K562 PRO-seq + 10% K562 RNA-seq,K562_RNA-seq_10,K562_10pctRNA,70M total reads,0,
    K562_RNA-seq_20,hg38,human,['$CODE/peppro/sample_pipeline_interface.yaml'],human_rDNA,PRO,/Users/mstolarczyk/K562_20pctRNA.fastq.gz,SINGLE,80% K562 PRO-seq + 20% K562 RNA-seq,K562_RNA-seq_20,K562_20pctRNA,70M total reads,0,
    K562_RNA-seq_30,hg38,human,['$CODE/peppro/sample_pipeline_interface.yaml'],human_rDNA,PRO,/Users/mstolarczyk/K562_30pctRNA.fastq.gz,SINGLE,70% K562 PRO-seq + 30% K562 RNA-seq,K562_RNA-seq_30,K562_30pctRNA,70M total reads,0,
    K562_RNA-seq_40,hg38,human,['$CODE/peppro/sample_pipeline_interface.yaml'],human_rDNA,PRO,/Users/mstolarczyk/K562_40pctRNA.fastq.gz,SINGLE,60% K562 PRO-seq + 40% K562 RNA-seq,K562_RNA-seq_40,K562_40pctRNA,70M total reads,0,
    K562_RNA-seq_50,hg38,human,['$CODE/peppro/sample_pipeline_interface.yaml'],human_rDNA,PRO,/Users/mstolarczyk/K562_50pctRNA.fastq.gz,SINGLE,50% K562 PRO-seq + 50% K562 RNA-seq,K562_RNA-seq_50,K562_50pctRNA,70M total reads,0,
    K562_RNA-seq_60,hg38,human,['$CODE/peppro/sample_pipeline_interface.yaml'],human_rDNA,PRO,/Users/mstolarczyk/K562_60pctRNA.fastq.gz,SINGLE,40% K562 PRO-seq + 60% K562 RNA-seq,K562_RNA-seq_60,K562_60pctRNA,70M total reads,0,
    K562_RNA-seq_70,hg38,human,['$CODE/peppro/sample_pipeline_interface.yaml'],human_rDNA,PRO,/Users/mstolarczyk/K562_70pctRNA.fastq.gz,SINGLE,30% K562 PRO-seq + 70% K562 RNA-seq,K562_RNA-seq_70,K562_70pctRNA,70M total reads,0,
    K562_RNA-seq_80,hg38,human,['$CODE/peppro/sample_pipeline_interface.yaml'],human_rDNA,PRO,/Users/mstolarczyk/K562_80pctRNA.fastq.gz,SINGLE,20% K562 PRO-seq + 80% K562 RNA-seq,K562_RNA-seq_80,K562_80pctRNA,70M total reads,0,
    K562_RNA-seq_90,hg38,human,['$CODE/peppro/sample_pipeline_interface.yaml'],human_rDNA,PRO,/Users/mstolarczyk/K562_90pctRNA.fastq.gz,SINGLE,10% K562 PRO-seq + 90% K562 RNA-seq,K562_RNA-seq_90,K562_90pctRNA,70M total reads,0,
    K562_RNA-seq_100,hg38,human,['$CODE/peppro/sample_pipeline_interface.yaml'],human_rDNA,PRO,/Users/mstolarczyk/K562_100pctRNA.fastq.gz,SINGLE,0% K562 PRO-seq + 100% K562 RNA-seq,K562_RNA-seq_100,K562_100pctRNA,70M total reads,0,
    K562_GRO-seq,hg38,human,['$CODE/peppro/sample_pipeline_interface.yaml'],human_rDNA,GRO,/Users/mstolarczyk/SRR1552484.fastq.gz,SINGLE,K562 GRO-seq,K562_GRO-seq,SRR1552484,none,0,
    HelaS3_GRO-seq,hg38,human,['$CODE/peppro/sample_pipeline_interface.yaml'],human_rDNA,GRO,/Users/mstolarczyk/SRR169361[1-2].fastq.gz,SINGLE,HelaS3 GRO-seq,HelaS3_GRO-seq,SRR169361[1-2],none,0,
    Jurkat_ChRO-seq_1,hg38,human,['$CODE/peppro/sample_pipeline_interface.yaml'],human_rDNA,PRO,/Users/mstolarczyk/SRR7616133.fastq.gz,SINGLE,Jurkat ChRO-seq,Jurkat_ChRO-seq_1,SRR7616133,none,6,
    Jurkat_ChRO-seq_2,hg38,human,['$CODE/peppro/sample_pipeline_interface.yaml'],human_rDNA,PRO,/Users/mstolarczyk/SRR7616134.fastq.gz,SINGLE,Jurkat ChRO-seq,Jurkat_ChRO-seq_2,SRR7616134,none,6,
    HEK_PRO-seq,hg38,human,['$CODE/peppro/sample_pipeline_interface.yaml'],human_rDNA,PRO,/Users/mstolarczyk/SRR8608074_PE1.fastq.gz,PAIRED,"HEK w/ osTIR1, ZNF143AID PRO-seq",HEK_PRO-seq,SRR8608074,Auxin,8,/Users/mstolarczyk/SRR8608074_PE2.fastq.gz
    HEK_ARF_PRO-seq,hg38,human,['$CODE/peppro/sample_pipeline_interface.yaml'],human_rDNA,PRO,/Users/mstolarczyk/SRR8608070_PE1.fastq.gz,PAIRED,"HEK w/ osTIR1, ZNF143AID, ARF PRO-seq",HEK_ARF_PRO-seq,SRR8608070,Auxin,8,/Users/mstolarczyk/SRR8608070_PE2.fastq.gz
    H9_PRO-seq_1,hg38,human,['$CODE/peppro/sample_pipeline_interface.yaml'],human_rDNA,PRO,/Users/mstolarczyk/H9_DMSO_rep1_PE1.fastq.gz,PAIRED,H9 PRO-seq,H9_PRO-seq_1,H9_DMSO_rep1,DMSO,8,/Users/mstolarczyk/H9_DMSO_rep1_PE2.fastq.gz
    H9_PRO-seq_2,hg38,human,['$CODE/peppro/sample_pipeline_interface.yaml'],human_rDNA,PRO,/Users/mstolarczyk/H9_DMSO_rep2_PE1.fastq.gz,PAIRED,H9 PRO-seq,H9_PRO-seq_2,H9_DMSO_rep2,DMSO,8,/Users/mstolarczyk/H9_DMSO_rep2_PE2.fastq.gz
    H9_PRO-seq_3,hg38,human,['$CODE/peppro/sample_pipeline_interface.yaml'],human_rDNA,PRO,/Users/mstolarczyk/H9_DMSO_rep3_PE1.fastq.gz,PAIRED,H9 PRO-seq,H9_PRO-seq_3,H9_DMSO_rep3,DMSO,8,/Users/mstolarczyk/H9_DMSO_rep3_PE2.fastq.gz
    H9_treated_PRO-seq_1,hg38,human,['$CODE/peppro/sample_pipeline_interface.yaml'],human_rDNA,PRO,/Users/mstolarczyk/H9_200nM_romidepsin_rep1_PE1.fastq.gz,PAIRED,H9 treated PRO-seq,H9_treated_PRO-seq_1,H9_200nM_romidepsin_rep1,200 nM romidepsin,8,/Users/mstolarczyk/H9_200nM_romidepsin_rep1_PE2.fastq.gz
    H9_treated_PRO-seq_2,hg38,human,['$CODE/peppro/sample_pipeline_interface.yaml'],human_rDNA,PRO,/Users/mstolarczyk/H9_200nM_romidepsin_rep2_PE1.fastq.gz,PAIRED,H9 treated PRO-seq,H9_treated_PRO-seq_2,H9_200nM_romidepsin_rep2,200 nM romidepsin,8,/Users/mstolarczyk/H9_200nM_romidepsin_rep2_PE2.fastq.gz
    H9_treated_PRO-seq_3,hg38,human,['$CODE/peppro/sample_pipeline_interface.yaml'],human_rDNA,PRO,/Users/mstolarczyk/H9_200nM_romidepsin_rep3_PE1.fastq.gz,PAIRED,H9 treated PRO-seq,H9_treated_PRO-seq_3,H9_200nM_romidepsin_rep3,200 nM romidepsin,8,/Users/mstolarczyk/H9_200nM_romidepsin_rep3_PE2.fastq.gz
    H9_PRO-seq_10,hg38,human,['$CODE/peppro/sample_pipeline_interface.yaml'],human_rDNA,PRO,/Users/mstolarczyk/H9_PRO-seq_10pct_PE1.fastq.gz,PAIRED,10% subset H9 PRO-seq 2,H9_PRO-seq_10,H9_PRO-seq_10pct,DMSO,8,/Users/mstolarczyk/H9_PRO-seq_10pct_PE2.fastq.gz
    H9_PRO-seq_20,hg38,human,['$CODE/peppro/sample_pipeline_interface.yaml'],human_rDNA,PRO,/Users/mstolarczyk/H9_PRO-seq_20pct_PE1.fastq.gz,PAIRED,20% subset H9 PRO-seq 2,H9_PRO-seq_20,H9_PRO-seq_20pct,DMSO,8,/Users/mstolarczyk/H9_PRO-seq_20pct_PE2.fastq.gz
    H9_PRO-seq_30,hg38,human,['$CODE/peppro/sample_pipeline_interface.yaml'],human_rDNA,PRO,/Users/mstolarczyk/H9_PRO-seq_30pct_PE1.fastq.gz,PAIRED,30% subset H9 PRO-seq 2,H9_PRO-seq_30,H9_PRO-seq_30pct,DMSO,8,/Users/mstolarczyk/H9_PRO-seq_30pct_PE2.fastq.gz
    H9_PRO-seq_40,hg38,human,['$CODE/peppro/sample_pipeline_interface.yaml'],human_rDNA,PRO,/Users/mstolarczyk/H9_PRO-seq_40pct_PE1.fastq.gz,PAIRED,40% subset H9 PRO-seq 2,H9_PRO-seq_40,H9_PRO-seq_40pct,DMSO,8,/Users/mstolarczyk/H9_PRO-seq_40pct_PE2.fastq.gz
    H9_PRO-seq_50,hg38,human,['$CODE/peppro/sample_pipeline_interface.yaml'],human_rDNA,PRO,/Users/mstolarczyk/H9_PRO-seq_50pct_PE1.fastq.gz,PAIRED,50% subset H9 PRO-seq 2,H9_PRO-seq_50,H9_PRO-seq_50pct,DMSO,8,/Users/mstolarczyk/H9_PRO-seq_50pct_PE2.fastq.gz
    H9_PRO-seq_60,hg38,human,['$CODE/peppro/sample_pipeline_interface.yaml'],human_rDNA,PRO,/Users/mstolarczyk/H9_PRO-seq_60pct_PE1.fastq.gz,PAIRED,60% subset H9 PRO-seq 2,H9_PRO-seq_60,H9_PRO-seq_60pct,DMSO,8,/Users/mstolarczyk/H9_PRO-seq_60pct_PE2.fastq.gz
    H9_PRO-seq_70,hg38,human,['$CODE/peppro/sample_pipeline_interface.yaml'],human_rDNA,PRO,/Users/mstolarczyk/H9_PRO-seq_70pct_PE1.fastq.gz,PAIRED,70% subset H9 PRO-seq 2,H9_PRO-seq_70,H9_PRO-seq_70pct,DMSO,8,/Users/mstolarczyk/H9_PRO-seq_70pct_PE2.fastq.gz
    H9_PRO-seq_80,hg38,human,['$CODE/peppro/sample_pipeline_interface.yaml'],human_rDNA,PRO,/Users/mstolarczyk/H9_PRO-seq_80pct_PE1.fastq.gz,PAIRED,80% subset H9 PRO-seq 2,H9_PRO-seq_80,H9_PRO-seq_80pct,DMSO,8,/Users/mstolarczyk/H9_PRO-seq_80pct_PE2.fastq.gz
    H9_PRO-seq_90,hg38,human,['$CODE/peppro/sample_pipeline_interface.yaml'],human_rDNA,PRO,/Users/mstolarczyk/H9_PRO-seq_90pct_PE1.fastq.gz,PAIRED,90% subset H9 PRO-seq 2,H9_PRO-seq_90,H9_PRO-seq_90pct,DMSO,8,/Users/mstolarczyk/H9_PRO-seq_90pct_PE2.fastq.gz
    H9_PRO-seq_100,hg38,human,['$CODE/peppro/sample_pipeline_interface.yaml'],human_rDNA,PRO,/Users/mstolarczyk/H9_PRO-seq_100pct_PE1.fastq.gz,PAIRED,100% H9 PRO-seq 2,H9_PRO-seq_100,H9_PRO-seq_100pct,DMSO,8,/Users/mstolarczyk/H9_PRO-seq_100pct_PE2.fastq.gz



```bash

```
