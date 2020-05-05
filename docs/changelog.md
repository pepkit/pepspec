# Changelog

This project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html) and [Keep a Changelog](https://keepachangelog.com/en/1.0.0/) format. 

## [2.0.0] - Unreleased

### Added
- Imports section allows linking to external PEP config files.
- It is now possible to specify more than one amendment (which replaced subprojects).

### Changed
- The structure changed (no more *metadata* section, new sections for sample and project modifiers, config, etc).
- Added a sample_modifiers section to house 5 modifiers: remove, append, duplicate, imply, and derive
- Added a project_modifiers section to house *amend* and *import*
- The structure for 'imply' now uses an if-then format instead of the previous format that was not readily interpretable
- Subprojects are renamed amendments
- Tool-specific sections for looper have been removed.


## [1.0.0] - Legacy version

The original PEP specification was used from 2014 through 2020 with some minor, backwards-compatible updates. It was not versioned.