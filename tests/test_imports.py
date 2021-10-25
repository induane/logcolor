# Standard
from unittest import TestCase


class TestImports(TestCase):
    def test_import_color_stripper(self):
        """Test importing ColorStripper."""
        try:
            from log_color import ColorStripper  # noqa
        except ImportError:
            raise AssertionError("Unable to import ColorStripper from module")

    def test_import_color_formatter(self):
        """Test importing ColorFormatter."""
        try:
            from log_color import ColorFormatter  # noqa
        except ImportError:
            raise AssertionError("Unable to import ColorFormatter from module")
