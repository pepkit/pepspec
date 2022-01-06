# How to validate a PEP

<figure>
<img src="../img/validation.svg" width="325">
<figcaption>The <i>eido</i> tool validates any PEP against any schema</figcaption>
</figure>

## Introduction

The [base PEP specification](https://schema.databio.org/pep/2.0.0.yaml) has few requirements, so PEPs can represent very different data types. A PEP that satisfies the base specification will work with general PEP tools, but a more specialized tool may need to impose additional requirements. To extend the PEP specification to specialized use cases, PEP provides a powerful validation framework. This allows tool authors to define a *schema* that specifies which attributes are required, which are optional, what their types are, which attributes point to input files, and so on.

## Validating a generic PEP

The base PEP specification is hosted at [https://schema.databio.org/pep/2.0.0.yaml](https://schema.databio.org/pep/2.0.0.yaml). You can validate a PEP against a PEP schema using the [eido Python package](http://eido.databio.org) like this:

```
eido validate path/to/your/PEP_config.yaml -s https://schema.databio.org/pep/2.0.0.yaml
```

This command will ensure that your metadata follows basic PEP format. That may be all you need, or you may need to validate it against a more specialized schema for a particular analysis.

## Validating a PEP for a specific tool

Most tools will require more attributes than a base PEP provides. For example, a tool may require a `genome` attribute for each sample and we need to validate a PEP against a stricter schema. You would do this in the same way, just using the more specialized schema:

```console
eido validate path/to/project_config.yaml -s SCHEMA
```

Where SCHEMA is a URL or local file. The author of the tool you are using should provide this schema so that you can make sure you are providing the correct metadata for the tool.


## Writing a schema

If you developing a PEP-compatible tool, we recommend you write a PEP schema that describes what sample and project attributes are required for your tool to work. A detailed guide for writing your own schema can be found in the [eido documentation](http://eido.databio.org/en/latest/writing-a-schema/).
