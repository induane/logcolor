# LogColor
<a href="http://log-color.readthedocs.io/en/latest/"><img src="https://img.shields.io/badge/docs-latest-brightgreen.svg?style=flat"></a>
<a href="https://pypi.python.org/pypi/log-color"><img src="https://img.shields.io/pypi/v/log_color.svg"></a>

When making command line interfaces, it's often useful to colorize the output
to emphasize salient pieces of information or otherwise enhance the user
experience. Unfortunately it's quite cumbersome to add colorized outputs to
Python log messages.

## ColorFormatter

The ColorFormatter is a logging formatter that parses your log messages and
adds color codes to the log messages.

![example](https://raw.githubusercontent.com/induane/logcolor/master/docs/source/images/example_logs.png)

## ColorStripper

The ColorStripper formatter is the inverse of the ColorFormatter. It strips the
color information from your messages so that you can safely log to a file.

## Installation
I'm on pypi!

```
$ pip install log_color
```

## Features

- Simple to use
- No external dependencies
- Compatibility with Python 2.7, Python 3.3+, PyPy

NOTE: Python ``3.0``, ``3.1``, and ``3.2`` are not supported due to lack of
support for  ``u""`` style format strings.

## Makefile

This project uses a Makefile for various tasks. Some of the available tasks
are listed below.

* `make clean` - Clean build artifacts out of your project
* `make test` - Run Unit Tests (using nose & tox)
* `make sdist` - Build a Python source distribution
* `make wheel` - Build a Python wheel
* `make docs` - Build the Sphinx documentation
* `make publish` - publish any artifacts in dist/* using twine
* `make format-code` - Format source code using ``black``
* `make` - Equivalent to `make test format-code docs sdist rpm`

## http://no-color.org/
LogColor honors the ``NO_COLOR`` environment variable.
