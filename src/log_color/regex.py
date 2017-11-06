"""Regex."""
# Standard
import re


COLOR_EXP = re.compile(r'#[mbcgyrw]<.+?>', re.DOTALL)
