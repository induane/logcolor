Usage
=====
.. _color_language:

Color Language
--------------
In order to colorize a word or words, the ``ColorFormatter`` implements a *DSL* or **D**\ omain **S**\ pecific **L**\ anguage.

Colorizing a string of text automatically can be done by using the following as a schemata: ``#x<text>`` where ``x`` is
the lowercase first letter of the color you want the text to appear in the terminal and ``text`` is the string of
characters to be colored. For example, to color a string blue::

    "#b<I am blue text>"

This can be done on a substring leaving the rest of the words untouched. In the following example only the word
``green`` would be colored, the rest of the text would appear in the terminals default color::

    "This text has some #g<green> words. Okay, just one actually."

.. tip:: Automatic coloring of text occurs only within the context of a log message. No other string values are handled.

Here is a more complete example of a log message with colored text; in this
example, the *path* substring would be colored green::

    LOG.debug("Processing asset #g<%s>", path)

The same example but with Python3-only f-strings::

    LOG.debug(f"Processing asset #g<{path}>")

In the above examples the value of the variable *path* would be printed as green text to the console.

**Logging Tip**\ :

Do not use f-strings in log messages. The format-pointer style with arguments passed directly to the log handler is the
preferred method for logging because it will avoid formatting the strings if the log message will not be omitted.

Bad:

``LOG.debug("Foo %s" % bar)``

``LOG.debug("Foo {}".format(bar))``

``LOG.debug(f"Foo {bar}")

Good:

``LOG.debug("Foo %s", bar)``

.. tip:: The difference between the *incorrect* ``LOG.debug("Foo %s" % bar)`` and the correct ``LOG.debug("Foo %s", bar)``
    is that the good one doesn't use the ``%`` operator, but instead passes the format variables to the log handler
    as arguments.

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
If you're using the ``#b<blue>`` notation, you probably realize that this means that if you log to a file, you'll end
up with text that looks more like ``\033[94mblue\033[0m`` since it contains the color escape codes. Or, alternatively,
if you use a different formatter, you'll have the literal ``#b<blue>`` string in the text. Neither of these are ideal.
To that end, another formatter is provided called: ``ColorStripper``. The purpose of this is to remove any escape codes
and/or :ref:`color_language` references from the text passing through the formatter.

This allows you to easily write plain text to files or other log handlers, while still using colored output for a
console logger.

Configuration
-------------
Configuration is very simple. Simply import the ``ColorFormatter`` and use it like you would any other log formatter.

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


Troubleshooting
---------------

Output Not Colorized
^^^^^^^^^^^^^^^^^^^^

There are a couple of things to check for:

1. If you're running on Windows, colorized output is *not* supported.
2. If you're in a *nix terminal and ANSI color codes are supported but you're not
   seeing colorized output, check for the ``NO_COLOR`` environment variable. See
   `no-color.org <http://no-color.org/>`_ for more information on this standard. If the ``NO_COLOR`` environment
   variable is set, colorized output is automatically suppressed.
3. Something else: It could be the case that the detection scheme that ``log_color`` ships is failing to detect that
   your particular terminal supports ANSI color codes. Detection of color support could be offloaded to a third party
   library, but one of the goals of ``log_color`` is to have no dependencies. Color support detection isn't
   standardized and most libraries that do color support detection employ reaching out to ncurses or including a huge
   array of information about very specific (and often obscure) terminals. I'm willing to include support for specific
   terminals if someone wishes to add them, but I'm not going to default to doing all of that work if no one is using
   them anyway. Color detection support can be found in ``src/log_color/colors.py`` in the ColorStr class. The
   ``color_supported`` method handles detection so feel free to add it there.
