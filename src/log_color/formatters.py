"""
Custom Formatters
=================
"""
# Standard
import logging

from log_color import colors
from log_color import compat
from log_color.regex import COLOR_EXP


def _cast_message(message):
    """Attempt to cast a value as a string if it isn't one."""
    if isinstance(message, compat.string_types):
        return message
    else:
        try:
            return compat.text_type(message)
        except Exception:
            return message  # Don't fail here but there *could* be problems


class ColorStripper(logging.Formatter):
    """
    Strips all references to colored output from the logging message. This is
    useful for passing messages to a file logger where color sequences are not
    desired.
    """
    def format(self, record):
        """Format the message."""
        message = _cast_message(record.msg)
        message = colors.strip_color(message)
        for val in COLOR_EXP.findall(record.msg):
            message = message.replace(val, val[3:-1])
        record.msg = message
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
        """Format the message."""
        message = _cast_message(record.msg)
        for val in COLOR_EXP.findall(message):
            message = message.replace(
                val,
                colors.ColorStr(val[3:-1], colors.COLOR_MAP[val[1]])
            )
        record.msg = message
        return logging.Formatter.format(self, record)
