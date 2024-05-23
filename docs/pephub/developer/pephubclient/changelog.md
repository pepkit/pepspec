# Changelog

This project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html) and [Keep a Changelog](https://keepachangelog.com/en/1.0.0/) format.

## [0.4.2] - 2024-04-16
### Updated
- View creation, by adding description and no_fail flag


## [0.4.1] - 2024-03-07
### Fixed
- Expired token error handling  ([#17](https://github.com/pepkit/pephubclient/issues/17))

## [0.4.0] - 2024-02-12
### Added
- a parameter that points to where peps should be saved ([#32](https://github.com/pepkit/pephubclient/issues/32))
- pep zipping option to `save_pep` function ([#34](https://github.com/pepkit/pephubclient/issues/34))
- API for samples ([#29](https://github.com/pepkit/pephubclient/issues/29))
- API for projects ([#28](https://github.com/pepkit/pephubclient/issues/28))

### Updated
- Transferred `save_pep` function to helpers

## [0.3.0] - 2024-01-17
### Added
- customization of the base PEPhub URL ([#22](https://github.com/pepkit/pephubclient/issues/22))

### Updated
- Updated PEPhub API URL
- Increased the required pydantic version to >2.5.0

## [0.2.2] - 2024-01-17
### Added
- customization of the base pephub URL. [#22](https://github.com/pepkit/pephubclient/issues/22)

### Updated 
- PEPhub API URL
- Increased the required pydantic version to >2.5.0

## [0.2.1] - 2023-11-01
### Added
- is_registry_path checker function

## [0.2.0] - 2023-10-02
### Added
- Project search functionality

## [0.1.1] - 2023-07-29
### Fixed
- Incorrect base url

## [0.1.1] - 2023-07-29
### Fixed
- New raw PEP structure was broken. ([#20](https://github.com/pepkit/pephubclient/issues/20))

## [0.1.0] - 2023-04-16
### Added
- First release
