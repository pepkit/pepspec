# This will auto-generate documentation for any packages listed in
# the lucidoc section of the mkdocs.yml file.

import lucidoc
import yaml


# Read the mkdocs config
with open("mkdocs.yml") as stream:
	cfg = yaml.safe_load(stream)

# Process auto-documented Python code
if "lucidoc" in cfg:
	for pkg, dest in cfg["lucidoc"].items():
		print(f"Documenting '{pkg}' at {dest}")
		lucidoc.run_lucidoc(pkg, "rst", outfile=f"docs/{dest}")

import glob
import nbconvert
import os
from pathlib import Path

# Render Juptyer notebooks to markdown
if "jupyter" in cfg:
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
