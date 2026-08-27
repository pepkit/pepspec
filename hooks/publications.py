"""Render docs/data/publications.yaml into the statistics page.

MkDocs native hook; registered under `hooks:` in mkdocs.yml.

The whole <ul> is emitted as one contiguous block of HTML with no blank
lines inside it. Python-Markdown passes top-level block HTML through
untouched, so titles containing `*` or `_` survive. A blank line inside
the block would break that and turn asterisks into emphasis.
"""

import html
import os

import yaml

MARKER = "<!-- publications-list -->"
PAGE = "statistics.md"
DATA = ("data", "publications.yaml")


def _entry_html(pub):
    authors = html.escape(str(pub["authors"]))
    title = html.escape(str(pub["title"]))
    year = pub["year"]
    doi = str(pub["doi"])
    journal = pub.get("journal")
    journal_html = f"<br><i>{html.escape(str(journal))}</i>. " if journal else "<br> "
    return (
        f"<li><b>{authors} ({year}). </b><i>{title}</i>"
        f"{journal_html}"
        f'<span class="doi">DOI: '
        f'<a href="https://doi.org/{doi}">{doi}</a></span></li>'
    )


def on_page_markdown(markdown, page, config, files):
    if page.file.src_uri != PAGE or MARKER not in markdown:
        return markdown
    path = os.path.join(config["docs_dir"], *DATA)
    with open(path, encoding="utf-8") as fh:
        pubs = yaml.safe_load(fh)["publications"]
    pubs.sort(key=lambda p: (-int(p["year"]), str(p["authors"]).lower()))
    items = "".join(_entry_html(p) for p in pubs)
    block = (
        f"<p><i>{len(pubs)} publications. "
        f"This list is updated monthly by an automated search; "
        f'see <a href="https://pep.databio.org/data/publications.yaml">'
        f"publications.yaml</a> for the machine-readable source.</i></p>\n"
        f'<ul class="publications">{items}</ul>'
    )
    return markdown.replace(MARKER, block)
