#!/usr/bin/env python3
"""Validate docs/data/publications.yaml for pepspec.

Modes:
    python validate_publications.py                       # structural only (no network)
    python validate_publications.py --check-dois          # + resolve every DOI
    python validate_publications.py --check-dois --only-changed
                                                          # + resolve only new DOIs

`--only-changed` diffs the working tree against `git show HEAD:<path>` and
network-checks only the DOIs that are new, so a PR does not re-verify every
legacy DOI on each push.

Exit code 0 = all valid, exit code 1 = errors found.
"""

import argparse
import re
import subprocess
import sys
import urllib.error
import urllib.parse
import urllib.request
from concurrent.futures import ThreadPoolExecutor, as_completed
from datetime import date
from pathlib import Path

import yaml

ROOT = Path(__file__).parent.resolve()
DATA = ROOT / "docs" / "data" / "publications.yaml"
DATA_REL = "docs/data/publications.yaml"
SOURCES = ROOT / "publication_sources.yaml"

REQUIRED = ("doi", "title", "authors", "year", "evidence", "added")
OPTIONAL = ("journal", "preprint_doi", "tools")

DOI_RE = re.compile(r"^10\.\d{4,9}/[-._;()/:a-z0-9]+$")
URL_PREFIX_RE = re.compile(r"^(https?://|doi:|dx\.doi\.org|doi\.org)", re.I)
ENTITY_RE = re.compile(r"&(#\d+|#x[0-9a-fA-F]+|[a-zA-Z][a-zA-Z0-9]{1,31});")
EVIDENCE_RE = re.compile(r"^(legacy|manual|cites:.+|fulltext:.+)$")
ADDED_RE = re.compile(r"^\d{4}-\d{2}-\d{2}$")

USER_AGENT = "pepspec-validate-publications (mailto:nsheff@databio.org)"


def normalize_title(title):
    return re.sub(r"[^a-z0-9]+", "", str(title).lower())


def load_vocabulary():
    if not SOURCES.exists():
        return None
    with open(SOURCES, encoding="utf-8") as fh:
        return set(yaml.safe_load(fh).get("tools") or [])


def load_publications(path):
    with open(path, encoding="utf-8") as fh:
        data = yaml.safe_load(fh)
    if not isinstance(data, dict):
        raise ValueError("top level of the file is not a YAML mapping")
    pubs = data.get("publications")
    if not isinstance(pubs, list):
        raise ValueError("top-level 'publications' key is missing or is not a list")
    return pubs


def check_text(errors, label, value):
    """No raw angle brackets and no HTML entities -- the renderer escapes."""
    text = str(value)
    if "<" in text or ">" in text:
        errors.append(f"{label} contains a raw '<' or '>': {text!r}")
    m = ENTITY_RE.search(text)
    if m:
        errors.append(f"{label} contains the HTML entity {m.group(0)!r}: {text!r}")


def validate(pubs, vocabulary):
    """Structural validation. Returns a list of error strings."""
    errors = []
    seen_dois = {}
    seen_titles = {}
    next_year = date.today().year + 1

    for i, pub in enumerate(pubs, start=1):
        tag = f"entry #{i}"
        if not isinstance(pub, dict):
            errors.append(f"{tag}: not a YAML mapping")
            continue
        doi_raw = pub.get("doi")
        if isinstance(doi_raw, str):
            tag = f"entry #{i} ({doi_raw})"

        for key in REQUIRED:
            if pub.get(key) is None:
                errors.append(f"{tag}: missing required key '{key}'")

        unknown = set(pub) - set(REQUIRED) - set(OPTIONAL)
        if unknown:
            errors.append(f"{tag}: unknown key(s) {sorted(unknown)}")

        # doi / preprint_doi
        for key in ("doi", "preprint_doi"):
            value = pub.get(key)
            if value is None:
                continue
            if not isinstance(value, str):
                errors.append(f"{tag}: '{key}' must be a string")
                continue
            if URL_PREFIX_RE.match(value):
                errors.append(f"{tag}: '{key}' carries a URL prefix: {value!r}")
                continue
            if value != value.lower():
                errors.append(f"{tag}: '{key}' must be lowercase: {value!r}")
            if not DOI_RE.match(value.lower()):
                errors.append(f"{tag}: '{key}' is not a bare DOI: {value!r}")
            key_l = value.lower()
            if key_l in seen_dois:
                errors.append(
                    f"{tag}: duplicate DOI {key_l!r} (also on entry #{seen_dois[key_l]})"
                )
            else:
                seen_dois[key_l] = i

        # title / journal
        title = pub.get("title")
        if title is not None:
            check_text(errors, f"{tag}: 'title'", title)
            norm = normalize_title(title)
            if norm and norm in seen_titles:
                errors.append(
                    f"{tag}: duplicate title (also on entry #{seen_titles[norm]}): {title!r}"
                )
            else:
                seen_titles[norm] = i
        journal = pub.get("journal")
        if journal is not None:
            check_text(errors, f"{tag}: 'journal'", journal)

        # authors
        authors = pub.get("authors")
        if authors is not None and not isinstance(authors, str):
            errors.append(f"{tag}: 'authors' must be a display string, not a list")

        # year
        year = pub.get("year")
        if year is not None:
            if not isinstance(year, int) or isinstance(year, bool):
                errors.append(f"{tag}: 'year' must be an integer, got {year!r}")
            elif not (1990 <= year <= next_year):
                errors.append(f"{tag}: 'year' {year} outside 1990..{next_year}")

        # tools
        tools = pub.get("tools")
        if tools is not None:
            if not isinstance(tools, list):
                errors.append(f"{tag}: 'tools' must be a list")
            elif vocabulary is not None:
                for tool in tools:
                    if tool not in vocabulary:
                        errors.append(
                            f"{tag}: tool {tool!r} is not in the "
                            f"publication_sources.yaml vocabulary"
                        )

        # evidence
        evidence = pub.get("evidence")
        if evidence is not None and not EVIDENCE_RE.match(str(evidence)):
            errors.append(
                f"{tag}: 'evidence' must be legacy, manual, cites:<doi>, or "
                f"fulltext:<id>; got {evidence!r}"
            )

        # added
        added = pub.get("added")
        if added is not None:
            text = added.isoformat() if isinstance(added, date) else str(added)
            if not ADDED_RE.match(text):
                errors.append(f"{tag}: 'added' must be an ISO date, got {added!r}")

    return errors


