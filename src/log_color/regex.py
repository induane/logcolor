"""
Regex
-----
Precompiled regular expressions used by the log_color module
"""
# Standard
import re


COLOR_EXP = re.compile(r'#[mbcgyrw]<.+?>', re.DOTALL)
