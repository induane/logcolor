Usage
=====
Usage is very simple. Simply import the ``ColorFormatter`` and use it like any
other log formatter.

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


Handy DictConfig (that also uses the ColorStripper formatter for a file
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
                "datefmt": "%Y-%m-%d %H:%M:%S",
            },
            "FileFormatter": {
                '()': ColorStripper,
                "format": ("%(levelname)-8s: %(asctime)s '%(message)s' "
                           "%(name)s:%(lineno)s"),
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
