# ubiquerg

![Run pytests](https://github.com/pepkit/ubiquerg/workflows/Run%20pytests/badge.svg)
[![codecov](https://codecov.io/gh/pepkit/ubiquerg/branch/master/graph/badge.svg)](https://codecov.io/gh/pepkit/ubiquerg)
[![PEP compatible](https://pepkit.github.io/img/PEP-compatible-green.svg)](https://pepkit.github.io)

Ubiquerg is a utility package with a collection of helpful universally useful functions. The name means work (erg) everywhere (ubique), indicating our intention for these to be low-level functions that can be used in lots of different places. Functions are divided into groups, including:

- collection
- environment
- files
- paths
- system
- web
- cli_tools

## Development guidelines

- Ubiquerg should have no dependencies outside of standard built-in python modules. Please do not add any functions that introduce a new dependency.
- Functions should be generic. They should perform basic, low-level processing that is not specific to a particular application.
- Functions should only be added to ubiquerg if they are used in at least 2 existing modules.
- Functions should be kept relatively small and simple (ideally <50 lines of code).
