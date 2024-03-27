# PEPHubClient CLI (phc)

Installing PEPHubClient provides a CLI through the `phc` command. It provides a set of commands to interact with PEPhub.

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