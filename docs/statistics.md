---
hide:
  - navigation
template: stats.html
title: "PEPkit: the bio data management toolkit"
toc_depth: 1
---

# PEPkit usage statistics

This page documents usage of PEPkit-related tools:

1. [statistics of downloads of packages from PyPI and CRAN](#download-history)
2. [other software packages that use PEPkit software](#software-using-pepkit)
3. [datasets organized in PEP-compatible formats](#demo-data-using-pepkit)
4. [publications that reference PEP manuscripts](#publications-that-use-pepkit)



## Download history

Monthly downloads of PEPkit packages. Data is harvested from PyPI and CRAN by
[databio/stats](https://github.com/databio/stats) and refreshed on the first of
each month.

### PyPI

<div class="chart-grid">
  <div class="chart-card"><div class="chart-container" id="pypi-peppy"        data-chart-type="pypi" data-package="peppy"></div></div>
  <div class="chart-card"><div class="chart-container" id="pypi-looper"       data-chart-type="pypi" data-package="looper"></div></div>
  <div class="chart-card"><div class="chart-container" id="pypi-eido"         data-chart-type="pypi" data-package="eido"></div></div>
  <div class="chart-card"><div class="chart-container" id="pypi-geofetch"     data-chart-type="pypi" data-package="geofetch"></div></div>
  <div class="chart-card"><div class="chart-container" id="pypi-pipestat"     data-chart-type="pypi" data-package="pipestat"></div></div>
  <div class="chart-card"><div class="chart-container" id="pypi-pypiper"      data-chart-type="pypi" data-package="piper" data-label="pypiper"></div></div>
  <div class="chart-card"><div class="chart-container" id="pypi-yacman"       data-chart-type="pypi" data-package="yacman"></div></div>
  <div class="chart-card"><div class="chart-container" id="pypi-ubiquerg"     data-chart-type="pypi" data-package="ubiquerg"></div></div>
  <div class="chart-card"><div class="chart-container" id="pypi-pephubclient" data-chart-type="pypi" data-package="pephubclient"></div></div>
  <div class="chart-card"><div class="chart-container" id="pypi-pepdbagent"   data-chart-type="pypi" data-package="pepdbagent"></div></div>
  <div class="chart-card"><div class="chart-container" id="pypi-divvy"        data-chart-type="pypi" data-package="divvy"></div></div>
</div>

### CRAN

<div class="chart-grid">
  <div class="chart-card"><div class="chart-container" id="cran-pepr" data-chart-type="cran" data-package="pepr"></div></div>
</div>

## Software using PEPkit

Publicly available software that builds on PEP:

* [PEPATAC](http://pepatac.databio.org/) - An ATAC-seq pipeline. 
* [PEPPRO](http://peppro.databio.org/) - An nascent RNA profiling pipeline (PRO-seq, GRO-seq, ChRO-seq).
* [peppy](https://github.com/pepkit/peppy)
* [pepr](https://github.com/pepkit/pepr)
* [geofetch](https://github.com/pepkit/geofetch) - Converts GEO or SRA accessions into PEP projects.
* [divcfg](https://github.com/pepkit/divcfg)
* [pifaces](https://github.com/pepkit/pifaces)
* [pypiper](https://github.com/databio/pypiper)
* [dnameth_pipelines](https://github.com/databio/dnameth_pipelines)
* [projectInit](https://github.com/databio/projectInit)
* [ngstoolkit](https://github.com/afrendeiro/toolkit) - NGS analysis toolkit
* [BiocProject](https://github.com/pepkit/BiocProject)

## Demo data using PEPkit

* [example_peps repository](https://github.com/pepkit/example_peps) - A collection of example PEPs demonstrating various features.
* [microtest](https://github.com/epigen/microtest)
* [hello looper! example](https://github.com/pepkit/hello_looper)

## Real datasets organized in PEP format:

* [https://github.com/epigen/crop-seq](https://github.com/epigen/crop-seq)
* [https://github.com/epigen/baf_complex](https://github.com/epigen/baf_complex)
* [https://github.com/epigen/mthfd1](https://github.com/epigen/mthfd1)
* [https://github.com/epigen/cll-ibrutinib_time](https://github.com/epigen/cll-ibrutinib_time)
* [https://github.com/epigen/cll-ibrutinib](https://github.com/epigen/cll-ibrutinib)
* [https://github.com/epigen/cll-chromatin](https://github.com/epigen/cll-chromatin)

## Publications that use PEPkit:

<!-- publications-list -->

## PEP shield

If your project is PEP-compatible, please add it to this list with a [pull request](https://github.com/pepkit/pepkit.github.io/blob/master/_docs/tools.md) and use this shield to showcase PEP:

<img src="https://pepkit.github.io/img/PEP-compatible-green.svg" alt="PEP compatible" style="float:left; margin:10px"><br clear="all"/>

Here's `markdown` (for use on GitHub READMEs):
```
[![PEP compatible](https://pepkit.github.io/img/PEP-compatible-green.svg)](https://pepkit.github.io)
```

Or `HTML`:
```
<a href="https://pepkit.github.io"><img src="https://pepkit.github.io/img/PEP-compatible-green.svg" alt="PEP compatible" style="float:left; margin:10px"></a>
```


