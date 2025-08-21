from __future__ import annotations

from unittest import TestCase


class TestImports(TestCase):
    """
    Test that the formatters can be successfully imported.

    This is a seemingly silly test, but I had a reason for doing this long ago which has
    been lost to history. Perhaps it was a good reason. Perhaps not.
    """

    def test_import_color_stripper(self):
        """ColorStripper can be successfully imported."""
        try:
            from log_color import ColorStripper  # noqa
        except ImportError as ie:
            raise AssertionError("Unable to import ColorStripper from module") from ie

    def test_import_color_formatter(self):
        """ColorFormatter can be successfully imported."""
        try:
            from log_color import ColorFormatter  # noqa
        except ImportError as ie:
            raise AssertionError("Unable to import ColorFormatter from module") from ie
