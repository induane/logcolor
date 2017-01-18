# ColorFormatter

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

## Goals

- Simple to use
- No external dependencies

## Documentation
Check out documentation on readthedocs: http://log-color.readthedocs.io/en/latest/

## Makefile

This project uses a Makefile for various tasks. Some of the available tasks
are listed below.

* `make clean` - Clean build artifacts out of your project
* `make test` - Run Unit Tests (using nose)
* `make sdist` - Build a Python source distribution
* `make rpm` - Build an RPM
* `make docs` - Build the Sphinx documentation
* `make pep8` - Get a pep8 compliance report about your code
* `make` - Equivalent to `make test pep8 docs sdist rpm`
