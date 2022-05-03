# Changelog

This project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html) and [Keep a Changelog](https://keepachangelog.com/en/1.0.0/) format. 


## [[2.1.0](http://pep.databio.org/en/2.1.0/specification/)] - 2022-05-03

Version 2.1.0 relaxes a few constraints and adds a few new features. It is backwards-compatible with 2.1.0 so updated parsers should continue to work with old sample tables. No existing features were changed, only a few new options were added.

### Added
- **CSV-only PEPs**: A `YAML` project configuration file is **no longer required**. A PEP may now be specified with only a CSV sample table file.
- **Multi-row samples**. Originally, PEP required each row to correspond to a single sample, and attributes with multiple values for a sample were specified using subsample tables. Furthermore, samples tables required  `sample_name` as the index column. In PEP `2.1.0`, multi-value attributes may now be accomplished without subsample tables by specifying multiple rows with the same identifier. These rows will be automatically merged, and unique attribute values will be retained. 
- Sample index and subsample index columns may now be specified using new project attributes: `sample_table_index` and `subsample_table_index`.

## [[2.0.0](http://pep.databio.org/en/2.0.0/specification/)] - 2020-05-26

### Added
- Imports section allows linking to external PEP config files.
- It is now possible to specify more than one amendment (which replaced subprojects).
- Support for multiple subsample tables

### Changed
- The structure changed (no more *metadata* section, new sections for sample and project modifiers, config, etc).
- Added a sample_modifiers section to house 5 modifiers: remove, append, duplicate, imply, and derive
- Added a project_modifiers section to house *amend* and *import*
- The structure for 'imply' now uses an if-then format instead of the previous format that was not readily interpretable
- Subprojects are renamed amendments
- Tool-specific sections for looper have been removed.


## [1.0.0] - Legacy version

The original PEP specification was used from 2014 through 2020 with some minor, backwards-compatible updates. It was not versioned.