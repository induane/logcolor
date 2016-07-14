"""
Tools for colored terminal output
"""

COLOR_MAP = {
    'BLUE': u'\033[94m',
    'CYAN': u'\033[96m',
    'GREEN': u'\033[92m',
    'MAGENTA': u'\033[95m',
    'RED': u'\033[91m',
    'WHITE': u'\033[97m',
    'YELLOW': u'\033[93m',
}

COLOR_END = '\033[0m'
# Assemble list of all color sequences
ALL_SEQ = [x[1] for x in COLOR_MAP.iteritems()] + [COLOR_END, ]


def magenta(value):
    """Color the given string Magenta"""
    return u"{0}{1}{2}".format(COLOR_MAP['MAGENTA'], value, COLOR_END)


def blue(value):
    """Color the given string Blue"""
    return u"{0}{1}{2}".format(COLOR_MAP['BLUE'], value, COLOR_END)


def green(value):
    """Color the given string Purple"""
    return u"{0}{1}{2}".format(COLOR_MAP['GREEN'], value, COLOR_END)


def yellow(value):
    """Color the given string Yellow"""
    return u"{0}{1}{2}".format(COLOR_MAP['YELLOW'], value, COLOR_END)


def red(value):
    """Color the given string Red"""
    return u"{0}{1}{2}".format(COLOR_MAP['RED'], value, COLOR_END)


def cyan(value):
    """Color the given string Cyan"""
    return u"{0}{1}{2}".format(COLOR_MAP['CYAN'], value, COLOR_END)


def white(value):
    """Color the given string White"""
    return u"{0}{1}{2}".format(COLOR_MAP['WHITE'], value, COLOR_END)


def strip_color(value):
    """Strip all color values from a given string"""
    for seq in ALL_SEQ:
        value = value.replace(seq, '')
    return value
