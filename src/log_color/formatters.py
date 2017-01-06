"""
Custom Formatters
=================
"""
# Standard
import logging

from log_color import colors
from log_color.regex import COLOR_EXP


class ColorStripper(logging.Formatter):
    """
    Strips all references to colored output from the logging message. This is
    useful for passing messages to a file logger where color sequences are not
    desired.
    """
    def format(self, record):
        # Strip any color sequences
        record.msg = colors.strip_color(record.msg)
        for val in COLOR_EXP.findall(record.msg):
            record.msg = record.msg.replace(val, val[3:-1])
        return logging.Formatter.format(self, record)


class ColorFormatter(logging.Formatter):
    """
    Adds in color sequences for logging messages. They are to be provided in
    the format: #y<message> which will be formatted as yellow. The colors
    allowed are:

    - m (magenta)
    - b (blue)
    - c (cyan)
    - g (green)
    - y (yellow)
    - r (red)
    - w (white)
    """
    def format(self, record):
        # Determine color replacements
        for val in COLOR_EXP.findall(record.msg):
            record.msg = record.msg.replace(
                val,
                colors.ColorStr(val[3:-1], colors.COLOR_MAP[val[1]])
            )
        return logging.Formatter.format(self, record)
