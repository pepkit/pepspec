# <img src="img/looper_logo.svg" class="img-header">

<p align="center">
<a href="https://pepkit.github.io/img/PEP-compatible-green.svg"><img src="https://pepkit.github.io/img/PEP-compatible-green.svg"></a>
<a href="https://github.com/pepkit/looper/actions/workflows/run-pytest.yml" alt="Run pytests"><img src="https://github.com/pepkit/looper/workflows/Run%20pytests/badge.svg"/></a>
<a href="https://img.shields.io/pypi/v/looper"><img src="https://img.shields.io/pypi/v/looper"></a>
<a href="https://github.com/pepkit/looper"><img src="https://img.shields.io/badge/source-github-354a75?logo=github"></a>
</p>

## What is looper?

Looper is a job submitting engine. Looper deploys arbitrary shell commands for each sample in a [standard PEP project](https://pepkit.github.io/docs/home/). You can think of looper as providing a single user interface to running, monitoring, and managing all of your sample-intensive research projects the same way, regardless of data type or pipeline used.

## What makes looper better?

Looper **decouples job handling from the pipeline process**. In a typical pipeline, job handling (managing how individual jobs are submitted to a cluster) is delicately intertwined with actual pipeline commands (running the actual code for a single compute job). In contrast, the looper approach is modular: looper *only* manages job submission. This approach leads to several advantages compared with the traditional integrated approach:

1. pipelines do not need to independently re-implement job handling code, which is shared.
2. every project uses a universal structure, so datasets can move from one pipeline to another.
3. users must learn only a single interface that works with any project for any pipeline.
4. running just one or two samples/jobs is simpler, and does not require a  distributed compute environment.




## Installing

Releases are posted as [GitHub releases](https://github.com/pepkit/looper/releases), or you can install using `pip`:


```console
pip install --user looper
```

Update with:

```console
pip install --user --upgrade looper
```

If the `looper` executable in not automatically in your `$PATH`, add the following line to your `.bashrc` or `.profile`:

```console
export PATH=~/.local/bin:$PATH
```

## Quick start

To test `looper`, follow the [Hello Looper example repository](https://github.com/databio/hello_looper) to run your first looper project:


```console
# download and unzip the hello_looper repository
wget https://github.com/databio/hello_looper/archive/master.zip
unzip master.zip

# Run looper:
cd hello_looper-master
looper run project/project_config.yaml
```

Detailed explanation of results is in the [Hello world tutorial](code/hello-world.md).
