# <img src="../img/divvy_logo.svg" class="img-header"> command-line tutorial

`Divvy` also provides a command-line interface that gives you the same power as the python API. You can use `--help` to get a list of the command-line options:


```bash
divvy --help
```

    version: 0.5.0
    usage: divvy [-h] [--version] [--verbosity V] [--silent] [--logdev]
                 {write,init,list,submit} ...
    
    divvy - write compute job scripts that can be submitted to any computing
    resource
    
    positional arguments:
      {write,init,list,submit}
        write               Write a job script
        init                Initialize a new divvy config file
        list                List available compute packages
        submit              Write and then submit a job script
    
    optional arguments:
      -h, --help            show this help message and exit
      --version             show program's version number and exit
      --verbosity V         Set logging level (1-5 or logging module level name)
      --silent              Silence logging. Overrides verbosity.
      --logdev              Expand content of logging message format.
    
    https://divvy.databio.org


# The `list` command

Let's first use `divvy list` to show us our available computing packages:


```bash
divvy list
```

    Using default config. No config found in env var: ['DIVCFG', 'PEPENV']
    Using divvy config: /home/nsheff/.local/lib/python2.7/site-packages/divvy/default_config/divvy_config.yaml
    Available compute packages:
    
    default
    slurm
    singularity_slurm
    singularity
    local
    docker




# The `write` command

Use `divvy write` to actually write a new script using a template. To do this, you'll need to provide 3 things: a template (which comes from your compute package), a settings file with variables, and an outfile.


## The settings file

The settings argument is where you can pass an existing `yaml` file with key-value pairs. Here's a simple example:


```bash
cat settings.yaml
```

    time: 4-0-0
    logfile: results.log
    cores: 6
    partition: large_mem
    mem: 16G


Now let's take a look at the template we are going to use by activating the `slurm` package


```bash
cat ../divvy/default_config/divvy_templates/slurm_template.sub
```

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
    
    {CODE}


We use `divvy` to populate that template with our list of variables above, like this:


```bash
divvy write -p slurm -s settings.yaml -o test.sub
```

    Using default config. No config found in env var: ['DIVCFG', 'PEPENV']
    Using divvy config: /home/nsheff/.local/lib/python2.7/site-packages/divvy/default_config/divvy_config.yaml
    Activating compute package 'slurm'
    Loading settings file: settings.yaml
    Writing script to /home/nsheff/code/divvy/docs_jupyter/test.sub


Now we can take a look at what our sbumission scripts looks like.


```bash
cat test.sub
```

    #!/bin/bash
    #SBATCH --job-name='{JOBNAME}'
    #SBATCH --output='results.log'
    #SBATCH --mem='16G'
    #SBATCH --cpus-per-task='6'
    #SBATCH --time='4-0-0'
    #SBATCH --partition='large_mem'
    #SBATCH -m block
    #SBATCH --ntasks=1
    
    echo 'Compute node:' `hostname`
    echo 'Start time:' `date +'%Y-%m-%d %T'`
    
    {CODE}


We populated several variables, like `{LOGFILE}` and `{TIME}`, from the `settings.yaml` file. However, the `{CODE}` and `{JOBNAME}` variables are still unpopulated, so this submission script is incomplete. To remedy this, we'll use `divvy`'s command-line variable passing: any non-interpreted arguments passed to `divvy` are assumed to be variables to populate the template. These command-line variables are considered highest priority and so will override any values in the more distant locations. For example:


```bash
divvy write -p slurm -s settings.yaml -o test.sub -c code=run-this-cmd jobname=12345 time=6-0-0
```

    Using default config. No config found in env var: ['DIVCFG', 'PEPENV']
    Using divvy config: /home/nsheff/.local/lib/python2.7/site-packages/divvy/default_config/divvy_config.yaml
    Activating compute package 'slurm'
    Loading settings file: settings.yaml
    Writing script to /home/nsheff/code/divvy/docs_jupyter/test.sub



```bash
cat test.sub
```

    #!/bin/bash
    #SBATCH --job-name='12345'
    #SBATCH --output='results.log'
    #SBATCH --mem='16G'
    #SBATCH --cpus-per-task='6'
    #SBATCH --time='6-0-0'
    #SBATCH --partition='large_mem'
    #SBATCH -m block
    #SBATCH --ntasks=1
    
    echo 'Compute node:' `hostname`
    echo 'Start time:' `date +'%Y-%m-%d %T'`
    
    run-this-cmd


Now we have a complete script, which we can run with `sbatch test.sub`. Notice also that the `time` variable uses the one provided on the CLI rather than the one provided in the `settings.yaml` file, because the CLI has a higher priority.

Variables can come from these 3 sources, in order of increasing priority: 1) compute package (defined in the `divvy` configuration file and selected with the `-p` or `--package` argument); 2) `settings.yaml` file, passed with `-s` or `--settings`; 3) any additional variables passed on the command line as key-value pairs to `-c`.

# Submitting jobs

Let's try actually submitting these jobs with `divvy submit`:


```bash
divvy submit -p slurm -s settings.yaml -o test.sub -c code=run-this-cmd jobname=12345 time=6-0-0
```

    Using default config. No config found in env var: ['DIVCFG', 'PEPENV']
    Using divvy config: /home/nsheff/.local/lib/python2.7/site-packages/divvy/default_config/divvy_config.yaml
    Activating compute package 'slurm'
    Loading settings file: settings.yaml
    Writing script to /home/nsheff/code/divvy/docs_jupyter/test.sub
    sbatch test.sub
    sh: 1: sbatch: not found


The *slurm* package uses `sbatch` as its `submission_command`, but since I'm running this locally, it won't run as I have no `sbatch` command available. Let's try `local` instead:


```bash
divvy submit -p local -s settings.yaml -o test.sub -c code=ls
```

    Using default config. No config found in env var: ['DIVCFG', 'PEPENV']
    Using divvy config: /home/nsheff/.local/lib/python2.7/site-packages/divvy/default_config/divvy_config.yaml
    Activating compute package 'local'
    Loading settings file: settings.yaml
    Writing script to /home/nsheff/code/divvy/docs_jupyter/test.sub
    sh test.sub
    Compute node: zither
    Start time: 2020-05-19 07:46:03
    build
    cli.ipynb
    debug.ipynb
    results.log
    settings.yaml
    test_local.sub
    test_script.sub
    test.sub
    tutorial.ipynb


There I switched the command to `ls`, which shows you a result of everything on this computer.
