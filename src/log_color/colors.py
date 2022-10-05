import os
import platform
import sys
from functools import lru_cache
from typing import Optional

from .lib import COLOR_END


class ColorStr(str):
    """Subclasses string to optionally include ascii color"""

    def __new__(cls, value: str, color: str, force_seq: Optional[bool] = None) -> "ColorStr":
        if cls.color_supported(force_seq=force_seq):
            return str.__new__(cls, f"{color}{value}{COLOR_END}")
        return str.__new__(cls, value)

    @staticmethod
    @lru_cache(maxsize=None)
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
