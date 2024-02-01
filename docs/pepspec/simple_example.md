
# How do I create my own PEP? A simple example

<img src="../img/pep_contents.svg" alt="" style="float:right; margin-left:20px" width="250px">

To use any PEP-compatible tool, you first need a **PEP**. A PEP describes a collection of data with its metadata. To create a PEP to represent your dataset, you create 2 files:



1. **Project config file** - a `yaml` file with project settings
2. **Sample table** - a `csv` file with 1 row per sample


In the simplest case, *project_config.yaml* is just a few lines of yaml, a simple and widely-used hierarchical markup language used to store key-value pairs; you can <a href="http://www.yaml.org/start.html">read more about yaml here</a>.  Here's a minimal example project_config.yaml:


```{yaml}
pep_version: 2.0.0
sample_table: "path/to/sample_table.csv"
```

The `sample_table` key points to the second part of a *PEP*, a comma-separated value (``csv``) file annotating samples in the project. Here's a small example of *sample_table.csv*:

```{csv}
"sample_name", "protocol", "file"
"frog_1", "RNA-seq", "frog1.fq.gz"
"frog_2", "RNA-seq", "frog2.fq.gz"
"frog_3", "RNA-seq", "frog3.fq.gz"
"frog_4", "RNA-seq", "frog4.fq.gz"
```

With those two simple files, you are ready to use the pepkit tools! With a single line of code, you could load this into R using [pepr](http://github.com/pepkit/pepr), into python using [peppy](http://peppy.databio.org), or run each sample through an arbitrary command-line pipeline using [looper](http://looper.databio.org). You can use this formulation to run a workflow written in [CWL](http://commonwl.org) or using [SnakeMake](http://snakemake.readthedocs.io). If you make a habit of describing all your projects like this, you'll never parse another sample annotation sheet again. You'll never write another pipeline submission loop.

This simple example presents a minimal functioning PEP. In practice, there are many advanced features of PEP structure. For instance, you can add additional sections to tailor your project for specific tools. But at its core, PEP is simple and generic; this way, you can start with the basics, and only add more complexity as you need it.

More advanced features are described in the [complete PEP specification](specification.md).
