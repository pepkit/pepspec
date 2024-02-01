# Installing pipestat

Install pipestat from [GitHub releases](https://github.com/pepkit/pipestat/releases) or from PyPI with `pip`:

- `pip install --user pipestat`: install into user space.
- `pip install --user --upgrade pipestat`: update in user space.
- `pip install pipestat`: install into an active virtual environment.
- `pip install --upgrade pipestat`: update in virtual environment.

See if your installation worked by calling `pipestat -h` on the command line. If the `pipestat` executable is not in your `$PATH`, append this to your `.bashrc` or `.profile` (or `.bash_profile` on macOS):

Note: with version 0.6.0, Pipestat installs with minimum dependencies to report _only_ using the YAML-formatted backend (FileBackend). If desired, the user can install additional functionality:
database dependencies:  `pip install pipestat['dbbackend']`
pipestat reader: `pip install pipestat['pipestatreader']`

```console
export PATH=~/.local/bin:$PATH
```
