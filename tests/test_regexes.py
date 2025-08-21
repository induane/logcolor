from __future__ import annotations

from unittest import TestCase

from log_color import regex


class TestRegexes(TestCase):
    """Test the regular expressions to ensure they can match valid color codes."""

    def test_color_re(self):
        """Valid color codes can be matched with regular expressions."""
        good_vals = (
            "#m<magenta>",
            "#b<blue>",
            "#g<green>",
            "#y<yellow>",
            "#c<cyan>",
            "#w<white>",
            "#db<darkblue>",
            "#dc<darkcyan>",
            "#dg<darkgreen>",
            "#dm<darkmagenta>",
            "#dr<darkred>",
            "#dy<darkyellow>",
        )
        bad_vals = ("Some text", "#f<fuscia>", "#m[magenta]")
        for good_val in good_vals:
            self.assertIsNotNone(regex.COLOR_EXP.match(good_val))

        for bad_val in bad_vals:
            self.assertIsNone(regex.COLOR_EXP.match(bad_val))

    def test_color_extract(self):
        """Regular expression catches all instances on findall."""
        text = (
            "This text has some very colourful words in it like: #m<magenta>, "
            " #b<blue>,  #g<green>,  #y<yellow>,  #c<cyan>, and #w<wh\nite>"
        )
        vals = regex.COLOR_EXP.findall(text)

        for item in (
            "#m<magenta>",
            "#b<blue>",
            "#g<green>",
            "#y<yellow>",
            "#c<cyan>",
            "#w<wh\nite>",
        ):
            if item not in vals:
                raise AssertionError(f"{item} was not detected")
