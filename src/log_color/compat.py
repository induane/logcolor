import sys

# Python2/3 compat
if sys.version_info[0] == 3:
    text_type = str
    binary_type = bytes
    string_types = (str, )
else:
    text_type = unicode
    binary_type = str
    string_types = (basestring, )
