"""
Regex
-----
Precompiled regular expressions used by the logcolor module
"""
# Standard
import re


COLOR_EXP = re.compile(r'%[mbcgyrw]<[^<>]+>')