def _get(url, method="GET", timeout=15):
    req = urllib.request.Request(url, method=method)
    req.add_header("User-Agent", USER_AGENT)
    req.add_header("Accept", "application/json")
    return urllib.request.urlopen(req, timeout=timeout)


def resolve_doi(doi, timeout=15):
    """Crossref, then DataCite, then doi.org. Returns (doi, ok, message)."""
    quoted = urllib.parse.quote(doi, safe="")
    try:
        with _get(f"https://api.crossref.org/works/{quoted}", timeout=timeout) as resp:
            if resp.status == 200:
                return (doi, True, "verified on Crossref")
    except urllib.error.HTTPError as e:
        if e.code not in (404, 400):
            return (doi, True, f"Crossref inconclusive (HTTP {e.code})")
    except Exception as e:
        return (doi, True, f"Crossref inconclusive (network error: {e})")

    try:
        with _get(f"https://api.datacite.org/dois/{quoted}", timeout=timeout) as resp:
            if resp.status == 200:
                return (doi, True, "verified on DataCite")
    except urllib.error.HTTPError as e:
        if e.code not in (404, 400):
            return (doi, True, f"DataCite inconclusive (HTTP {e.code})")
    except Exception as e:
        return (doi, True, f"DataCite inconclusive (network error: {e})")

    try:
        with _get(f"https://doi.org/{doi}", method="HEAD", timeout=timeout) as resp:
            if 200 <= resp.status < 400:
                return (doi, True, f"resolved via doi.org (HTTP {resp.status})")
            return (doi, False, f"doi.org returned HTTP {resp.status}")
    except urllib.error.HTTPError as e:
        if 200 <= e.code < 400:
            return (doi, True, f"resolved via doi.org (HTTP {e.code})")
        return (doi, False, f"does not resolve (doi.org HTTP {e.code})")
    except Exception as e:
        return (doi, False, f"does not resolve (doi.org error: {e})")


def collect_dois(pubs):
    dois = []
    for pub in pubs:
        if not isinstance(pub, dict):
            continue
        for key in ("doi", "preprint_doi"):
            value = pub.get(key)
            if isinstance(value, str) and value.strip():
                dois.append(value.strip().lower())
    return dois


def previous_dois():
    """DOIs in HEAD's copy of the data file, or None if it cannot be read."""
    try:
        blob = subprocess.run(
            ["git", "show", f"HEAD:{DATA_REL}"],
            cwd=ROOT,
            capture_output=True,
            check=True,
        ).stdout.decode("utf-8")
    except Exception:
        return None
    try:
        data = yaml.safe_load(blob)
        return set(collect_dois(data["publications"]))
    except Exception:
        return None


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--check-dois", action="store_true", help="verify that DOIs resolve"
    )
    parser.add_argument(
        "--only-changed",
        action="store_true",
        help="with --check-dois, only verify DOIs that are new versus HEAD",
    )
    args = parser.parse_args()

    print(f"Validating {DATA_REL}...")

    try:
        pubs = load_publications(DATA)
    except FileNotFoundError:
        print(f"  ERROR {DATA_REL} does not exist")
        sys.exit(1)
    except Exception as e:
        print(f"  ERROR {e}")
        sys.exit(1)

    vocabulary = load_vocabulary()
    if vocabulary is None:
        print("  WARN  publication_sources.yaml not found; skipping tool vocabulary check")

    errors = validate(pubs, vocabulary)
    if errors:
        for msg in errors:
            print(f"  ERROR {msg}")
    else:
        print(f"  OK    {len(pubs)} entries, structure valid")

    doi_errors = 0
    if args.check_dois:
        dois = sorted(set(collect_dois(pubs)))
        if args.only_changed:
            previous = previous_dois()
            if previous is None:
                print("  WARN  could not read HEAD's copy; checking every DOI")
            else:
                dois = [d for d in dois if d not in previous]
        if not dois:
            print("  OK    no DOIs to verify")
        else:
            print(f"\nResolving {len(dois)} DOIs...")
            failures = []
            with ThreadPoolExecutor(max_workers=4) as pool:
                futures = [pool.submit(resolve_doi, d) for d in dois]
                for future in as_completed(futures):
                    doi, ok, msg = future.result()
                    if not ok:
                        failures.append((doi, msg))
            for doi, msg in sorted(failures):
                print(f"  ERROR {doi}: {msg}")
            doi_errors = len(failures)
            print(f"  {len(dois) - doi_errors} resolved, {doi_errors} failed")

    total = len(errors) + doi_errors
    print(f"\nValidation complete: {total} errors")
    if total:
        sys.exit(1)


if __name__ == "__main__":
    main()
