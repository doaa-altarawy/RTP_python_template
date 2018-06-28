[![Build Status](https://travis-ci.org/MolSSI/python_template.svg?branch=master)](https://travis-ci.org/MolSSI/python_template)[![codecov](https://codecov.io/gh/MolSSI/python_template/branch/master/graph/badge.svg)](https://codecov.io/gh/MolSSI/python_template)[![License](https://img.shields.io/badge/License-BSD%203--Clause-blue.svg)](https://opensource.org/licenses/BSD-3-Clause)

# python_template
This repository will provide a starting template for new Python-based projects.
Here we pick a set of tools that we are familiar with; however, there are many
tools extant that have similar functionality. 

The following tools will be used:
 - [GitHub](github.com) - Version Control
 - [Travis CI](https://travis-ci.org) - Continous Integration
 - [pytest](https://docs.pytest.org/en/latest/) - Unit and Regression Testing
 - [CodeCov](https://codecov.io) - Testing Coverage Analysis
 - [Read the Docs](https://readthedocs.org) - Documentation

## Testing

To run the test suite please first run `pip install -e .[tests]` in the base
repository folder. This will register this repository with your local Python so
that `import python_template` will work in any directory. Tests can then be run
with `pytest -v` (or `py.test -v` in pytest versions <3.0). 



