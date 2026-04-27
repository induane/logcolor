from __future__ import annotations

from unittest import TestCase

from log_color.colors import ColorStr
from log_color.formatters import ColorFormatter, ColorStripper
from log_color.lib import COLOR_END, COLOR_MAP
from tests.lib import temp_env, temp_logger


class TestColorFormatter(TestCase):
    def test_format_matches(self):
        """Format includes expected output on preformatted strings."""
        base_str = "blue"
        blue_str = ColorStr(base_str, COLOR_MAP["b"])
        expected = f"INFO: this is {blue_str}\n"
        with temp_logger(ColorFormatter) as (log, stream):
            log.info(f"this is #b<{base_str}>")
            self.assertEqual(stream.getvalue(), expected)

    def test_format_matches_arg_manage(self):
        """Format includes expected output when formatted with logger args."""
        base_str = "blue"
        blue_str = ColorStr(base_str, COLOR_MAP["b"])
        expected = f"INFO: this is {blue_str}\n"
        with temp_logger(ColorFormatter) as (log, stream):
            log.info("this is #b<%s>", base_str)
            self.assertEqual(stream.getvalue(), expected)

    def test_format_object(self):
        """Non-string objects can be formatted."""
        expected = "INFO: {}\n"
        with temp_logger(ColorFormatter) as (log, stream):
            log.info({})
            self.assertEqual(stream.getvalue(), expected)

    def test_multiple_colors_in_one_message(self):
        """Multiple color tokens in one message are each converted."""
        a = "blue"
        b = "red"
        blue_str = ColorStr(a, COLOR_MAP["b"])
        red_str = ColorStr(b, COLOR_MAP["r"])
        expected = f"INFO: this is {blue_str} and {red_str}\n"
        with temp_logger(ColorFormatter) as (log, stream):
            log.info("this is #b<%s> and #r<%s>", a, b)
            self.assertEqual(stream.getvalue(), expected)

    def test_dark_color_token(self):
        """Dark color tokens (two-letter codes) are handled."""
        val = "dark"
        dark_str = ColorStr(val, COLOR_MAP["db"])
        expected = f"INFO: sample {dark_str}\n"
        with temp_logger(ColorFormatter) as (log, stream):
            log.info("sample #db<%s>", val)  # Use the #d prefix for dark colors as defined in the DSL (#db<...>)
            self.assertEqual(stream.getvalue(), expected)

    def test_complex_formatter_includes_colored_message(self):
        """Complex formatter with asctime/name/lineno still contains colored content."""
        with temp_logger(ColorFormatter, fmt="%(levelname)-8s: %(asctime)s '%(message)s' %(name)s:%(lineno)s") as (
            log,
            stream,
        ):
            # The assertion focuses on the presence of the colored portion rather than exact timestamp/lineno
            log.info("complex #g<message>")
            out = stream.getvalue()
            green = ColorStr("message", COLOR_MAP["g"])
            self.assertIn(str(green), out)


class TestColorStripper(TestCase):
    def test_format_matches(self):
        """Format includes expected output."""
        base_str = "blue"
        expected = f"INFO: this is {base_str}\n"
        with temp_logger(ColorStripper) as (log, stream):
            log.info("\033[94mthis\033[0m is #b<%s>", base_str)
            self.assertEqual(stream.getvalue(), expected)

    def test_strips_multiple_and_dark_sequences(self):
        """Stripper should remove both escape sequences and DSL tokens (including dark colors)."""
        a = "one"
        b = "two"
        # Include an explicit escape-coded portion and DSL tokens for both regular and dark color codes
        with temp_logger(ColorStripper) as (log, stream):
            log.info("\033[94mlead\033[0m middle #b<%s> end #db<%s>", a, b)
            expected = f"INFO: lead middle {a} end {b}\n"
            self.assertEqual(stream.getvalue(), expected)

    def test_strips_from_complex_formatter(self):
        """When used with a more complex formatter the ColorStripper removes color sequences from the message portion."""
        with temp_logger(ColorStripper, fmt="%(levelname)-8s: %(asctime)s '%(message)s' %(name)s:%(lineno)s") as (
            log,
            stream,
        ):
            # Message contains both explicit escape sequences and DSL tokens
            log.info("\033[95mhead\033[0m #m<mid> tail")
            out = stream.getvalue()
            # The output should not contain any raw escape sequences or DSL markers
            self.assertNotIn(COLOR_END, out)
            self.assertNotIn("#m<", out)
            self.assertIn("head mid tail", out)

    def test_no_color_env_disables_colorformatter(self):
        """NO_COLOR environment variable should prevent ColorFormatter from emitting ANSI sequences."""
        with temp_env(NO_COLOR="1"):
            with temp_logger(ColorFormatter) as (log, stream):
                log.info("this is #b<blue> and #db<darkblue>")
                out = stream.getvalue()
                # No ANSI sequences from the color map should be present when NO_COLOR is set
                for seq in COLOR_MAP.values():
                    self.assertNotIn(seq, out)
                # The plain text values should still be present
                self.assertIn("blue", out)
                self.assertIn("darkblue", out)

    def test_no_color_env_with_colorstr_direct(self):
        """ColorStr should honor NO_COLOR when constructed directly (no ANSI in result)."""
        with temp_env(NO_COLOR="1"):
            # Construct ColorStr directly; with NO_COLOR set it should not include COLOR_END
            s = ColorStr("x", COLOR_MAP["g"])
            self.assertNotIn(COLOR_END, str(s))
            # And equality to plain string should hold
            self.assertEqual(str(s), "x")
