# How to Run a Pipeline

You first have to [define your project](defining-a-project.md) and a [config file](looper-config.md). This will give you a PEP linked to a pipeline via a [pipeline interface](writing-a-pipeline-interface.md). Next, we'll run the pipeline.

The basic command is `looper run`. To run your pipeline, just:

```console
looper run --config .your_looper_config.yaml
```

This will submit a job for each sample. That's basically all there is to it; after this, there's a lot of powerful options and tweaks you can do to control your jobs. Here we'll just mention a few of them.

- **Dry runs**. You can use `-d, --dry-run` to create the job submission scripts, but not actually run them. This is really useful for testing that everything is set up correctly before you commit to submitting hundreds of jobs.
- **Limiting the number of jobs**. You can `-l, --limit` to test a few before running all samples. You can also use the `--selector-*` arguments to select certain samples to include or exclude.
- **Grouping jobs**. You can use `-u, --lump`, `-n, --lumpn`, `-j, --lumpj` to group jobs. [More details on grouping jobs](grouping-jobs.md).
- **Changing compute settings**. You can use `-p, --package`, `-s, --settings`, or `--compute` to change the compute templates. Read more in [running on a cluster](running-on-a-cluster.md).
- **Time delay**. You can stagger submissions to not overload a submission engine using `--time-delay`.
- **Use rerun to resubmit jobs**. To run only jobs that previously failed, try `looper rerun`.
- **Tweak the command on-the-fly**. The `--command-extra` arguments allow you to pass extra arguments to every command straight through from looper. See [parameterizing pipelines](parameterizing-pipelines.md).

# Running Multiple pipelines

To run more than one pipeline, simply specify pipeline interfaces in the looper config file:

```yaml
pep_config: pephub::databio/looper:default
output_dir: "$HOME/hello_looper-master/output"
pipeline_interfaces:
  sample: "$HOME/hello_looper-master/pipeline/pipeline_interface"
  project: "$HOME/hello_looper-master/project/pipeline"
```

You can also link to the pipeline interface with a sample attribute. If you want the same pipeline to run on all samples, it's as easy as using an `append` modifier like this:

```
sample_modifiers:
  append:
    pipeline_interfaces: "test.yaml"
```

But if you want to submit different samples to different pipelines, depending on a sample attribute, like `protocol`, you can use an implied attribute:

```
sample_modifiers:
  imply:
    - if:
        protocol: [PRO-seq, pro-seq, GRO-seq, gro-seq] # OR
      then:
        pipeline_interfaces: ["peppro.yaml"]
```

This approach uses only functionality of PEPs to handle the connection to pipelines as sample attributes, which provides full control and power using the familiar sample modifiers. It completely eliminates the need for re-inventing this complexity within looper, which eliminated the protocol mapping section to simplify the looper pipeline interface files. You can read more about the rationale of this change in [issue 244](https://github.com/pepkit/looper/issues/244#issuecomment-611154594).


# Pass Extra Command-Line Arguments

Occasionally, a particular project needs to run a particular flavor of a pipeline. How can you  adjust pipeline arguments for just this project? You can use looper *command extras* to solve this problem. Command extras let you pass any string on to the pipeline, which will be appended to the command.

There are 2 ways to use command extras: for sample pipelines, or for project pipelines:

## 1. Sample pipeline command extras

### Adding sample command extras via sample attributes

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

### Adding sample command extras via the command line

You can also pass extra arguments using `--command-extra` like this:

```
looper run project_config.yaml --command-extra="--flavor-flag"
```

## 2. Project pipeline command extras

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


## Overriding PEP-based command extras

By default, the CLI extras are *appended to the command_extra specified in your PEP*. If you instead want to *override* the command extras listed in the PEP, you can instead use `--command-extra-override`.

So, for example, make your looper call like this:

```bash
looper run --command-extra-override="-R"
```

That will remove any defined command extras and append `-R` to the end of any commands created by looper.
