# Changelog

This project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html) and [Keep a Changelog](https://keepachangelog.com/en/1.0.0/) format.

## [0.7.0] - 2024-XX-XX
### Added
- `__iter__` now takes limit and cursor arguments to create an iterator from `select_records`
### Changed
- updated pydantic requirement to be >= 2.5.3 

## [0.6.0] - 2023-12-22
### Added
- `select_records`, which allows for a single API for selecting attributes (result_identifiers) given filter_conditions and/or columns
- `retrieve_one`, and `retrieve_many` which allows for selecting one or multiple records given record_identifier
- pipestat reader submodule to read DB results via FastAPI endpoints: `pipestat serve --config "config.yaml"`
- ability to create `SamplePipestatManager` and `ProjectSamplePipestatManager` which are sample/project specific PipestatManager objects.
- PipestatBoss wrapper class which holds `SamplePipestatManager` and `ProjectSamplePipestatManager` classes.
- `to_dict` methods to parsed schema object.
- `select_distinct` function which retrieves unique results for a list of attributes.
- `pipestat link` which creates a directory of symlinks for reported results.
- `list_recent_results` which allows for retrieving records filtered via a start and end time.
- reporting and retrieving results via item access,e.g. `psm["sample1", "name_of_something"] = "name_of_something_string"` or `result = psm["sample1"]`
- pipestat now supports one results file per sample by using `{record_identifier}` in the results_file_path.

### Fixed
- path expansion when creating database url.
- added jinja2 requirement.
- `pipeline_name` column not populating in postgres db backend.
- pipestat will now create subdirectories during results_file creation.
- fixed bugs and polished both report generation and stats table generation per https://github.com/pepkit/pipestat/pull/131 

### Changed
- Removed `retrieve`, `get_one_record`, `get_records function`.
- Removed `get_orm` and replace with `get_model`.
- Removed `get_table_name` function.
- Refactor:
  - `sample_name` -> `record_identifier`.
  - `pipeline_type` has been removed from most functions.
- added optional dependencies for the database backend and pipestat reader, e.g. `pip install pipestat[dbbackend]`.

## [0.5.2] - 2023-11-30
### Fixed

- add jinja2 to requirements doc.

## [0.5.1] - 2023-08-14
### Fixed

- fix schema_path issue when building html reports and obtaining schema from config file.

## [0.5.0] - 2023-08-08
### Added

- Add summarize function to generate static html results report.

## [0.4.1] - 2023-07-26

### Fix

- ensure Pipestat uses proper versions of Pydantic, Yacman.

## [0.4.0] - 2023-06-29

### Changed

- Remove attmap dependency
- Migrate to SQLModel for Object–relational mapping (ORM)
- Renamed `list_existing_results` to `list_results` and allow for returning a subset of results.
- Refactor: 
  - `namespace` -> `project_name`, 
  - `pipeline_id` -> `pipeline_name`, 
  - `record_identifier` -> `sample_name`

### Added

- Add 'init -g' for creating generic configuration file.
- Add ability to pass function to format reported results.

## [0.3.1] - 2022-08-18

### Fix

- database connection error

## [0.3.0] - 2021-10-30

### Added

- `select_distinct` for select distinct values from given table and column(s)

## [0.2.0] - 2021-10-25

### Added

- optional parameter for specify returning columns with `select_txt`
 
## [0.1.0] - 2021-06-24

**This update introduces some backwards-incompatible changes due to database interface redesign**

### Changed

- database interface type from a driver to an Object–relational mapping (ORM) approach

### Added

- results highlighting support
- database column parametrizing from the results schema
- static typing
- possibility to initialize the `PipestatManager` object (or use the `pipestat status` CLI) with no results schema defined for pipeline status management even when backed by a database; [Issue #1](https://github.com/pepkit/pipestat/issues/1)

## [0.0.4] - 2021-04-02

### Added

- config validation
- typing in code

## [0.0.3] - 2021-03-12

### Added

- possibility to initialize the `PipestatManager` object (or use the `pipestat status` CLI) with no results schema defined for pipeline status management; [Issue #1](https://github.com/pepkit/pipestat/issues/1)

## [0.0.2] - 2021-02-22

### Added

- initial package release
