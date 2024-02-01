# Changelog

This project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html) and [Keep a Changelog](https://keepachangelog.com/en/1.0.0/) format.

## [0.2.2] - 2023-11-16

### Changed
- remove unused `exclude-case` from CLI. Fixes #65

## [0.2.1] - 2023-07-05

### Changed
- printing project to logger.debug

## [0.2.0] - 2023-06-21

### Added
- CLI options for modulating peppy project (#50)

### Fixed
- Rewrote history to remove large files committed by mistake
- You can now check for existing of files in subsample table (#26)

### Changed
- All validation functions now use similar error-raising behavior
- Validation functions now return all individual error objects grouped by type


## [0.1.9] - 2022-09-12

### Fixed
- CSV filter bug

### Added
- New test cases

## [0.1.8] - 2022-08-29
### Changed
- the way of merging tables for multiline output format from eido convert

### Added
- better architecture for output formatters that goes well with **open-closed principle**
- using mock in some testcases
- test data in the format that was causing the errors previously

### Fixed
- passing plugin keyword arguments to `run_filter` function
- saving output file will now work for path like `file.txt`, no need to pass full path


## [0.1.7] - 2022-08-11
### Changed
- When a validation fails, `eido` will now return all errors instead of just the first one it finds.

## [0.1.6] - 2022-05-16
### Added
- a possibility to set a custom sample table index with `-s/--st-index` option
- an option to see filters docs via CLI: `eido filters -f <filter_name>`
- PEP filters now return their conversion result for progrommatic use.
- PEP filters can write to files.
- A filter can write multiple outputs to multiple files using the `paths` keyword arg.

### Fixed
- Some error messages with incorrectly defined schemas.
- 'required' attribute is no longer required in schema

### Changed
- Moved all `eido filter` functionality into the `eido convert` command for simplicity. This way, a single top-level command namespace holds all related functionality. Filters are still EXPERIMENTAL.

## [0.1.5] - 2021-04-15
### Added
- `eido convert` converts the provided PEP to a specified format (EXPERIMENTAL! may change in future versions)
- `eido filter` lists available filters in current environment (EXPERIMENTAL! may change in future versions)
- built-in plugins (EXPERIMENTAL! may change in future versions):
  - `basic_pep_filter`
  - `yaml_pep_filter`
  - `csv_pep_filter`
  - `yaml_samples_pep_filter`

### Changed
- in `validate_inputs` function sample attributes are first validated for existence before their values' existence is checked

## [0.1.4] - 2021-03-14
### Changed
- update schema preprocessing

## [0.1.3] - 2020-10-07
### Changed
- `validate_inputs` function now returns a dictionary with validation data, i.e missing, required_inputs, all_inputs, input_file_size rather than a list of missing files
- `validate_inputs` function does not modify `Sample` objects

## [0.1.2] - 2020-08-06
### Added
- license in the package source distribution

## [0.1.1] - 2020-05-27
### Changed
- documentation updates
- CLI behavior when no subcommand provided; [#20](https://github.com/pepkit/eido/issues/20)

## [0.1.0] - 2020-05-26
### Added
- automatic support for subsamples for sample the following property types:
    - `string`
    - `boolean`
    - `numeric`
- `eido inspect` CLI command
- schema importing functionality (via top level `imports` key)
- exported functions:
    - `validate_inputs`
    - `inspect_project`
    - `read_schema`

### Changed
- previous CLI `eido` functionality moved to `eido validate`

## [0.0.6] - 2020-02-07
### Changed
- CLI can accommodate URLs.

## [0.0.5] - 2020-02-04
### Added
- [documentation website](http://eido.databio.org/en/latest/)
- include version in the CLI help

## [0.0.4] - 2020-01-31
### Added
- `validate_sample` function for sample level validation
- sample validation CLI support (via `-n`/`--sample-name` argument)
- `validate_config` to facilitate samples exclusion in validation
- config validation CLI support (via `-c`/`--just-config` argument)

## [0.0.3] - 2020-01-30
### Added
- Option to exclude the validation case from error messages in both Python API and CLI app with `exclude_case` and `-e`/`--exclude-case`, respectively.
- include requirements in the source distribution

## [0.0.2] - 2020-01-12

### Added
- Initial project release
