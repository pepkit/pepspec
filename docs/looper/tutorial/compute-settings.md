# Advanced compute configuration


## How to submit jobs to a cluster with <img src="../../img/divvy_logo.svg" height="25">

## Introduction

By default, `looper` will build a shell script for each sample and then run it sequentially on the local computer. This is convenient for simple cases, but when it comes time to scale up, this is where `looper` really excels. Looper uses a powerful [concentric template system](concentric-templates.md) that enables looper to run jobs on any cluster resource manager (like SLURM, SGE, LFS, etc.) by simply setting up a template for it. The environment templates are managed by `divvy`.

## What is `divvy`?

![Connect](img/divvy-connect.svg)

`Divvy` is `looper`'s job submission configuration tool.
Divvy is automatically installed when you install looper.
You can also use `divvy` independently from looper.
Divvy allows you to populate job submission scripts by integrating job-specific settings with separately configured computing environment settings.
Divvy helps you toggle among computing resources.

Without `divvy`, tools are tied to a particular compute resource setup. This makes it difficult to transfer to different environments. For tools that can run in multiple environments, each one must be configured separately. In contrast, `divvy`-compatible tools can run on any computing resource. **Users configure their computing environment once, and all divvy-compatible tools will use this same configuration.**


## Overview and basic example of cluster computing

To configure `divvy` (and therefore `looper`) for cluster computing, first create a `divvy` computing configuration file using `divvy init`. Looper looks for the divvy configuration file in the environment variable `$DIVCFG`, so it's best to set that up to point to your divvy configuration file, so you don't have to provide it every time you run `looper`. This `init` command will create a default config file, along with a folder of computing templates:

```bash
export DIVCFG="divvy_config.yaml"
divvy init -c $DIVCFG
```

Looper will now have access to your computing configuration. Add the `export...` line to your `.bashrc` or `.profile` to ensure the `DIVCFG` variable persists for future command-line sessions. 
You can override the `DIVCFG` environment variable by specifying a path with `--divvy` argument, like this:

```bash
looper run
  --divvy /path/to/divvy_cfg.yaml ...
```

On a fresh init, `divvy` comes pre-loaded with some built-in compute packages, which you can explore by typing `divvy list`. This will display the available compute packages:

```{console}
divvy list
```


```{console}
Divvy config: divvy_config.yaml

docker
default
singularity_slurm
singularity
local
slurm
```


For example, there's a package called 'slurm'. You select a package with `--package` (*e.g.* ). 

```bash
looper run
  --package slurm
```

For many systems (SLURM, SGE, LFS, etc), the default divvy configuration will work out of the box.
If you need to tweak things, the template system is flexible and you can override individual parameters using `--compute`, *e.g.*:

```bash
looper run
  --package slurm  
  --compute PARTITION=standard time='01-00:00:00' cores='32' mem='32000'
```

You can also add you own custom templates to tailor divvy to any compute environment.

## Customizing your configuration file

The *divvy configuration file* (`DIVCFG` for short) is a `yaml` file that specifies a user's available *compute packages*. Each compute package represents a computing resource; for example, by default we have a package called `local` that populates templates to simple run jobs in the local console, and another package called `slurm` with a generic template to submit jobs to a SLURM cluster resource manager. Users can customize compute packages as much as needed. 

Here is an example `divvy` configuration file:

```{console}
compute_packages:
  default:
    submission_template: templates/local_template.sub
    submission_command: sh
  local:
    submission_template: templates/local_template.sub
    submission_command: sh
  develop_package:
    submission_template: templates/slurm_template.sub
    submission_command: sbatch
    partition: develop
  big:
    submission_template: templates/slurm_template.sub
    submission_command: sbatch
    partition: bigmem
```

Each entry in `compute_packages` defines a separate package. If you don't specify a package to activate, `divvy` uses the package named `default`. You can make your default whatever you like. 
Each compute package must specify the `submission_command` and `submission_template` attributes. You can add whatever other attributes you want. 

