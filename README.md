# LogColor
<a href="http://log-color.readthedocs.io/en/latest/"><img src="https://img.shields.io/badge/docs-latest-brightgreen.svg?style=flat"></a>
<a href="https://pypi.python.org/pypi/log-color"><img src="https://img.shields.io/pypi/v/log_color.svg"></a>
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
