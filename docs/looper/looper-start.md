[looper_start]: img/looper_start.svg
# Looper - Getting Started

To begin using Looper, it is important to understand the **three** components required to execute looper.


![looper_start][looper_start]


### Project (PEP)
Looper requires your sample list to be in [PEP format](http://pepkit.github.io). This format generally consists of two files:
   - Csv containing the list of samples
   - A PEP project config which is a yaml file with information about you project.
See more here: [Defining a project](defining-a-project.md)

### Pipeline Interface
A Pipeline Interface points to the pipeline you wish to submit your samples to and contains additional submission information for looper to pass to the pipeline, e.g. file name.
See more here: [Pipeline interface](pipeline-interface-specification.md)

### Looper Configuration
The looper configuration file contains important information about the looper project. 
It points to the PEP project (via `pep_config`). It allows the user to supply the pipeline interfaces.

See more here: [Looper config](looper-config.md)


To get started running a simple looper example, check out our Hello World example here: [Hello World](code/hello-world.md)