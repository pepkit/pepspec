[![PEP compatible](https://pepkit.github.io/img/PEP-compatible-green.svg)](https://pepkit.github.io)
![Run pytests](https://github.com/pepkit/pephubclient/workflows/Run%20pytests/badge.svg)
[![codecov](https://codecov.io/gh/pepkit/pephubclient/branch/dev/graph/badge.svg)](https://codecov.io/gh/pepkit/pephubclient)
[![pypi-badge](https://img.shields.io/pypi/v/pephubclient)](https://pypi.org/project/pephubclient)
[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)
[![GitHub source](https://img.shields.io/badge/source-github-354a75?logo=github)](https://github.com/pepkit/pephubclient)



# PEPHubClient

`PEPHubClient` is a tool to provide Python API and CLI for [PEPhub](https://pephub.databio.org).

`pephubclient` features:

- `push` (upload projects)
- `pull` (download projects)

Additionally, our client supports pephub authorization.
The authorization process is based on pephub device authorization protocol.
To upload projects or to download private projects, user must be authorized through pephub.

If you want to use your own pephub instance, you can specify it by setting `PEPHUB_BASE_URL` environment variable.
e.g. `export PEPHUB_BASE_URL=https://pephub.databio.org` (This is original pephub instance)

To login, use the `login` argument; to logout, use `logout`.

----
```text
$ phc --help
                                                                                                                   
 Usage: pephubclient [OPTIONS] COMMAND [ARGS]...                                                                   
                                                                                                                   
╭─ Options ───────────────────────────────────────────────────────────────────────────────────────────────────────╮
│ --version             -v                                                                                        │
│ --install-completion            Install completion for the current shell.                                       │
│ --show-completion               Show completion for the current shell, to copy it or customize the              │
│                                 installation.                                                                   │
│ --help                          Show this message and exit.                                                     │
╰─────────────────────────────────────────────────────────────────────────────────────────────────────────────────╯
╭─ Commands ──────────────────────────────────────────────────────────────────────────────────────────────────────╮
│ login               Login to PEPhub                                                                             │
│ logout              Logout                                                                                      │
│ pull                Download and save project locally.                                                          │
│ push                Upload/update project in PEPhub                                                             │
╰─────────────────────────────────────────────────────────────────────────────────────────────────────────────────╯
```

```text
$ phc pull --help
                                                                                                                   
 Usage: pephubclient pull [OPTIONS] PROJECT_REGISTRY_PATH                                                          
                                                                                                                   
 Download and save project locally.                                                                                
                                                                                                                   
╭─ Arguments ─────────────────────────────────────────────────────────────────────────────────────────────────────╮
│ *    project_registry_path      TEXT  [default: None] [required]                                                │
╰─────────────────────────────────────────────────────────────────────────────────────────────────────────────────╯
╭─ Options ───────────────────────────────────────────────────────────────────────────────────────────────────────╮
│ --force    --no-force      Overwrite project if it exists. [default: no-force]                                  │
│ --help                     Show this message and exit.                                                          │
╰─────────────────────────────────────────────────────────────────────────────────────────────────────────────────╯
```

```text
$ phc push --help
                                                                                                                   
 Usage: pephubclient push [OPTIONS] CFG                                                                            
                                                                                                                   
 Upload/update project in PEPhub                                                                                   
                                                                                                                   
╭─ Arguments ─────────────────────────────────────────────────────────────────────────────────────────────────────╮
│ *    cfg      TEXT  Project config file (YAML) or sample table (CSV/TSV)with one row per sample to constitute   │
│                     project                                                                                     │
│                     [default: None]                                                                             │
│                     [required]                                                                                  │
╰─────────────────────────────────────────────────────────────────────────────────────────────────────────────────╯
╭─ Options ───────────────────────────────────────────────────────────────────────────────────────────────────────╮
│ *  --namespace                        TEXT  Project namespace [default: None] [required]                        │
│ *  --name                             TEXT  Project name [default: None] [required]                             │
│    --tag                              TEXT  Project tag [default: None]                                         │
│    --force         --no-force               Force push to the database. Use it to update, or upload project.    │
│                                             [default: no-force]                                                 │
│    --is-private    --no-is-private          Upload project as private. [default: no-is-private]                 │
│    --help                                   Show this message and exit.                                         │
╰─────────────────────────────────────────────────────────────────────────────────────────────────────────────────╯

```