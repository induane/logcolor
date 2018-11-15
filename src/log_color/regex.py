"""Regex."""
# Standard
import re


COLOR_EXP = re.compile(r'#d?[mbcgyrw]<.+?>', re.DOTALL)
