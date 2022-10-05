import re
from functools import lru_cache
from typing import Dict, FrozenSet, List, Match, Sequence, Tuple

SUBMAP_TYPE = Sequence[Tuple[str, str]]
"""Substitution mapping type."""

COLOR_MAP: Dict[str, str] = {
    "b": "\033[94m",
    "c": "\033[96m",
    "g": "\033[92m",
    "m": "\033[95m",
    "r": "\033[91m",
    "y": "\033[93m",
    "w": "\033[97m",
    "db": "\033[34m",
    "dc": "\033[36m",
    "dg": "\033[32m",
    "dm": "\033[35m",
    "dr": "\033[31m",
    "dy": "\033[33m",
}

COLOR_END: str = "\033[0m"
# Assemble list of all color sequences
ALL_SEQ: FrozenSet[str] = frozenset([x for x in COLOR_MAP.values()] + [COLOR_END])


class MultiReplace:
    """
    MultiReplace is a tool for doing multiple find/replace actions in one pass.

    Given a mapping of values to be replaced it allows for all of the matching values to be replaced in a single pass
    which can save a lot of performance on very large strings. In addition to simple replace, it also allows for
    replacing based on regular expressions.

    Keyword Arguments:

    :type regex: bool
    :param regex: Treat search keys as regular expressions [Default: False]
    :type flags: int
    :param flags: flags to pass to the regex engine during compile

    Usage::

        from boltons import stringutils
        s = stringutils.MultiReplace((
            ('foo', 'zoo'),
            ('cat', 'hat'),
            ('bat', 'kraken)'
        ))
        new = s.sub('The foo bar cat ate a bat')
        new == 'The zoo bar hat ate a kraken'
    """

    def __init__(self, sub_map: SUBMAP_TYPE) -> None:
        """Compile any regular expressions that have been passed."""
        self.group_map: Dict[str, str] = {}
        regex_values: List[str] = []

        for idx, vals in enumerate(sub_map):
            group_name = f"group{idx}"
            exp = re.escape(vals[0])
            regex_values.append(f"(?P<{group_name}>{exp})")
            self.group_map[group_name] = vals[1]

        self.combined_pattern = re.compile("|".join(regex_values))

    def _get_value(self, match: Match) -> str:
        """Given a match object find replacement value."""
        group_dict = match.groupdict()
        key = [x for x in group_dict if group_dict[x]][0]
        return self.group_map[key]

    def sub(self, text: str) -> str:
        """Run substitutions on the input text."""
        try:
            return self.combined_pattern.sub(self._get_value, text)
        except IndexError:
            # There are no matches so just return the original text
            return text


def multi_replace(text: str, sub_map: SUBMAP_TYPE) -> str:
    """
    Shortcut function to invoke MultiReplace in a single call.

    Example Usage::

        from boltons.stringutils import multi_replace
        new = multi_replace(
            'The foo bar cat ate a bat',
            {'foo': 'zoo', 'cat': 'hat', 'bat': 'kraken'}
        )
        new == 'The zoo bar hat ate a kraken'
    """
    m = MultiReplace(sub_map)
    return m.sub(text)


@lru_cache(maxsize=None)
def get_strip_map() -> Tuple[Tuple[str, str], ...]:
    return tuple((x, "") for x in ALL_SEQ)


def strip_color(value: str) -> str:
    """Strip all color values from a given string"""
    return multi_replace(value, get_strip_map())
