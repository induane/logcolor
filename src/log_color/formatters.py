"""Custom Formatters."""
# Standard
import logging

from log_color import (colors, compat, )
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
    Strip references to colored output from message.

    This formatter removes all color code text from a message. For example
    it would convert ``this #g<is> text`` to ``this is text``.
    """
    def format(self, record):
        """Format the message."""
        message = _cast_message(record.msg)
        message = colors.strip_color(message)
        for val in COLOR_EXP.findall(record.msg):
            if val.startswith("#d"):
                message = message.replace(val, val[4:-1])
            else:
                message = message.replace(val, val[3:-1])
        record.msg = message
        return logging.Formatter.format(self, record)


class ColorFormatter(logging.Formatter):
    """
    Insert color sequences for logging messages.

    Convert all portions of a message that contain color codes into a ColorStr
    instance that matches the color map data then re-insert it into the
    message. On supported platforms this will insert a color codes around the
    specified text.

    Color sequences should be in the following format: #y<message> which will
    be formatted as yellow. The colors allowed are:

    - m (magenta)
    - b (blue)
    - c (cyan)
    - g (green)
    - y (yellow)
    - r (red)
    - w (white)

    - dm (dark magenta)
    - db (dark blue)
    - dc (dark cyan)
    - dg (dark green)
    - dy (dark yellow)
    - dr (dark red)
    """
    def format(self, record):
        """Format the message."""
        message = _cast_message(record.msg)
        for val in COLOR_EXP.findall(message):
            if val.startswith("#d"):
                message = message.replace(
                    val,
                    colors.ColorStr(val[4:-1], colors.COLOR_MAP[val[1:3]])
                )
            else:
                message = message.replace(
                    val,
                    colors.ColorStr(val[3:-1], colors.COLOR_MAP[val[1]])
                )
        record.msg = message
        return logging.Formatter.format(self, record)