### The `submission_command` attribute

The `submission_command` attribute is the string divvy will use to submit a job. For example, in our compute package named `develop_package`, we've set `submission_command` to `sbatch`. We are telling divvy that, when this package is activated, divvy should submit the job by running: `sbatch <submission_script.txt>`.

### The `submission_template` attribute

The `submission_template` attribute is a path to a template file. The template file provides a skeleton that `divvy` will populate with job-specific attributes. These paths can be relative or absolute; relative paths are considered *relative to the DIVCFG file*. Let's explore what template files look like next.

### Template files

Each compute package must point to a template file with the `submission_template` attribute. These template files are typically stored relative to the `divvy` configuration file. Template files are taken by `divvy`, populated with job-specific information, and then run as scripts. Here's an example of a generic SLURM template file:

```{bash}
#!/bin/bash
#SBATCH --job-name='{JOBNAME}'
#SBATCH --output='{LOGFILE}'
#SBATCH --mem='{MEM}'
#SBATCH --cpus-per-task='{CORES}'
#SBATCH --time='{TIME}'
#SBATCH --partition='{PARTITION}'
#SBATCH -m block
#SBATCH --ntasks=1

echo 'Compute node:' `hostname`
echo 'Start time:' `date +'%Y-%m-%d %T'`

srun {CODE}
```

Template files use variables (*e.g.* `{VARIABLE}`), which will be populated independently for each job. If you want to make your own templates, you can find examples in the [submit_templates](https://github.com/pepkit/divcfg/tree/master/templates) folder. Making your own templates gives `divvy` ultimate flexibility to work with any compute infrastructure in any environment. 

### Creating a custom compute package

To create a custom compute package and add it to divvy is easy:

1. Create your own template. Just follow the examples. It's a simple text file, with `{VARIBLE}` syntax for any job-specific variables.
2. Add a new compute package as an entry under `compute_packages` in your divvy config file.
3. Point to your custom template in the `submission_template` attribute of your new compute package.
4. Don't forget to add the appropriate `submission_command` for this package.

### Flexible template variables

Starting with `divvy v0.5.0` the configuration file can include an `adapters` section, which is used to provide a set of variable mappings that `divvy` uses to populate the submission templates.

This makes the connection with `divvy` and client software more flexible and more elegant, since the source of the data does not need to follow any particular naming scheme, any mapping can be used and adapted to work with any `divvy` templates.

## Example adapters section

```yaml
adapters:
  CODE: namespace.command
  LOGFILE: namespace1.log_file
  JOBNAME: user_settings.program.job_name
  CORES: processors_number
...
```

As you can see in the example `adapters` section above, each adapter is a key-value pair that maps a `divvy` template variable to a target value. The target values can use namespaces (nested mapping).

## Resources

You may notice that the compute config file does not specify resources to request (like memory, CPUs, or time). Yet, these are required in order to submit a job to a cluster. **Resources are not handled by the divcfg file** because they not relative to a particular computing environment; instead they vary by pipeline and sample. As such, these items should be provided elsewhere. 


Here are some [examples of divvy configuration files](http://github.com/pepkit/divcfg).


## Using divvy independently from the command-line

![Merge](img/divvy-merge.svg)

You can actually use `divvy` without using looper, to submit one-off jobs to a cluster. Divvy will take variables from a file or the command line, merge these with environment settings to create a specific job script. Write a submission script from the command line:

```{console}
divvy write --package slurm \
    --settings myjob.yaml \
    --compute sample=sample1 \
    --outfile submit_script.txt
```

## Python interface

You can also use `divvy` via Python interface, or you can use it to make your own Python tools divvy-compatible:

```{python}
import divvy
dcc = divvy.ComputingConfiguration()
dcc.activate_package("slurm")

# write out a submission script
dcc.write_script("test_script.sub", 
    {"code": "bowtie2 input.bam output.bam"})
```


