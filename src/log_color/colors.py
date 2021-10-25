# Standard
import os
import sys
import platform
from typing import Dict, FrozenSet, Optional

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


def strip_color(value: str) -> str:
    """Strip all color values from a given string"""
    for seq in ALL_SEQ:
        value = value.replace(seq, "")
    return value


class ColorStr(str):
    """Subclasses string to optionally include ascii color"""

    def __init__(self, *args, **kwargs):
        super().__init__()

    def __new__(cls, value, color, force_seq=None, *args, **kwargs):
        if cls.color_supported(force_seq=force_seq):
            return str.__new__(cls, f"{color}{value}{COLOR_END}")
        return str.__new__(cls, value)

    @staticmethod
    def color_supported(force_seq: Optional[bool] = None) -> bool:
        """Shoddy detection of color support."""
        # If True or False, override autodetection and return.
        if force_seq is False or force_seq is True:
            return force_seq

        # Honor NO_COLOR environment variable:
        if os.environ.get("NO_COLOR", None):
            return False

        # Attempt simple autodetection
        if (hasattr(sys.stderr, "isatty") and sys.stderr.isatty()) or (
            "TERM" in os.environ and os.environ["TERM"] == "ANSI"
        ):
            if "windows" in platform.system().lower() and not ("TERM" in os.environ and os.environ["TERM"] == "ANSI"):
                return False  # Windows console, no ANSI support
            else:
                return True  # ANSI output allowed
        else:
            return False  # ANSI output not allowed
