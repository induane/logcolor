"""
Regex Tests
===========
Tests of regular expressions
"""
# Standard
from unittest import TestCase

# Project
from logcolor import regex


class TestRegexes(TestCase):

    def test_url_re(self):
        """Test matching basic urls"""
        good_vals = (
            "%m<magenta>",
            "%b<blue>",
            "%g<green>",
            "%y<yellow>",
            "%c<cyan>",
            "%w<white>",
        )
        bad_vals = (
            "Some text",
            "%f<fuscia>",
        )
        for good_val in good_vals:
            self.assertIsNotNone(regex.COLOR_EXP.match(good_val))

        for bad_val in bad_vals:
            self.assertIsNone(regex.COLOR_EXP.match(bad_val))

    def test_color_extract(self):
        """Make sure regular expression catches all instances on findall"""
        text = (
            "This text has some very colourful words in it like: %m<magenta>, "
            " %b<blue>,  %g<green>,  %y<yellow>,  %c<cyan>, and %w<white>"
        )
        for item in ("%m<magenta>", "%b<blue>",
                     "%g<green>", "%y<yellow>", "%c<cyan>", "%w<white>"):

            self.assertTrue(item in regex.COLOR_EXP.findall(text))
