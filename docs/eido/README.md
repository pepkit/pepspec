[![PEP compatible](https://pepkit.github.io/img/PEP-compatible-green.svg)](http://pepkit.github.io)
![Run pytests](https://github.com/pepkit/eido/workflows/Run%20pytests/badge.svg)
[![codecov](https://codecov.io/gh/pepkit/eido/branch/master/graph/badge.svg)](https://codecov.io/gh/pepkit/eido)
[![pypi-badge](https://img.shields.io/pypi/v/eido)](https://pypi.org/project/eido)
[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)
[![GitHub source](https://img.shields.io/badge/source-github-354a75?logo=github)](https://github.com/pepkit/eido)

# <img src="img/eido.svg" alt="eido" style="height:70px"/>

## Introduction

Eido is used to 1) validate or 2) convert format of sample metadata. Sample metadata is stored according to the standard [PEP specification](https://pep.databio.org). For validation, eido is based on [JSON Schema](https://json-schema.org) and extends it with new features, like required input files. You can [write your own schema](writing-a-schema.md) for your pipeline and use eido to validate sample metadata. For conversion, [eido filters](filters.md) convert sample metadata input into any output format, including [custom filters](writing-a-filter.md).

## Why do we need eido?

Data-intensive bioinformatics projects often include metadata describing a set of samples. When it comes to handling such sample metadata, there are two common challenges that eido solves:

<img src="img/validation.svg" style="float:right; width:220px; margin-left:50px">

- **Validation**. Tool authors use eido to specify and describe required input sample attributes. Input sample attributes are described with a schema, and eido validates the sample metadata to ensure it satisfies the tool's needs. Eido uses [JSON Schema](https://json-schema.org/), which annotates and validates JSON. JSON schema alone is great for validating JSON, but bioinformatics sample metadata is more complicated, so eido provides additional capability and features tailored to bioinformatics projects listed below. 

<img src="img/conversion.svg" style="float:right; width:220px; margin-left:50px">

- **Format conversion**. Tools often require sample metadata in a specific format. Eido filters take a metadata in standard PEP format and convert it to any desired output format. Filters can be either built-in or custom. This allows a single sample metadata source to be used for multiple downstream analyses.

## Eido validation features

An eido schema is written using the JSON Schema vocabulary, plus a few additional features:

1. **required input files**. Eido adds `required_files`, which allows a schema author to specify which attributes must point to files that exist.
2. **optional input files**. `files` specifies which attributes point to files that may or may not exist.
3. **project and sample validation**. Eido validates project attributes separately from sample attributes.
4. **schema imports**. Eido adds an `imports` section for schemas that should be validated prior to this schema
5. **automatic multi-value support**. Eido validates successfully for singular or plural sample attributes for strings, booleans, and numbers. This accommodates the PEP subsample_table feature.

## How to use eido

- [Use eido to validate data from the command line](cli.md)
- [Use eido to validate data from Python](demo.md)
- [Write your own schema](writing-a-schema.md)

---

## Why the name 'eido'?

*Eidos* is a Greek term meaning *form*, *essence*, or *type* (see Plato's [Theory of Forms](https://en.wikipedia.org/wiki/Theory_of_forms)). Schemas are analogous to *forms*, and eido tests claims that an instance is of a particular form. Eido also helps *change* forms using filters.
