"""
Custom Formatters
=================
"""
# Standard
import logging

from logcolor import colors
from logcolor.regex import COLOR_EXP


class ColorStripper(logging.Formatter):
    """
    Strips all references to colored output from the logging message. This is
    useful for passing something through to a file logger where the color is
    not desired.
    """

    def format(self, record):
        # Strip any color sequences
        record.msg = colors.strip_color(record.msg)
        record.levelname = colors.strip_color(record.levelname)

        # Create replacements map for the message
        repl_map = {}
        for val in COLOR_EXP.findall(record.msg):
            repl_map[val] = val[3:-1]
        for k, v in repl_map.iteritems():
            record.msg = record.msg.replace(k, v)
        return logging.Formatter.format(self, record)


class ColoredFormatter(logging.Formatter):
    """
    Adds in color sequences for logging messages. They are to be provided in
    the format: %y{colored part}  which will be formatted as yellow. The colors
    allowed are:

    - m (magenta)
    - b (blue)
    - c (cyan)
    - g (green)
    - y (yellow)
    - r (red)
    - w (white)

    Additionally the logging levels are colorized as follows:

    - WARNING: yellow
    - INFO: white
    - DEBUG: blue
    - CRITICAL: yellow
    - ERROR: red
    """
    LEVEL_MAP = {
        'WARNING': colors.yellow,
        'INFO': colors.white,
        'DEBUG': colors.blue,
        'CRITICAL': colors.yellow,
        'ERROR': colors.red,
    }
    FUNC_MAP = {
        'm': colors.magenta,
        'b': colors.blue,
        'c': colors.cyan,
        'g': colors.green,
        'y': colors.yellow,
        'w': colors.white,
        'r': colors.red,
    }

    def format(self, record):
        try:
            level_func = self.LEVEL_MAP[record.levelname]
        except KeyError:
            pass
        else:
            # Colorizing the level breaks auto-padding, manually handle
            pad = 7 - len(record.levelname)
            record.levelname = "{0}{1}".format(
                " " * pad,
                level_func(record.levelname)
            )

        # Determine color replacements
        repl_map = {}
        for val in COLOR_EXP.findall(record.msg):
            color_func = self.FUNC_MAP.get(val[1])
            if not color_func:
                continue

            repl_map[val] = color_func(val[3:-1])

        for k, v in repl_map.iteritems():
            record.msg = record.msg.replace(k, v)

        return logging.Formatter.format(self, record)
