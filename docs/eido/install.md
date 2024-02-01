# Installing eido

Install from [GitHub releases](https://github.com/pepkit/eido/releases) or from PyPI using `pip`:

- `pip install --user eido`: install into user space.
- `pip install --user --upgrade eido`: update in user space.
- `pip install eido`: install into an active virtual environment.
- `pip install --upgrade eido`: update in virtual environment.

See if your install worked by calling `eido -h` on the command line. If the `eido` executable in not in your `$PATH`, append this to your `.bashrc` or `.profile` (or `.bash_profile` on macOS):

```{console}
export PATH=~/.local/bin:$PATH
```
