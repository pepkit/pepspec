# PEP in practice

## Software using PEP

Publicly available software that builds on PEP:

* [PEPATAC](http://pepatac.databio.org/) - An ATAC-seq pipeline. 
* [PEPPRO](http://peppro.databio.org/) - An nascent RNA profiling pipeline (PRO-seq, GRO-seq, ChRO-seq).
* [peppy](https://github.com/pepkit/peppy) - PEP reading Python package
* [pepr](https://github.com/pepkit/pepr) - PEP reading R package
* [BiocProject](https://github.com/pepkit/BiocProject) - R package that connects PEP standard with Bioconductor
* [geofetch](https://github.com/pepkit/geofetch) - Converts GEO or SRA accessions into PEP projects.
* [divcfg](https://github.com/pepkit/divcfg) - PEP reading Python package
* [pypiper](https://github.com/databio/pypiper) - a development-oriented pipeline framework
* [dnameth_pipelines](https://github.com/databio/dnameth_pipelines) - a set of pypiper pielines
* [projectInit](https://github.com/databio/projectInit) - R package that helps you load a project-specific R workspace
* [ngstoolkit](https://github.com/afrendeiro/toolkit) - NGS analysis toolkit
* [Snakemake](https://snakemake.readthedocs.io/en/stable/snakefiles/configuration.html#configuring-scientific-experiments-via-peps) - A tool to create reproducible and scalable data analyses workflows.


## Demo data using PEP

* [example_peps repository](https://github.com/pepkit/example_peps) - a collection of example PEPs demonstrating various features.
* [microtest](https://github.com/epigen/microtest) - a repository of small test data from various data types, for testing pipelines
* [hello looper! example](https://github.com/pepkit/hello_looper) - a repository demonstrates how to install [looper](http://looper.databio.org/en/latest/) and use it to run the included pipeline on the included PEP

## Real datasets organized in PEP format:

* [https://github.com/epigen/crop-seq](https://github.com/epigen/crop-seq) - Pooled CRISPR screening with single-cell transcriptome readout | PEP1.0.0. 
* [https://github.com/epigen/baf_complex](https://github.com/epigen/baf_complex): *Systematic functional characterization of BAF mutations yields novel intra-complex synthetic lethalities* | PEP1.0.0
* [https://github.com/epigen/mthfd1](https://github.com/epigen/mthfd1) - MTHFD1 links folate metabolism to BRD4-mediated transcriptional regulation | PEP1.0.0
* [https://github.com/epigen/cll-ibrutinib_time](https://github.com/epigen/cll-ibrutinib_time) - Chromatin mapping and single-cell immune profiling define the temporal dynamics of ibrutinib drug response in chronic lymphocytic leukemia | PEP1.0.0
* [https://github.com/epigen/cll-ibrutinib](https://github.com/epigen/cll-ibrutinib) - Combined chemosensitivity and chromatin profiling prioritizes drug combinations in CLL | PEP1.0.0
* [https://github.com/epigen/cll-chromatin](https://github.com/epigen/cll-chromatin) - Chromatin accessibility maps of chronic lymphocytic leukemia identify subtype-specific epigenome signatures and transcription regulatory networks | PEP1.0.0

## Publications that use PEP software:

Molder et al.
2021.
Sustainable data analysis with Snakemake
*F1000Res*
[https://www.ncbi.nlm.nih.gov/pmc/articles/PMC8114187/](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC8114187/)

Sheffield et al.
2020.
Linking big biomedical datasets to modular analysis with Portable Encapsulated Projects.
*BioRxiv.*
[https://doi.org/10.1101/2020.10.08.331322](https://doi.org/10.1101/2020.10.08.331322)

Zhou et al.
2020.
CATA: a comprehensive chromatin accessibility database for cancer
*BioRxiv.*
[https://doi.org/10.1101/2020.05.16.099325](https://doi.org/10.1101/2020.05.16.099325)


Weber et al.
2020.
Transient “rest” induces functional reinvigoration and epigenetic remodeling in exhausted CAR-T cells.
*BioRxiv.*
[https://doi.org/10.1101/2020.01.26.920496](https://doi.org/10.1101/2020.01.26.920496)

Granja et al.
2020.
ArchR: An integrative and scalable software package for single-cell chromatin accessibility analysis
*BioRxiv.*
[https://doi.org/10.1101/2020.04.28.066498](https://doi.org/10.1101/2020.04.28.066498)

Smith et al.
2020.
Quality control and processing of nascent RNA profiling data
*BioRxiv.*
[https://doi.org/10.1101/2020.02.27.956110](https://doi.org/10.1101/2020.02.27.956110)

Ram-Mohan et al.
2020.
Integrative profiling of early host chromatin accessibility responses in human neutrophils with sensitive pathogen detection
*BioRxiv.*
[https://doi.org/10.1101/2020.04.28.066829](https://doi.org/10.1101/2020.04.28.066829)

Fan et al.
2020.
Epigenetic reprogramming towards mesenchymal-epithelial transition in ovarian cancer-associated mesenchymal stem cells drives metastasis
*BioRxiv.*
[https://doi.org/10.1101/2020.02.25.964197](https://doi.org/10.1101/2020.02.25.964197)

Stolarczyk et al.
2020.
Refgenie: a reference genome resource manager
*GigaScience*.
[https://doi.org/10.1093/gigascience/giz149](https://doi.org/10.1093/gigascience/giz149)

Corces et al.
2018.
The chromatin accessibility landscape of primary human cancers.
*Science*.
[https://doi.org/10.1126/science.aav1898](https://doi.org/10.1126/science.aav1898)

Datlinger et al.
2017.
Pooled CRISPR screening with single-cell transcriptome readout
*Nature Methods*.
[https://doi.org/10.1038/nmeth.4177](https://doi.org/10.1038/nmeth.4177)

Sheffield et al.
2017.
DNA methylation heterogeneity defines a disease spectrum in Ewing sarcoma
*Nature Medicine*.
[https://doi.org/10.1038/nm.4273](https://doi.org/10.1038/nm.4273)


### PEP shield

If your project is PEP-compatible, please add it to this list with a [pull request](https://github.com/pepkit/pepkit.github.io/blob/master/_docs/tools.md) and use this shield to showcase PEP:

<img src="http://pepkit.github.io/img/PEP-compatible-green.svg" alt="PEP compatible" style="float:left; margin:10px"><br clear="all"/>

Here's `markdown` (for use on GitHub READMEs):
```
[![PEP compatible](http://pepkit.github.io/img/PEP-compatible-green.svg)](http://pepkit.github.io)
```

Or `HTML`:
```
<a href="http://pepkit.github.io"><img src="http://pepkit.github.io/img/PEP-compatible-green.svg" alt="PEP compatible" style="float:left; margin:10px"></a>
```

