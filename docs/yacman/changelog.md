# Changelog

This project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html) and [Keep a Changelog](https://keepachangelog.com/en/1.0.0/) format.

## [1.0.0] -- Unreleased

### Changed
- Renamed `FutureYAMLConfigManager` to `YAMLConfigManager` (the "future" is now!)
- `FutureYAMLConfigManager` is still available as a deprecated alias with a warning (will be removed in v1.1.0)

### Fixed
- Simplified dependencies
- Removed deprecated code (`IK` constant, `_warn_deprecated` function)
- Removed deprecated properties (`alias_dict`, `_raw_alias_dict`)

### Removed
- jsonschema validation
- attmap support

## [0.9.4] -- 2025-11-03

### Added
- Python 3.13 support

### Fixed
- Missing import for `urlopen` from `urllib.request`
- Missing import for `Mapping` from `collections.abc`

### Removed
- Deprecated Python < 3.7 compatibility code

## [0.9.3] -- 2024-02-01

### Added
- New `FutureYAMLConfigManager` object, prep for v1.
- Improved file locking system with `read_lock` and `write_lock` context managers
- New `from_x` object construction API.


## [0.9.2] -- 2023-10-05

## Added
- new functionality for handling names of config files

## Fixed
- bugs with selecting a config file
- bug with exiting Python on system interrupt

## [0.9.1] -- 2023-06-15

## Added
- `.priority_get()` function on `YAMLConfigManager` object

## [0.9.0] -- 2022-05-04

This is a transition release that is compatible with the 0.X series, and also provides new capability from 1.0, which will not be backwards-compatible

## Added
- new `YAMLConfigManager` object, to replace YacAttMap, which will be the new interface in 1.0. 

## [0.8.4] -- 2021-12-02
## Fixed
- a bug that prevented writing a readonly file to an external path

## [0.8.3] -- 2021-09-20
## Fixed
- removed use2to3 for compatibility with setuptools upgrade.

## [0.8.2] -- 2021-06-28
## Fixed
- if file is empty, initialize its contents to an empty dict, which prevents failure
- check for previously applied path to `yaml.SafeLoader` before patching

## [0.8.1] -- 2021-03-18
## Fixed
- Clarified message for `__internal` key.


## [0.8.0] -- 2021-03-10
### Added
- jsonschema validation support. The `YacAttMap` contents can be validated when object is constructed and on every call to the `write` method
- `__internal` key in `YacAttMap` object, which stores a `attamp.AttMap` of meta attributes. `__internal` can be accessed in clients as: `yacman.IK`

## Deprecated
- use of the following properties, which should be accessed via `__internal` key from now on:
  - `YacAttMap.file_path`
  - `YacAttMap.writable`

## [0.7.1] -- 2021-02-22
### Added
- environment variables expansion in provided paths in `select_config` function
### Fixed
- issues with locking nonexistant files; [#41](https://github.com/databio/yacman/issues/41)

## [0.7.0] -- 2020-08-28
### Added
- `AliasedYacAttMap` class that supports top-level key aliases

## [0.6.9] -- 2020-07-01
### Changed
- improved file locking
### Removed
- possibility to provide a file path as `entries` in the `YacAttMap` constructor

## [0.6.8] -- 2020-06-25
### Changed
- extended lock wait time and the frequency of checks
- drop Python 2 support
### Fixed
- a problem with file locking after other process unlocked it before the timeout


## [0.6.7] -- 2020-02-07
### Changed
- load_yaml function can accommodate URLs.


## [0.6.6] -- 2019-12-13
### Added
- possibility to use `YacAttMap` in a context manager even if it was _not_ read from a file, but a file path attribute has been set


## [0.6.5] -- 2019-12-02

### Added
- context manager functionality to `YacAttMap` class

### Changed
- method name: `unlock` to `make_readonly`
- `make_writable` behavior: it re-reads the source file now

## [0.6.4] -- 2019-11-04

### Added
- distribute license file with the package

## [0.6.3] -- 2019-10-22

### Fixed
- silent lock creation failures in case the lock directory does not exist; [#24](https://github.com/databio/yacman/issues/24)

### Added
- `YacAttMap` properties: `file_path` and `writable`

## [0.6.2] -- 2019-10-10

### Changed

- in `select_config` always use default config file path when no valid path is determined

## [0.6.1] -- 2019-10-08

### Added
- `strict_env` argument to the `select_config` function

### Changed
- in `select_config` use the `default_config_filepath` even if no `config_env_vars` were specified

## [0.6.0] -- 2019-10-02

### Added
- add support for multi-user context operation
- `writable` argument to create the object in a read-only or writable mode
- `wait_max` argument to specify the wait time for the lock before raising a `RuntimeError`
- `unlock` method
- `make_writable` method

### Changed
- entries argument accepting a file path becomes deprecated and throws a `DeprecationWarning` and will be removed altogether in the future release

## [0.5.2] -- 2019-08-20

### Changed
- Force all indexes to be strings (not floats or ints).

## [0.5.1] -- 2019-08-02

### Added
- Allow providing a yaml string to constructor.

## [0.5.0] -- 2019-06-18

### Added
- Improve constructor to allow either a dict or a filepath
- Make printing prettier

## [0.4.2] -- 2019-06-18

### Changed
- Parameterize existence check for `select_config`.

## [0.4.1] -- 2019-06-14

### Changed
- Parameterize behavior when `select_config` filepath argument does not exist.

## [0.4.0] -- 2019-06-07

### Fixed
- Fix bug when building a `YacAttMap` with a filepath in Python 2.7: [Issue 6](https://github.com/databio/yacman/issues/6)

### CHanged
- Defer exception handling from `load_yaml` to client code.

## [0.3.0] -- 2019-06-04

### Added
- Allow a YacAttMap to remember its own path so it can use `write` without an argument.

## [0.2.0] -- 2019-05-21

### Changed
- Changed `select_load` to just `select` so you load on your own.

### Fixed
- Fixed packaging bug

## [0.1.0] -- 2019-05-15
- First functional public release of `yacman`.
