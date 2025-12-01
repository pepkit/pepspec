
# Installing pipestat

### Minimal install for file backend

Install pipestat from PyPI with `pip`: 

```
pip install pipestat
```

Confirm installation by calling `pipestat -h` on the command line. If the `pipestat` executable is not in your `$PATH`, append this to your `.bashrc` or `.profile` (or `.bash_profile` on macOS):

```console
export PATH=~/.local/bin:$PATH
```

### Optional dependencies for database backend

Pipestat can use either a file or a database as the backend for recording results. The default installation only provides file backend. To install dependencies required for the database backend:

```
pip install pipestat['dbbackend']
```

### Optional dependencies for pipestat reader

To install dependencies for the included `pipestatreader` submodule:

```
pip install pipestat['pipestatreader']
```