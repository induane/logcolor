# LogColor
[![Stable Version](https://img.shields.io/pypi/v/log-color?color=blue)](https://pypi.org/project/log-color/)
[![Documentation Status](https://readthedocs.org/projects/log-color/badge/?version=latest)](https://log-color.readthedocs.io/en/latest/?badge=latest)
[![Downloads](https://img.shields.io/pypi/dm/log-color)](https://pypistats.org/packages/log-color)
![Test](https://github.com/induane/logcolor/actions/workflows/test.yml/badge.svg) ![Lint](https://github.com/induane/logcolor/actions/workflows/lint.yml/badge.svg)
[![Imports: isort](https://img.shields.io/badge/%20imports-isort-%231674b1?style=flat&labelColor=ef8336)](https://pycqa.github.io/isort/)
[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)

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
