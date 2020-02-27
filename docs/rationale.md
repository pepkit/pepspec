---
title: Rationale
---

<img src="/img/data-munging.svg" alt="" style="float:right; margin-left:10px" width="300px">

In a data analysis project, we frequently want to run many different tools on the same input data. Too often, this requires structuring the data uniquely for each tool. This makes it difficult to test multiple tools because each connection structure must be defined manually.

To alleviate this challenge of linking data to tools, Portable Encapsulated Projects (PEP) standardizes the description of data collections, enabling both data providers and data users to communicate through a common interface. This link operates around a simple, standard, extensible definition of a <i>project</i>.

PEP makes it easy to:

1. use one metadata structure for all your projects
2. work collaboratively
3. share your project with others
4. use multiple tools without restructuring metadata
5. analyze data in both R *and* Python


This web page outlines the PEP specification. Once you have a PEP, you will be able to process that metadata using tools in *pepkit*. You can find tools to use on your PEP in the [list of PEP-compatible external tools](/docs/software/) and [projects that use PEP](/docs/projects/).

# User stories

Here are a few example scenarios that describe the type of users and use cases for which *PEP* can be useful. 

## Sharing datasets among collaborators

### The situation
Vijay is a computational biologist who collaborates with a group that has produced genomic data from 24 human blood samples. Vijay put together some software tools to analyze this data and came up with a novel way of looking at the samples. When he presents his results, Artur, from a lab down the hall, thinks Vijay's method would be really cool to apply on *his* samples as well. Artur's project has 50 genomic patient blood samples from a different disease with a similar underpinning. Artur would like to just send his data to Vijay and have him run it through Vijay's tool to see what he finds. Will Vijay be stuck with organizing and reformatting Artur's poorly-organized data?

### How pepkit solves the problem

Luckily, Artur's group is enlightened, and they always organize their projects in PEP format because they use a PEP-compatible pipeline for their data processing. Similarly, Vijay has designed his python package to rely on [peppy](http://code.databio.org/peppy) for project structure. As a result, all Artur has to do is send Vijay his PEP, and Vijay runs it right on the samples. Nobody has to duplicate, rename, reorganize, and re-annotate Artur's samples to get Vijay's tool to run.

## Running multiple pipelines on my dataset
### The situation
Agnes is a biologist interested in understanding how chromatin accessibility differs among patients with Ewing sarcoma. Agnes processed 15 human patient samples with ATAC-seq. She isn't sure how to analyze the data, but she found [PEPATAC](http://code.databio.org/PEPATAC), a pipeline that processes ATAC-seq data. PEPATAC requires that she organize her 15 samples in PEP format, which she does. She runs the data through the pipeline and is analyzing the results when a new pipeline called ATACMASTER is published, which is particularly suited for her particular biological system. She'd love to run her samples through this pipeline to see if it changes things. But wait...it took her a week to get her samples in the right format and structure and filenames on the cluster for the first pipeline. Will she need to re-organize her project, re-name her files, and change her annotation structure to fit the new pipeline?

### How pepkit solves the problem

Because ATACMASTER is *also* PEP-compatible, Agnes doesn't have to reorganize anything; all she does is change her project to point at the new pipeline, and it runs right through. If ATACMASTER was built in the traditional way, though, it would specify it's *own* structure, and Agnes would have a few painful days of data munging and troubleshooting before she got ATACMASTER to run. Then, if ULTIMATEPIPELINE comes out, Agnes could be burned out of data restructuring, and may decide to forget it, missing potential discovery.



## Running my pipeline on a public dataset from GEO

### The situation

Jane has been working on a project studying DNA methylation in kidneys from a population of mice. She has sequencing data from 200 mouse samples, which are divided into 3 different treatment groups, and wants to know how the DNA methylation differs among groups. She has put together a pipeline to process her raw `fastq` sequencing data into methylation calls and has identified some interesting differences. But now she'd like to analyze this is the context of a recently published cohort of 75 mouse kidneys from a different population. The original study put the raw data on GEO, but the processed data was run on the `mm9` reference assembly instead of `mm10`, so she can't immediately compare. Shortly thereafter, this kidney work has become really hot, and 2, then 3 more studies with mouse kidney samples are published. How can Jane organize all that recently published data in a way that will work with her project?

### How pepkit solves the problem

If she organized her project as a PEP and her pipeline used pepkit, she could use [geofetch](http://code.databio.org/geofetch) to download the public GEO data and create a PEP from it in a single line of code. In another line or two, she could use `looper` to run her custom DNA methylation pipeline on that data. Finally, she can use `pepr` or `BiocProject` to load that processed public data into R, and immediately compare it with her in-house data. If she was using an independent method for organizing her samples, she'd have to repeat that for each new dataset that is published.


## Testing my tool on many different data sources

### The situation

Carlos has downloaded some public transcription factor binding microarray data and been trying to think of new ways to visualize things. He made a nice new tool that can load up this data type into R and display a shiny app for interactive visualization. He would like to use it to test a bunch of other public datasets, and eventually realizes that others might want to use it to look at their data as well. 

### How pepkit solves the problem

Since Carlos' package imports `pepr`, his tool can immediately work on any PEP-compatible project. He can therefoer use `geofetch` to download the public GEO data and create a PEP, which can load right into his tool Any of his colleagues that want to use his tool can, as well. By testing a bunch of different datasets, Carlos has made his tool much more useful.
