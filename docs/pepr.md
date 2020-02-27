---
title: "R package: pepr"
---

<img src="/img/logo_R.svg" alt="" style="float:left; margin:20px">

`pepr` is an R package for reading Portable Encapsulated Projects. It will read PEP projects, loading all project and sample metadata into R with a single line of code. `pepr` is currently in alpha mode and should not be used production projects. It is made available for conceptual and testing purposes only.

### Code and documentation

* [User documentation and vignettes](http://code.databio.org/pepr/)
* [Source code at Github](https://github.com/pepkit/pepr)

### Quick start

Install with 

```
devtools::install_github("pepkit/pepr")
```

Load up your project like this:


```
p = pepr::Project(file="project_config.yaml")
```

Now you can retrieve all your configuration information or sample metadata with easy getter functions:

```
samples(p)
config(p)
```


