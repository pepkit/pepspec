# Advanced pipeline configuration

## Running Multiple pipelines

To run more than one pipeline, specify multiple pipeline interfaces in the looper config file:

```yaml
pep_config: pephub::databio/looper:default
output_dir: "$HOME/hello_looper-master/output"
pipeline_interfaces:
  sample: "$HOME/hello_looper-master/pipeline/pipeline_interface"
  project: "$HOME/hello_looper-master/project/pipeline"
```

You can also link to the pipeline interface with a sample attribute. If you want the same pipeline to run on all samples, it's as easy as using an `append` modifier like this:

```yaml
sample_modifiers:
  append:
    pipeline_interfaces: "test.yaml"
```

But if you want to submit different samples to different pipelines, depending on a sample attribute, like `protocol`, you can use an implied attribute:

```yaml
sample_modifiers:
  imply:
    - if:
        protocol: [PRO-seq, pro-seq, GRO-seq, gro-seq] # OR
      then:
        pipeline_interfaces: ["peppro.yaml"]
```

This approach uses only functionality of PEPs to handle the connection to pipelines as sample attributes, which provides full control and power using the familiar sample modifiers. It completely eliminates the need for re-inventing this complexity within looper, which eliminated the protocol mapping section to simplify the looper pipeline interface files. You can read more about the rationale of this change in [issue 244](https://github.com/pepkit/looper/issues/244#issuecomment-611154594).


## Passing extra command-line arguments

Occasionally, a particular project needs to run a particular flavor of a pipeline. How can you  adjust pipeline arguments for just this project? You can use looper *command extras* to solve this problem. Command extras let you pass any string on to the pipeline, which will be appended to the command.

There are 2 ways to use command extras: for sample pipelines, or for project pipelines:

### 1. Sample pipeline command extras

#### Adding sample command extras via sample attributes

Looper uses a reserved sample attribute called `command_extras`, which you can set using general PEP sample modifiers however you wish. For example, if your extras are the same for all samples you could use an `append` modifier:


```yaml
sample_modifiers:
  append:
    command_extra: "--flavor-flag"
```

This will add `--flavor-flag` the end of the command looper constructs. If you need to modulate the extras depending on another attribute value, you could use an imply modifier:

```yaml
sample_modifiers:
  imply:
    - if:
        protocol: "rrbs"
      then:
        command_extra: "-C flavor.yaml --epilog"
```

#### Adding sample command extras via the command line

You can also pass extra arguments using `--command-extra` like this:

```
looper run project_config.yaml --command-extra="--flavor-flag"
```

### 2. Project pipeline command extras

For *project pipelines*, you can specify command extras in the `looper` section of the PEP config:

```yaml
looper:
  output_dir: "/path/to/output_dir"
  cli:
    runp:
      command-extra: "--flavor"
```

or as an argument to the `looper runp` command:


```bash
looper runp project_config.yaml --command-extra="--flavor-flag"
```


### Overriding PEP-based command extras

By default, the CLI extras are *appended to the command_extra specified in your PEP*. If you instead want to *override* the command extras listed in the PEP, you can instead use `--command-extra-override`.

So, for example, make your looper call like this:

```bash
looper run --command-extra-override="-R"
```

That will remove any defined command extras and append `-R` to the end of any commands created by looper.


## Grouping many jobs into one

By default, `looper` will translate each row in your `sample_table` into a single job. But perhaps you are running a project with tens of thousands of rows, and each job only takes mere minutes to run; in this case, you'd rather just submit a single job to process many samples. `Looper` makes this easy with the `--lump` and `--lumpn` command line arguments.

### Lumping jobs by job count: `--lumpn`

It's quite simple: if you want to run 100 samples in a single job submission script, just tell looper `--lumpn 100`.

### Lumping jobs by input file size: `--lump`

But what if your samples are quite different in terms of input file size? For example, your project may include many small samples, which you'd like to lump together with 10 jobs to 1, but you also have a few control samples that are very large and should have their own dedicated job. If you just use `--lumpn` with 10 samples per job, you could end up lumping your control samples together, which would be terrible. To alleviate this problem, `looper` provides the `--lump` argument, which uses input file size to group samples together. By default, you specify an argument in number of gigabytes. Looper will go through your samples and accumulate them until the total input file size reaches your limit, at which point it finalizes and submits the job. This will keep larger files in independent runs and smaller files grouped together.

### Lumping jobs by input file size: `--lumpj`

Or you can lump samples into number of jobs.

