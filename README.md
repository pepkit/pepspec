# PEP-docs

This repository powers all the documentation for PEP-related tools, services, and standards.

Documentation is written using [mkdocs](https://www.mkdocs.org/) and themed with [material for mkdocs](https://squidfunk.github.io/mkdocs-material/). The repository has:

- `mkdocs.yml`: the primary configuration, as well as the structure of the documentation. 
- `/docs`: the markdown files. Each tool gets its own folder.

## How to write/update documentation

Each tool gets a `nav` section in `mkdocs.yml`, which maps to its own section/tab in the rendered documentation. So to add a new page, change titles, or change structure, edit `mkdocs.yml`. To edit the documentation itself, edit the `.md` documentation files in the subfolders under `/docs`.

### Prerequisites

```bash
pip install mkdocs-material mkdocstrings[python] mkdocs-jupyter
```

You'll also need to install the packages being documented (peppy, looper, pipestat, pypiper, geofetch, eido, yacman) for the API documentation to build correctly:

```bash
pip install peppy looper pipestat pypiper geofetch eido yacman
```


### Building locally for development

I recommend previewing your changes locally before deploying. You can get a hot-reload server going by cloning this repository, and then just running:

```bash
mkdocs serve
```

You can also use `mkdocs build` to build a portable local version of the docs.

The documentation now uses **mkdocstrings** for Python API documentation and **mkdocs-jupyter** for Jupyter notebooks. These plugins automatically generate documentation from the source code and render notebooks, so the build process is now a single step.


### Publishing updates

The documentation is published automatically upon commits to `master` using a GitHub Action, which runs `mkdocs gh-deploy`. This builds the docs, and pushes them to the `gh-pages` branch. This branch is then published with GitHub Pages. There's no need to do this locally, just let the action deploy the updates for you automatically.

## FAQ

### Python API Documentation

Python API documentation is now automatically generated using **mkdocstrings** during the build process. No separate script is needed. The API docs are defined in markdown files (e.g., `docs/peppy/code/python-api.md`) using the `:::` syntax:

```markdown
::: peppy.Project
    options:
      docstring_style: google
      show_source: true
```

This syntax tells mkdocstrings to extract and render the documentation for the specified class or function directly from the source code.

### Jupyter Notebooks

Jupyter notebooks are now rendered automatically using the **mkdocs-jupyter** plugin. Configure which notebooks to include in the `plugins` section of `mkdocs.yml`:

```yaml
plugins:
- mkdocs-jupyter:
    include:
      - peppy/notebooks/*.ipynb
      - looper/notebooks/*.ipynb
```

Notebooks are rendered directly from `.ipynb` files during the build - no conversion step is needed.

### CLI Usage Documentation

CLI usage documentation for geofetch can be updated manually when needed using the helper script:

```bash
python scripts/generate_cli_usage_docs.py
```

This script reads the template at `docs/geofetch/usage-template.md.tpl` and runs `geofetch --help` to generate `docs/geofetch/code/usage.md`. This only needs to be run when the CLI interface changes.

### Can we version the docs?

The individual tools are versioned independently, but the documentation is versioned with a suite version. Right now I'm only planning to publish a single version (the latest version), of all the docs. In the future, if the need arises, we can investigate pushing different versions to different branches, hosted under different URLs on github pages.
