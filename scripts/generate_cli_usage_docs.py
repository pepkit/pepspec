#!/usr/bin/env python3
"""
Generate geofetch CLI usage documentation.

Run manually when geofetch CLI interface changes:
    python scripts/generate_cli_usage_docs.py
"""
import subprocess

template = "docs/geofetch/usage-template.md.tpl"
outfile = "docs/geofetch/code/usage.md"
command = "geofetch --help"

print(f"Generating CLI usage documentation for: {command}")

with open(template) as f:
    result = f.read()

usage = subprocess.check_output(command, shell=True).decode("utf-8")
result += f"\n`{command}`\n\n```console\n{usage}\n```\n"

with open(outfile, "w") as f:
    f.write(result)

print(f"✓ Generated {outfile}")
