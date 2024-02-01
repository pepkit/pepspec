# <img src="../img/divvy_logo.svg" class="img-header"> python tutorial

## Compute packages

When you start `divvy`, you may provide a configuration file that specifies one or more *compute packages*. A compute package is just a set of a variables that contains information needed to run a job, such as a job submission template, the command that you use to submit a job (*e.g.* `sbatch` or `qsub`), and any other variables needed to fill the template (*e.g.* `partition` or `account`). You can find out [how to write your own divvy config file](../configuration), but for this tutorial, we'll just use the default.

Start by importing `divvy`, and then create a new `ComputingConfiguration` object. If you provide no arguments, you'll just get a few default packages:


```python
import divvy
dcc = divvy.ComputingConfiguration()

```

This loads up the default compute package, and we see that there are a few other packages available. We can explore the compute settings in the loaded (`default`) package like this: 


```python
dcc.compute
```




    submission_template: /home/nsheff/.local/lib/python3.5/site-packages/divvy/default_config/submit_templates/localhost_template.sub
    submission_command: sh



Here you can see that a *compute package* is really a simple thing. In this case, it's just 2 key-value pairs. The `submission_template` key is a path to a template file, with these contents: 




```python
with open(dcc.compute.submission_template) as f:
    print(f.read())
```

    #!/bin/bash
    
    echo 'Compute node:' `hostname`
    echo 'Start time:' `date +'%Y-%m-%d %T'`
    
    {CODE} | tee {LOGFILE}
    


We can populate this simple template by passing values for the `{VARIABLE}` text in the template:


```python
dcc.write_script("test_local.sub", {"code": "run-this-command", "logfile": "logfile.txt"})
```

    Writing script to /home/nsheff/code/divvy/docs_jupyter/test_local.sub





    'test_local.sub'



Now let's look at the contents of our populated template:


```python
with open("test_local.sub") as f:
    print(f.read())
```

    #!/bin/bash
    
    echo 'Compute node:' `hostname`
    echo 'Start time:' `date +'%Y-%m-%d %T'`
    
    run-this-command | tee logfile.txt
    


This function opens the template specified by the `submission_template` variable in the compute package, and then populates any template variables with values from the compute package. The original `{CODE}` and `{LOGFILE}` has been replaced by the variables we passed to `write_script()`.

The other variable in the compute package is `submission_command`, which contains the shell instruction that would be used to submit this populated template; in this case, it's simply `sh` to run this script in the console. We can activate a different *compute_package* like this: 


```python
dcc.activate_package("slurm")
```

    Activating compute package 'slurm'





    True



It returns 'True' to indicate that the activation has been successful. This will change our settings. Let's inspect the new package:


```python
dcc.compute
```




    submission_template: /home/nsheff/.local/lib/python3.5/site-packages/divvy/default_config/submit_templates/slurm_template.sub
    submission_command: sbatch



Now that we've activated the package of interest, let's take a peek at the now-active `submission_template`:


```python
with open(dcc.compute.submission_template) as f:
    print(f.read())
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
    


In this template there are a lot more variables to populate. If we don't populate them all, they will just be left in the template. Let's pass a value for the `code` variable and see how this changes the submission script output:


```python
s = dcc.write_script("test_script.sub", {"code":"yellow"})
```

    Writing script to /home/nsheff/code/divvy/docs_jupyter/test_script.sub


Here's the output. Notice that the `{CODE}` variable has been replaced with the word `yellow`:


```python
with open("test_script.sub") as f:
    print(f.read())
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
    
    yellow
    


## Using a priority list of variables

Now, you can also pass more than one `Dict` object, in priority order, by just passing a list. Here, we'll pass 2 dicts, and any values in the 1st will override values in the 2nd:


```python
s = dcc.write_script("test_script.sub", [{"code":"red"}, {"code": "yellow", "time": "now"}])
```

    Writing script to /home/nsheff/code/divvy/docs_jupyter/test_script.sub



```python
with open("test_script.sub") as f:
    print(f.read())
```

    #!/bin/bash
    #SBATCH --job-name='{JOBNAME}'
    #SBATCH --output='{LOGFILE}'
    #SBATCH --mem='{MEM}'
    #SBATCH --cpus-per-task='{CORES}'
    #SBATCH --time='now'
    #SBATCH --partition='{PARTITION}'
    #SBATCH -m block
    #SBATCH --ntasks=1
    
    echo 'Compute node:' `hostname`
    echo 'Start time:' `date +'%Y-%m-%d %T'`
    
    red
    


In this case the value `red` took priority for the `code` variable, because it came first; but `time` was not overwritten in the first entry, so it is maintained. This allows for a cascading cumulative priority variable replacement.
