# Setting up pipestat

## Introduction

Pipestat is a tool used by pipelines to standardize reporting of pipeline results. For example, we are using the `count_lines.sh` pipeline to calculate the number of provinces in several countries. This number is a result of the pipeline. Our previous pipelines record the result by printing to the screen and log file. Pipestat will help us collect and aggregate those results in a clean way. 

Pipestat is a standalone tool.
It is not required to use looper, and it can also be used by pipelines that are not looper-compatible.
You can read the complete details about pipestat in the [pipestat documentation](../pipestat).
In this tutorial, we will wire up our simple pipeline with pipestat, and show how this lets use powerful reporting tools to view pipeline results nicely.

!!! success "Learning objectives"
    - What is pipestat? 
    - How can I configure my looper project to use pipestat effectively?
    - How can I make my pipeline store results in PEPhub?
    - Where are pipestat results saved? Can I use other databases?


---

- Show how to add pipestat reporting to the count_lines script. (maybe with the shell version, and then the Python version? Or just go straight to Python? I see the advantage of doing both, because then you demonstrate the CLI of pipestat)
- Show how to report results back into the PEP at PEPhub
- Show how to use `looper check` with the pipestat-compatible pipeline
- Show how to use `looper report`.


!!! tip "Summary"
    - Pipestat is a standalone tool that can be used with or without looper.
    - ...
    - ...

