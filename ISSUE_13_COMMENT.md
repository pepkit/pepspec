# Suggestion for Author Metadata in PEP Specification

After researching the PEP specification, pandoc frontmatter conventions, and existing practices, I'd like to propose a structured approach for adding author metadata to PEP.

## Background & Rationale

Adding authorship metadata serves several important purposes:
1. **Attribution & Credit**: Proper recognition for data creators in open science
2. **Traceability**: Clear provenance tracking for datasets
3. **Discoverability**: Enhanced metadata for searching and cataloging
4. **Interoperability**: Alignment with established standards (pandoc, scholarly markdown)

## Proposed Specification

### Location in PEP Structure

I recommend adding an **optional** `authors` field at the project level in the project config file (`project_config.yaml`). This aligns with the PEP philosophy of keeping the core simple while allowing optional enhancements.

### Author Metadata Format

Following pandoc frontmatter conventions (which are widely adopted in scholarly markdown), I propose supporting both simple and structured formats:

#### Simple Format (for basic use cases)
```yaml
pep_version: 2.1.0
sample_table: "samples.csv"
authors:
  - Nathan Sheffield
  - Michal Stolarczyk
  - Andre Rendeiro
```

#### Structured Format (recommended for full attribution)
```yaml
pep_version: 2.1.0
sample_table: "samples.csv"
authors:
  - name: Nathan Sheffield
    affiliation: University of Virginia
    email: nathan@example.org
    orcid: 0000-0001-5643-4068
    corresponding: true
  - name: Michal Stolarczyk
    affiliation: University of Virginia
    orcid: 0000-0002-5857-9560
  - name: Andre Rendeiro
    affiliation: CeMM Research Center
    orcid: 0000-0001-9362-5373
```

### Recommended Fields

The structured format would support these optional fields per author:

| Field | Type | Description | Example |
|-------|------|-------------|---------|
| `name` | string | **Required**. Full name of author | "Nathan Sheffield" |
| `affiliation` | string or list | Institution(s) | "University of Virginia" |
| `email` | string | Contact email | "nathan@example.org" |
| `orcid` | string | ORCID identifier | "0000-0001-5643-4068" |
| `url` | string | Personal or lab website | "https://databio.org" |
| `corresponding` | boolean | Corresponding author flag | true |
| `roles` | list | CRediT contributor roles | ["Conceptualization", "Data curation"] |

### Alternative: Institute References

For complex projects with many authors from the same institutions, an alternative format using institute references could be supported:

```yaml
pep_version: 2.1.0
sample_table: "samples.csv"
authors:
  - name: Nathan Sheffield
    affiliation: uva
    email: nathan@example.org
    orcid: 0000-0001-5643-4068
  - name: Michal Stolarczyk
    affiliation: uva
    orcid: 0000-0002-5857-9560

affiliations:
  uva:
    name: University of Virginia
    department: Center for Public Health Genomics
    city: Charlottesville
    country: USA
```

## Best Practices & Recommendations

### 1. ORCID as Primary Identifier
- **Recommendation**: Strongly encourage ORCID identifiers as the primary author ID
- **Rationale**: Persistent, unique, widely adopted in academic publishing
- **Format**: Use the numeric identifier without the full URL (e.g., `0000-0001-5643-4068`)

### 2. Order Matters
- Authors should be listed in the order of contribution significance
- Use `corresponding: true` to flag corresponding authors rather than relying on position

### 3. CRediT Taxonomy (Optional Enhancement)
Consider supporting the [CRediT (Contributor Roles Taxonomy)](https://credit.niso.org/) for more granular attribution:
```yaml
authors:
  - name: Nathan Sheffield
    roles:
      - Conceptualization
      - Methodology
      - Software
      - Writing - original draft
```

### 4. Backward Compatibility
- Make the `authors` field **optional** to maintain backward compatibility
- Existing PEPs without author metadata remain valid
- Tools reading PEPs should gracefully handle missing author fields

### 5. Validation Schema
Extend the PEP validation schema to include:
```yaml
authors:
  type: array
  items:
    oneOf:
      - type: string  # Simple format
      - type: object  # Structured format
        properties:
          name:
            type: string
          affiliation:
            oneOf:
              - type: string
              - type: array
          email:
            type: string
            format: email
          orcid:
            type: string
            pattern: "^[0-9]{4}-[0-9]{4}-[0-9]{4}-[0-9]{3}[0-9X]$"
          url:
            type: string
            format: uri
          corresponding:
            type: boolean
          roles:
            type: array
            items:
              type: string
        required:
          - name
```

## Integration with PEP Ecosystem

### Documentation
Author metadata could be displayed in:
- PEPhub project pages (similar to GitHub repository contributors)
- Generated reports and documentation
- Citation formats

### Compatibility
This proposal aligns with:
- **Pandoc**: Uses same field names and structure as pandoc frontmatter
- **Scholarly Markdown**: Compatible with academic markdown workflows
- **DataCite/Dublin Core**: Maps well to metadata standards for datasets
- **JSON-LD**: Can be easily serialized for linked data applications

## Core Spec vs. Extension?

### Recommendation: Include in Core Spec

I recommend including `authors` as an **optional** field in the core PEP specification rather than as an extension, for these reasons:

1. **Universal Applicability**: Nearly all scientific datasets benefit from authorship attribution
2. **Discoverability**: Author metadata is fundamental for dataset discovery and citation
3. **Simplicity**: The simple format (list of names) is trivial to implement
4. **Standards Alignment**: Following pandoc conventions makes it intuitive for users already familiar with markdown/YAML

However, the field should remain **optional** to:
- Maintain backward compatibility
- Keep the barrier to entry low
- Allow PEPs to be used in contexts where authorship is not relevant

## Example: Complete PEP with Authors

```yaml
pep_version: 2.1.0
sample_table: "annotation.csv"

# Project metadata
name: "Example RNA-seq Project"
description: "RNA-seq analysis of frog samples under different conditions"

# Author metadata
authors:
  - name: Nathan Sheffield
    affiliation: University of Virginia
    email: nathan@example.org
    orcid: 0000-0001-5643-4068
    corresponding: true
  - name: Michal Stolarczyk
    affiliation: University of Virginia
    orcid: 0000-0002-5857-9560

# Sample modifiers
sample_modifiers:
  derive:
    attributes: [read1, read2]
    sources:
      data: "/path/to/{sample_name}.fastq.gz"
```

## Implementation Considerations

1. **peppy**: Update to parse and expose author metadata via the Project object
2. **PEPhub**: Display author information on project pages, enable author-based search
3. **eido**: Extend validation schema to support author metadata validation
4. **Documentation**: Add examples and best practices to the PEP specification docs

## References

- [Pandoc Manual - Metadata Blocks](https://pandoc.org/MANUAL.html#metadata-blocks)
- [CRediT Taxonomy](https://credit.niso.org/)
- [ORCID](https://orcid.org/)
- [DataCite Metadata Schema](https://schema.datacite.org/)
- [Sciquill Project](https://github.com/databio/sciquill) (referenced in the original issue)

---

This proposal provides a pragmatic path forward that:
- ✅ Supports both simple and complex use cases
- ✅ Aligns with established standards (pandoc)
- ✅ Maintains backward compatibility
- ✅ Enables rich attribution and discovery
- ✅ Integrates naturally with the PEP ecosystem

I'm happy to help refine this further or contribute to implementation!
