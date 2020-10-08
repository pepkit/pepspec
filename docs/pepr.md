# R package: pepr

<!-- <img src="/img/logo_R.svg" alt="" style="float:left; margin:20px"> -->

`pepr` is an R package for reading Portable Encapsulated Projects. It will read PEP projects, loading all project and sample metadata into R with a single line of code. `pepr` is currently in alpha mode and should not be used production projects.

### Code and documentation

* [User documentation and vignettes](http://code.databio.org/pepr/)
* [`pepr` API](https://code.databio.org/pepr/reference/index.html)
* [Source code at Github](https://github.com/pepkit/pepr)

### Quick start

Install from [CRAN](https://cran.rstudio.com/web/packages/pepr/index.html):

```R
install.packages("pepr")
```

Load a project and explore metadata like this:

```R
library("pepr")
cfgPath = system.file(
    "extdata",
    paste0("example_peps-master"),
    "example_basic",
    "project_config.yaml",
    package = "pepr"
  )
p = Project(file = cfgPath)

sampleTable(p)
config(p)
```