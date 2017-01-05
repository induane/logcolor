"""
Tools for colored terminal output
"""
import os
import sys
import platform


class ColorStr(unicode):
    """Subclasses string to include ascii color"""

    def __init__(self, *args, **kwargs):
        super(ColorStr, self).__init__()

    def __new__(cls, value, color, *args, **kwargs):
        if cls.color_supported():
            return unicode.__new__(cls, "{0}{1}\033[0m".format(color, value))
        else:
            return unicode.__new__(cls, value)

    @staticmethod
    def color_supported():
        """Shoddy detection for color support"""
        if (
            (hasattr(sys.stderr, "isatty") and sys.stderr.isatty()) or
            ('TERM' in os.environ and os.environ['TERM'] == 'ANSI')
        ):
            if (
                'windows' in platform.system().lower() and not
                ('TERM' in os.environ and os.environ['TERM'] == 'ANSI')
            ):
                return False  # Windows console, no ANSI support
            else:
                return True  # ANSI output allowed
        else:
            return False  # ANSI output not allowed


COLOR_MAP = {
    'b': u'\033[94m',
    'c': u'\033[96m',
    'g': u'\033[92m',
    'm': u'\033[95m',
    'r': u'\033[91m',
    'w': u'\033[97m',
    'y': u'\033[93m',
}

COLOR_END = '\033[0m'
# Assemble list of all color sequences
ALL_SEQ = [x for x in COLOR_MAP.values()] + [COLOR_END, ]


def strip_color(value):
    """Strip all color values from a given string"""
    for seq in ALL_SEQ:
        value = value.replace(seq, '')
    return value
