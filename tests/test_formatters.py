# Standard
import logging
from io import StringIO
from unittest import TestCase

# Project
from log_color import colors
from log_color.formatters import ColorFormatter, ColorStripper


class TestColorFormatter(TestCase):
    def setUp(self):
        self.stream = StringIO()
        self.handler = logging.StreamHandler(self.stream)
        formatter = ColorFormatter("%(levelname)s: %(message)s")
        self.handler.setFormatter(formatter)

        self.log = logging.getLogger("test_logger")
        self.log.setLevel(logging.INFO)
        for handler in self.log.handlers:
            self.log.removeHandler(handler)
        self.log.addHandler(self.handler)

    def test_format_matches(self):
        """Test format includes expected output on preformatted strings."""
        base_str = "blue"
        blue_str = colors.ColorStr(base_str, colors.COLOR_MAP["b"])
        expected = f"INFO: this is {blue_str}\n"
        self.log.info(f"this is #b<{base_str}>")
        self.assertEqual(self.stream.getvalue(), expected)

    def test_format_matches_arg_manage(self):
        """Test format includes expected output when formatted with logger args."""
        base_str = "blue"
        blue_str = colors.ColorStr(base_str, colors.COLOR_MAP["b"])
        expected = f"INFO: this is {blue_str}\n"
        self.log.info("this is #b<%s>", base_str)
        self.assertEqual(self.stream.getvalue(), expected)

    def test_format_object(self):
        """Test formatting a non-string object."""
        expected = "INFO: {}\n"
        self.log.info({})
        self.assertEqual(self.stream.getvalue(), expected)


class TestColorStripper(TestCase):
    def setUp(self):
        self.stream = StringIO()
        self.handler = logging.StreamHandler(self.stream)
        formatter = ColorStripper("%(levelname)s: %(message)s")
        self.handler.setFormatter(formatter)

        self.log = logging.getLogger("test_logger")
        self.log.setLevel(logging.INFO)
        for handler in self.log.handlers:
            self.log.removeHandler(handler)
        self.log.addHandler(self.handler)

    def test_format_matches(self):
        """Test format includes expected output."""
        base_str = "blue"
        expected = f"INFO: this is {base_str}\n"
        self.log.info("\033[94mthis\033[0m is #b<%s>", base_str)
        self.assertEqual(self.stream.getvalue(), expected)
