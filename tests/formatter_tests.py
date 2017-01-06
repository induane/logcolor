"""
Formatter Tests
===============
Make sure formatters function as expected
"""
# Standard
import logging
from StringIO import StringIO
from unittest import TestCase

# Project
from log_color import colors
from log_color.formatters import (
    ColorFormatter,
    ColorStripper,
)


class TestColorFormatter(TestCase):

    def setUp(self):
        self.stream = StringIO()
        self.handler = logging.StreamHandler(self.stream)
        formatter = ColorFormatter('%(levelname)s: %(message)s')
        self.handler.setFormatter(formatter)

        self.log = logging.getLogger('test_logger')
        self.log.setLevel(logging.INFO)
        for handler in self.log.handlers:
            self.log.removeHandler(handler)
        self.log.addHandler(self.handler)

    def test_format_matches(self):
        """Test format includes expected output"""
        base_str = "blue"
        blue_str = colors.ColorStr(base_str, colors.COLOR_MAP['b'])
        expected = "INFO: this is {0}\n".format(blue_str)
        self.log.info("this is #b<{0}>".format(base_str))
        self.assertEqual(self.stream.getvalue(), expected)


class TestColorStripper(TestCase):

    def setUp(self):
        self.stream = StringIO()
        self.handler = logging.StreamHandler(self.stream)
        formatter = ColorStripper('%(levelname)s: %(message)s')
        self.handler.setFormatter(formatter)

        self.log = logging.getLogger('test_logger')
        self.log.setLevel(logging.INFO)
        for handler in self.log.handlers:
            self.log.removeHandler(handler)
        self.log.addHandler(self.handler)

    def test_format_matches(self):
        """Test format includes expected output"""
        base_str = "blue"
        expected = "INFO: this is {0}\n".format(base_str)
        self.log.info("\033[94mthis\033[0m is #b<{0}>".format(base_str))
        self.assertEqual(self.stream.getvalue(), expected)
