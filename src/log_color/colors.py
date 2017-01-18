"""
Tools for colored terminal output
"""
import os
import sys
import platform

# Python2/3 compat
if sys.version_info[0] == 3:
    text_type = str
    binary_type = bytes
else:
    text_type = unicode
    binary_type = str


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
ALL_SEQ = frozenset([x for x in COLOR_MAP.values()] + [COLOR_END, ])


def strip_color(value):
    """Strip all color values from a given string"""
    for seq in ALL_SEQ:
        value = value.replace(seq, '')
    return value


class ColorStr(text_type):
    """Subclasses string to optionally include ascii color"""

    def __init__(self, *args, **kwargs):
        super(ColorStr, self).__init__()

    def __new__(cls, value, color, force_seq=None, *args, **kwargs):
        if cls.color_supported(force_seq=force_seq):
            return text_type.__new__(cls, u"{0}{1}{2}".format(
                color,
                value,
                COLOR_END
            ))
        return text_type.__new__(cls, value)

    @staticmethod
    def color_supported(force_seq=None):
        """Shoddy detection for color support"""
        # If True or False, override autodetection and return. Using "or" here
        # is slightly faster than in (True, False, ) as it short circuits
        if force_seq is False or force_seq is True:
            return force_seq

        # Attempt on to autodetection
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
