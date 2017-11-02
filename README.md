# ColorFormatter

<a href="http://log-color.readthedocs.io/en/latest/"><img src="https://img.shields.io/badge/docs-latest-brightgreen.svg?style=flat"></a>
<a href="https://pypi.python.org/pypi/log-color"><img src="https://img.shields.io/pypi/v/log_color.svg"></a>

When making command line interfaces, it's often useful to colorize the output
to emphasize certain salient pieces of information or to otherwise enhance the
user experience. Unfortunately it's quite cumbersome to add colorized outputs
to Python log messages.

![example](https://raw.githubusercontent.com/induane/logcolor/master/docs/source/images/example_logs.png)

## Installation
I'm on pypi!

```
$ pip install log_color
```

## Features

- Simple to use
- No external dependencies
- Compatibility with Python2.6, Python 2.7, Python 3.x, PyPy

## Makefile

This project uses a Makefile for various tasks. Some of the available tasks
are listed below.

* `make clean` - Clean build artifacts out of your project
* `make test` - Run Unit Tests (using nose & tox)
* `make sdist` - Build a Python source distribution
* `make wheel` - Build a Python wheel
* `make docs` - Build the Sphinx documentation
* `make publish` - publish any artifacts in dist/* using twine
* `make pep8` - Get a pep8 compliance report about your code
* `make` - Equivalent to `make test pep8 docs sdist rpm`
