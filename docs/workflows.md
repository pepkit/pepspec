# Using PEP with workflows systems

PEP is designed to be used with *any* workflow system. It is a common way of organizing sample metadata that spans individual workflows and even workflow systems. In practice, we have worked with several workflow systems to try to make it particularly easy to adopt PEP with your existing system.

## Snakemake

Snakemake has a built-in directive for reading PEPs. For an example of how to read a PEP into a Snakemake flow, see: 

- [PEP Snakemake example](https://github.com/pepkit/pep-snakemake)

## CWL

Using our pipeline submission engine [looper](http://looper.databio.org), it is possible to run CWL pipelines on each sample in a PEP. This example repository shows how to do it: 

- [PEP CWL example](https://github.com/pepkit/pep-cwl)

## Pypiper

Pypiper is our python-based pipeline manager. It is also PEP-compatible:

- [PEP Pypiper example](https://github.com/pepkit/pep-pypiper)