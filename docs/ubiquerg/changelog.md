# Changelog

This project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html) and [Keep a Changelog](https://keepachangelog.com/en/1.0.0/) format. 

## [0.8.2] -- 2025-12-01

### Changed
- Removed veracitools as test dependency, and all other test dependencies.

## [0.8.1] - 2025-03-05

### Added
- Ported deep_update from yacman

## [0.8.0] - 2024-04-02
### Changed
- Expanded `mkabs` function to handle more cases
- Allow `is_url` to work on Path objects
- Remove `mock` test requirement in favor of importing `unittest.mock as mock`

## [0.7.0] - 2024-01-02

### Added
- Experimental support for three-locking.


## [0.6.3] - 2023-08-08
### Fixed 
- Incorrect read of registry path.  [Issue 35](https://github.com/pepkit/ubiquerg/issues/35)

## [0.6.2] - 2021-01-28

### Fixed 
- `is_url` function; [Issue 32](https://github.com/pepkit/ubiquerg/issues/32)

## [0.6.1] - 2020-07-01

### Changed
- file locking enhancements

## [0.6.0] - 2020-06-23

### Added
- file locking utilities:
    - `create_lock`
    - `remove_lock`
    - `make_lock_path`
    - `create_file_racefree`
    - `wait_for_lock`
    
## [0.5.2] - 2020-05-15
### Changed
- in `size` function, if a file is not found a warning is issued, instead of a message

### Added
- `VersionInHelpParser` methods characterizing the instance: 
    - `arg_defaults`
    - `dests_by_subparser`
    - `subcommands`
    - `top_level_args`
    - `subparsers`

## [0.5.1] - 2020-03-30
### Added
- `uniqify` function
- support for collection of paths in `size` function

### Fixed
- path expansion issues; [Issue #24](https://github.com/pepkit/ubiquerg/issues/24)

### Changed
  
## [0.5.0] - 2019-10-17
### Added
- add `asciify_dict` function

## [0.4.9] - 2019-09-17
### Added
- add `--version` argument in `VersionInHelpParser`
- add `untar` function
- add `mkabs` function

## [0.4.8] - 2019-08-27
### Added
- `parse_registry_path` function.

## [0.4.7] - 2019-08-09
### Fixed
- `is_writable` function; [Issue 16](https://github.com/pepkit/ubiquerg/issues/16)

## [0.4.6] - 2019-08-08
### Added
- file/directory size checker
- `is_writable` function

## [0.4.5] - 2019-07-01
### Changed
- If argument to callability checker is a file, require executability; if it's a folder, it's not callable.
### Fixed
- Populate intended field in error message for bad argument to callability checker.

## [0.4.4] - 2019-06-20
### Added
- Command callability checker

## [0.4.3] - 2019-06-06
### Changed
- To avoid implicitly wrapping `input()` in `eval`, never use `2to3`.

## [0.4.2] - 2019-06-06
### Fixed
- More robust handling of terminal interaction in `query_yes_no`

## [0.4] - 2019-05-31
### Added
- `checksum`, using md5
- `query_yes_no` to facilitate binary user terminal interaction

## [0.3] - 2019-05-29
### Added
- `TmpEnv`: environment variable context manager

## [0.2.1] - 2019-05-16
### Changed
- Use `is_url` to determine slash behavior in `expandpath`

## [0.2] - 2019-05-16
### Added
- `is_url`

## [0.1] - 2019-05-08
### Changed
- Remove `ExpectContext`; see [`veracitools`](https://github.com/pepkit/veracitools)

## [0.0.5.1] - 2019-05-08
### Fixed
- Control exports to fix a docs build issue; see [Issue 2](https://github.com/pepkit/ubiquerg/issues/2)

## [0.0.5] - 2019-05-08
### Added
- `expandpath` utility for dealing with user and environment variables in paths

## [0.0.4] - 2019-05-03
### Added
- `ExpectContext` for uniform test execution, regardless of whether expectation is an ordinary object or an exception
### Changed
- When minimum item count exceeds pool size and/or the "pool" of items is empty, `powerset` returns an empty collection rather than a collection with a single empty element.

## [0.0.3] - 2019-05-02
### Added
- CLI optarg string builder (`build_cli_extra`)
- `powerset` (all subsets of a collection)

## [0.0.2] - 2019-05-01
## Changed
- Restrict offerings to most generic functionality.

## [0.0.1] - 2019-04-30
- First release version
