"""
Tools for colored terminal output
"""
import os
import sys
import platform

from log_color import compat

COLOR_MAP = {
    'b': u'\033[94m',
    'c': u'\033[96m',
    'g': u'\033[92m',
    'm': u'\033[95m',
    'r': u'\033[91m',
    'y': u'\033[93m',
    'w': u'\033[97m',

    'db': u'\033[34m',
    'dc': u'\033[36m',
    'dg': u'\033[32m',
    'dm': u'\033[35m',
    'dr': u'\033[31m',
    'dy': u'\033[33m',
}

COLOR_END = '\033[0m'
# Assemble list of all color sequences
ALL_SEQ = frozenset([x for x in COLOR_MAP.values()] + [COLOR_END, ])


def strip_color(value):
    """Strip all color values from a given string"""
    for seq in ALL_SEQ:
        value = value.replace(seq, '')
    return value


class ColorStr(compat.text_type):
    """Subclasses string to optionally include ascii color"""

    def __init__(self, *args, **kwargs):
        super(ColorStr, self).__init__()

    def __new__(cls, value, color, force_seq=None, *args, **kwargs):
        if cls.color_supported(force_seq=force_seq):
            return compat.text_type.__new__(cls, u"{0}{1}{2}".format(
                color,
                value,
                COLOR_END
            ))
        return compat.text_type.__new__(cls, value)

    @staticmethod
    def color_supported(force_seq=None):
        """Shoddy detection of color support."""
        # If True or False, override autodetection and return.
        if force_seq is False or force_seq is True:
            return force_seq

        # Honor NO_COLOR environment variable:
        if os.environ.get('NO_COLOR', None):
            return False

        # Attempt simple autodetection
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
