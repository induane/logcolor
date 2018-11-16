Usage
=====
.. _color_language:

Color Language
--------------
In order to colorize a word or words, the ``ColorFormatter`` implements a
sort of *DSL* or **D**\ omain **S**\ pecific **L**\ anguage.

Colorizing a string of text automatically can be done by using the following as
a schemata: ``#x<text>`` where ``x`` is the lowercase first letter of the color
you want the text to appear in the terminal and ``text`` is the string of
characters to be colored. For example, to color a string blue::

    "#b<I am blue text>"

This can be done on a substring leaving the rest of the words untouched. In the
following example only the word ``green`` would be colored, the rest of the
text would appear in the terminals default color::

    "This text has some #g<green> words. Okay, just one actually."

.. tip:: Automatic coloring of text occurs only within the context of a log
    message. No other string values are handled.

Here is a more complete example of a log message with colored text; in this
example, the *path* substring would be colored green::

    LOG.debug("Processing asset #g<{0}>".format(path))

In the above example the *path* would be printed as green text to the console.

Supported Colors
^^^^^^^^^^^^^^^^
Only a few colors are supported by the ``ColoredFormatter``, but they should be
sufficient for most purposes.

- ``b``\ —``#b<blue>``
- ``c``\ —``#b<cyan>``
- ``g``\ —``#b<green>``
- ``m``\ —``#b<maroon>``
- ``r``\ —``#b<red>``
- ``w``\ —``#b<white>``
- ``y``\ —``#b<yellow>``
- ``db``\ —``#b<dark-blue>``
- ``dc``\ —``#b<dark-cyan>``
- ``dg``\ —``#b<dark-green>``
- ``dm``\ —``#b<dark-maroon>``
- ``dr``\ —``#b<dark-red>``
- ``dy``\ —``#b<dark-yellow>``


Color Stripping
^^^^^^^^^^^^^^^
If you're using the ``#b<blue>`` notation, you probably realize that this means
that if you log to a file, you'll end up with text that looks more like
``\033[94mblue\033[0m`` since it contains the color escape codes. Or,
alternatively, if you use a different formatter, you'll have the literal
``#b<blue>`` string in the text. Neither of these are ideal. To that end,
another formatter is provided called: ``ColorStripper``. The purpose of this is
to remove any escape codes and/or :ref:`color_language` references from the
text passing through the formatter.

This allows you to easily write plain text to files or other log handlers,
while still using colored output for a console logger.

Configuration
-------------
Configuration is very simple. Simply import the ``ColorFormatter`` and use it
like you would any other log formatter.

Simple Example::

    import logging
    from log_color import ColorFormatter

    handler = logging.StreamHandler()
    formatter = ColorFormatter("%(levelname)s: %(message)s")
    handler.setFormatter(formatter)

    log = logging.getLogger('color_log')
    log.setLevel(logging.INFO)
    log.addHandler(handler)
    log.info('Look, #b<blue> text!')


Here is a  DictConfig (that also uses the ColorStripper formatter for a file
handler)::

    from logging.config import dictConfig
    from log_color import ColorFormatter, ColorStripper

    BASE_CONFIG = {
        'version': 1,
        'disable_existing_loggers': False,
        'formatters': {
            "ConsoleFormatter": {
                '()': ColorFormatter,
                "format": "%(levelname)s: %(message)s",
            },
            "FileFormatter": {
                '()': ColorStripper,
                "format": ("%(levelname)-8s: %(asctime)s '%(message)s' "
                           "%(name)s:%(lineno)s"),
                "datefmt": "%Y-%m-%d %H:%M:%S",
            },
        },
        'handlers': {
            "console": {
                "level": "DEBUG",
                "class": "logging.StreamHandler",
                "formatter": "ConsoleFormatter",
            },
            "filehandler": {
                'level': "DEBUG",
                'class': 'logging.handlers.RotatingFileHandler',
                'filename': "/tmp/logfile",
                'formatter': 'FileFormatter',
            },
        },
        'loggers': {
            'my_script': {
                'handlers': ["console", "filehandler"],
                'level': 'INFO',
            },
        }
    }
    dictConfig(BASE_CONFIG)
