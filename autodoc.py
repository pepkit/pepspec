# This script will auto-generate documentation for Python code, CLI usage, and Jupyter notebooks
# It is intended to be run as a pre-build step in a MkDocs project
# It will read the mkdocs.yml file for configuration
# It will use the lucidoc package to auto-generate documentation for Python code
# It will use the subprocess package to run CLI commands and capture the output
# It will use the nbconvert package to convert Jupyter notebooks to markdown

import lucidoc
import yaml
import subprocess
import glob
import nbconvert
import os
from pathlib import Path

import argparse

parser = argparse.ArgumentParser(description="Description of your program")
parser.add_argument(
    "--x-usage",
    help="Exclude usage",
    required=False,
    default=False,
    action="store_true",
)
parser.add_argument(
    "--x-lucidoc",
    help="Exclude lucidoc",
    required=False,
    default=False,
    action="store_true",
)
parser.add_argument(
    "--x-jupyter",
    help="Exclude jupyter",
    required=False,
    default=False,
    action="store_true",
)

args = vars(parser.parse_args())

print(args)

# Read the mkdocs config
with open("mkdocs.yml") as stream:
    cfg = yaml.safe_load(stream)


if "autodoc" not in cfg:
    print("No autodoc configuration found in mkdocs.yml")
    exit(1)
else:
    cfg = cfg["autodoc"]

# Process auto-documented Python code
if args["x_lucidoc"] is False and "lucidoc" in cfg:
    for bundle in cfg["lucidoc"]:
        print(f"Documenting lucidoc '{bundle['pkg']}' at {bundle['outfile']}")
        lucidoc.run_lucidoc(parse_style="rst", **bundle)
else:
    print("Skipping lucidoc")


usage_tpl = """
\n`{cmd}`
\n
```console
{usage}
```
"""

# Process CLI usage
if args["x_usage"] is False and "cli_usage" in cfg:
    for item in cfg["cli_usage"]:
        result = ""
        with open(item["template"], "r") as file:
            result = file.read()
        for cmd in item["commands"]:
            print(f"Documenting command '{cmd}' to '{item['outfile']}'")
            usage = subprocess.check_output(cmd, shell=True).decode("utf-8")
            content = usage_tpl.format(cmd=cmd, usage=usage)
            result += content
        with open(item["outfile"], "w") as file:
            file.write(result)
else:
    print("Skipping usage documentation")

# # Render Juptyer notebooks to markdown
if args["x_jupyter"] is False and "jupyter" in cfg:
    for item in cfg["jupyter"]:
        files = glob.glob(f"docs/{item['in']}/*.ipynb")
        for nb in files:
            bn, _ = os.path.splitext(os.path.basename(nb))
            out = f"docs/{item['out']}/{bn}.md"
            print(f"Converting '{nb}' to '{out}'")
            md_result = nbconvert.exporters.export(nbconvert.MarkdownExporter(), nb)[0]
            Path(os.path.dirname(out)).mkdir(parents=True, exist_ok=True)
            with open(out, "w") as stream:
                stream.write(md_result)
else:
    print("Skipping jupyter notebooks")