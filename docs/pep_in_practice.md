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

- [https://github.com/ccrobertson/t1d-immunochip-2020/tree/master/scripts/caqtl/pepatac_files](https://github.com/ccrobertson/t1d-immunochip-2020/tree/master/scripts/caqtl/pepatac_files) - Analysis of caQTLs in Type I diabetes
- [https://github.com/databio/bedshift_analysis](https://github.com/databio/bedshift_analysis) - Analysis of perturbation of genomic intervals.
- [https://github.com/epigen/crop-seq](https://github.com/epigen/crop-seq) - Pooled CRISPR screening with single-cell transcriptome readout | PEP1.0.0. 
- [https://github.com/epigen/baf_complex](https://github.com/epigen/baf_complex): *Systematic functional characterization of BAF mutations yields novel intra-complex synthetic lethalities* | PEP1.0.0
- [https://github.com/epigen/mthfd1](https://github.com/epigen/mthfd1) - MTHFD1 links folate metabolism to BRD4-mediated transcriptional regulation | PEP1.0.0
- [https://github.com/epigen/cll-ibrutinib_time](https://github.com/epigen/cll-ibrutinib_time) - Chromatin mapping and single-cell immune profiling define the temporal dynamics of ibrutinib drug response in chronic lymphocytic leukemia | PEP1.0.0
- [https://github.com/epigen/cll-ibrutinib](https://github.com/epigen/cll-ibrutinib) - Combined chemosensitivity and chromatin profiling prioritizes drug combinations in CLL | PEP1.0.0
- [https://github.com/epigen/cll-chromatin](https://github.com/epigen/cll-chromatin) - Chromatin accessibility maps of chronic lymphocytic leukemia identify subtype-specific epigenome signatures and transcription regulatory networks | PEP1.0.0

## Publications that use PEP software:

<ul>
<li><b>O'Connor et al. (2021). </b><i>BET protein inhibition regulates macrophage chromatin accessibility and microbiota-dependent colitis</i> 
<br><i>bioRxiv</i>.  <span class="doi">DOI: <a href="http://dx.doi.org/10.1101/2021.07.15.452570">10.1101/2021.07.15.452570</a></li>
<li><b>Ram-Mohan et al. (2021). </b><i>Profiling chromatin accessibility responses in human neutrophils with sensitive pathogen detection</i> 
<br><i>Life Science Alliance</i>.  <span class="doi">DOI: <a href="http://dx.doi.org/10.26508/lsa.202000976">10.26508/lsa.202000976</a></li>
<li><b>Robertson et al. (2021). </b><i>Fine-mapping, trans-ancestral and genomic analyses identify causal variants, cells, genes and drug targets for type 1 diabetes</i> 
<br><i>Nature Genetics</i>.  <span class="doi">DOI: <a href="http://dx.doi.org/10.1038/s41588-021-00880-5">10.1038/s41588-021-00880-5</a></li>
<li><b>Hasegawa et al. (2021). </b><i>Clonal inactivation of telomerase promotes accelerated stem cell differentiation</i> 
<br><i>bioRxiv</i>.  <span class="doi">DOI: <a href="http://dx.doi.org/10.1101/2021.04.28.441728">10.1101/2021.04.28.441728</a></li>
<li><b>Weber et al. (2021). </b><i>Transient rest restores functionality in exhausted CAR-T cells through epigenetic remodeling</i> 
<br><i>Science</i>.  <span class="doi">DOI: <a href="http://dx.doi.org/10.1126/science.aba1786">10.1126/science.aba1786</a></li>
<li><b>Gharavi et al. (2021). </b><i>Embeddings of genomic region sets capture rich biological associations in low dimensions</i> 
<br><i>Bioinformatics</i>.  <span class="doi">DOI: <a href="http://dx.doi.org/10.1093/bioinformatics/btab439">10.1093/bioinformatics/btab439</a></li>
<li><b>Tovar et al. (2021). </b><i>Integrative phenotypic and genomic analyses reveal strain-dependent responses to acute ozone exposure and their associations with airway macrophage transcriptional activity</i> 
<br><i>bioRxiv</i>.  <span class="doi">DOI: <a href="http://dx.doi.org/10.1101/2021.01.29.428733">10.1101/2021.01.29.428733</a></li>
<li><b>Granja et al. (2021). </b><i>ArchR is a scalable software package for integrative single-cell chromatin accessibility analysis</i> 
<br><i>Nature Genetics</i>.  <span class="doi">DOI: <a href="http://dx.doi.org/10.1038/s41588-021-00790-6">10.1038/s41588-021-00790-6</a></li>
<li><b>Gu et al. (2021). </b><i>Bedshift: perturbation of genomic interval sets</i> 
<br><i>Genome Biology</i>.  <span class="doi">DOI: <a href="http://dx.doi.org/10.1186/s13059-021-02440-w">10.1186/s13059-021-02440-w</a></li>
<li><b>Mölder et al. (2021). </b><i>Sustainable data analysis with Snakemake</i> 
<br><i>F1000Research</i>.  <span class="doi">DOI: <a href="http://dx.doi.org/10.12688/f1000research.29032.2">10.12688/f1000research.29032.2</a></li>
<li><b>Smith et al. (2021). </b><i>PEPPRO: quality control and processing of nascent RNA profiling data</i> 
<br><i>Genome Biology</i>.  <span class="doi">DOI: <a href="http://dx.doi.org/10.1186/s13059-021-02349-4">10.1186/s13059-021-02349-4</a></li>
<li><b>Fan et al. (2020). </b><i>Epigenomic Reprogramming toward Mesenchymal-Epithelial Transition in Ovarian-Cancer-Associated Mesenchymal Stem Cells Drives Metastasis</i> 
<br><i>Cell Reports</i>.  <span class="doi">DOI: <a href="http://dx.doi.org/10.1016/j.celrep.2020.108473">10.1016/j.celrep.2020.108473</a></li>
<li><b>Smith et al. (2020). </b><i>PEPATAC: An optimized ATAC-seq pipeline with serial alignments</i> 
<br><i>bioRxiv</i>.  <span class="doi">DOI: <a href="http://dx.doi.org/10.1101/2020.10.21.347054">10.1101/2020.10.21.347054</a></li>
<li><b>Zhou et al. (2020). </b><i>CATA: a comprehensive chromatin accessibility database for cancer</i> 
<br><i>bioRxiv</i>.  <span class="doi">DOI: <a href="http://dx.doi.org/10.1101/2020.05.16.099325">10.1101/2020.05.16.099325</a></li>
<li><b>Stolarczyk et al. (2020). </b><i>Refgenie: a reference genome resource manager</i> 
<br><i>GigaScience</i>.  <span class="doi">DOI: <a href="http://dx.doi.org/10.1093/gigascience/giz149">10.1093/gigascience/giz149</a></li>
<li><b>Corces et al. (2018). </b><i>The chromatin accessibility landscape of primary human cancers</i> 
<br><i>Science</i>.  <span class="doi">DOI: <a href="http://dx.doi.org/10.1126/science.aav1898">10.1126/science.aav1898</a></li>
<li><b>Datlinger et al. (2017). </b><i>Pooled CRISPR screening with single-cell transcriptome readout</i> 
<br><i>Nat. Methods</i>.  <span class="doi">DOI: <a href="http://dx.doi.org/10.1038/nmeth.4177">10.1038/nmeth.4177</a></li>
<li><b>Sheffield et al. (2017). </b><i>DNA methylation heterogeneity defines a disease spectrum in Ewing sarcoma</i> 
<br><i>Nature Medicine</i>.  <span class="doi">DOI: <a href="http://dx.doi.org/10.1038/nm.4273">10.1038/nm.4273</a></li>
</ul>

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

