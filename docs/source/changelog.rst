Changelog
=========

1.0.7
-----
- Added automatic code formatting with ``black``
- Dropped support for Python 2.6
- Use vanilla python -m unittest instead of third party testrunner ``nosetests``
  because it is no longer maintained and it's simpler to not have a third
  party test runner in use
- Simplified code formatting logic
- Some minor documentation updates
- WARNING: This is the last release that will support Python 2.x
- Updated ``setup.py`` metadata to indicate which versions of Python are
  supported by ``log_color``

1.0.6
-----
- Added support for darker colors

1.0.5
-----
- Honor the NO_COLOR environment variable

1.0.4
-----
- Fixed a bug with logging non text objects

1.0.3
-----
- Improved cross platform testing with tox
- Added base test assertions for use in multiple
  versions of Python

1.0.2
-----
- Updated README.md with a nice picture
- Added publish option to Makefile
- Fixed an import and coverage package name

1.0.1
-----
- Added licence information

1.0.0
-----
- Base loggers implemented
