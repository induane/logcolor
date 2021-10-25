Description
===========

``log_color`` provides Logging formatters for colorized outputs. A very simple domain specific language (DSL) is used
to colorize all or part of  a particular log message. For example::

    LOG.debug('Found file at #g<%s>', path)

The above would colorize the contents of the 'path' variable green when output to a command line terminal.\n

A formatter which strips color sequences from the output is also included for situations like logging to files where
having ANSI color sequences embedded in the output would not make sense.
