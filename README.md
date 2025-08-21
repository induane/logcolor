# LogColor
[![Stable Version](https://img.shields.io/pypi/v/log-color?color=blue)](https://pypi.org/project/log-color/)
[![Documentation Status](https://readthedocs.org/projects/log-color/badge/?version=latest)](https://log-color.readthedocs.io/en/latest/?badge=latest)
[![Downloads](https://img.shields.io/pypi/dm/log-color)](https://pypistats.org/packages/log-color)
![Test](https://github.com/induane/logcolor/actions/workflows/test.yml/badge.svg) ![Lint](https://github.com/induane/logcolor/actions/workflows/lint.yml/badge.svg)


When making command line interfaces, it's often useful to colorize the output to emphasize salient pieces of
information or otherwise enhance the user experience. Unfortunately it's quite cumbersome to add colorized outputs to
Python log messages.

## ColorFormatter

The ColorFormatter is a logging formatter that parses your log messages and adds color codes to the log messages.

![example](https://raw.githubusercontent.com/induane/logcolor/master/docs/source/images/example_logs.png)

## ColorStripper

The ColorStripper formatter is the inverse of the ColorFormatter. It strips the color information from your messages so
that you can log to a file without it being full of color codes.

## Installation
I'm on pypi!

```
$ pip install log_color
```

## Features

- Simple to use
- No external dependencies
- Compatibility with Python 3.7+, PyPy
- Fast! Compiled binaries are available for some systems!

## http://no-color.org/
LogColor honors the ``NO_COLOR`` environment variable.

## Developer Setup

This project uses [uv](https://docs.astral.sh/uv/ "UV Documentation") for dependency management, command running, etc... install it:

```bash
$ curl -LsSf https://astral.sh/uv/install.sh | sh
```

### Makefile

If you're on Linux or OSX, there is a ``Makefile`` with a number of helpful targets:

* ``make check-types`` Run ``mypy`` static code analysis tools
* ``make format-code`` Runs the [ruff](https://beta.ruff.rs/docs/) code formatter
* ``make check-code`` Validates no code formatting errors or import sorting errors (check only, makes no changes)
* ``make wheel`` Build Python ``.whl`` file for distribution
* ``make test`` Run the unittests
* ``make docs`` Build the documentation
* ``make freeze`` List all packages (and their version number) installed in the virtual environment
* ``make shell`` Launch an interactive Python shell in the virtual environment context
* ``make clean`` Remove any files that aren't part of the repo (build artifacts, test reports, etc...)
* ``make git-clean`` Runs the git ``fsck`` tool, prunes the reflog, etc...

**TIP:** *If you want to force a target to be re-evaluated (i.e. ``make env``) run make with the ``-B`` flag to force
it to evaluate.*
