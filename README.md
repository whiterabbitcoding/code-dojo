![Coverage](coverage.svg)
[![made-with-python](https://img.shields.io/badge/Made%20with-Python-1f425f.svg)](https://www.python.org/)
![Black](https://img.shields.io/badge/code%20style-black-black)

# Code-Dojo

A collection of scripts from online practice questions and formal tests for
interview preparation and learning.

## Environment setup

To setup a local environment, run the following command:

```
make all
```

This will create a virutal environment, install pre-commit requirements and
requirements.txt

### Formatting & Linting

```
# Check for linting issues:
make format-check

# Fix the issues:
make format
```

### Testing

Check test coverage:

```
make coverage
```

Run tests:

```
make test
```

### Pre-commit ooks

This service uses pre-commit hooks to apply `black`, `flake8`, and `isort`
formatting.

If you want the code style checks to be run automatically before you commit any
code, install included Git hooks with this command:

```
# Installing:
pre-commit install

# Uninstalling:
pre-commit uninstall
```
