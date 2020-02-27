---
title: "Create a PEP from GEO or SRA"
---
`geofetch` is a command-line utility that converts GEO or SRA accessions into PEP projects. You provide an accession (or a spreadsheet with a list of accessions), and `geofetch` with produce the PEP (both project config and sample annotation). `geofetch` can also download the data from SRA, so your project will be ready for direct input into any PEP-compatible tool.

### Code and documentation

* [User documentation and vignettes](http://code.databio.org/geofetch)
* [Source code at Github](https://github.com/pepkit/geofetch)

### Quick start

`geofetch` is a python package that can be installed from [PyPI](https://pypi.org/project/geofetch/):

```
pip install geofetch
```

To see the command-line options, run it with `-h`:

```console
geofetch --help
```

For example, you can run `geofetch` to build a PEP for a GSE accession like this:

```console
geofetch -i GSE##### -m path/to/metadata/folder -n PROJECT_NAME
```

