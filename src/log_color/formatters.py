# Standard
import logging
from logging import LogRecord

# Project
from log_color import colors
from log_color.regex import COLOR_EXP


class ColorStripper(logging.Formatter):
    """
    Strip references to colored output from message.

    This formatter removes all color code text from a message. For example
    it would convert ``this #g<is> text`` to ``this is text``.
    """

    def format(self, record: LogRecord) -> str:
        """Format the message."""
        msg = super().format(record)
        msg = colors.strip_color(msg)
        for val in COLOR_EXP.findall(msg):
            if val.startswith("#d"):
                msg = msg.replace(val, val[4:-1])
            else:
                msg = msg.replace(val, val[3:-1])
        return msg


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

    def format(self, record: LogRecord) -> str:
        """Format the message."""
        msg = super().format(record)
        for val in COLOR_EXP.findall(msg):
            if val.startswith("#d"):
                msg = msg.replace(val, colors.ColorStr(val[4:-1], colors.COLOR_MAP[val[1:3]]))
            else:
                msg = msg.replace(val, colors.ColorStr(val[3:-1], colors.COLOR_MAP[val[1]]))
        return msg
