# Standard
from unittest import TestCase

# Project
from logcolor import colors


class TestColorModule(TestCase):

    def test_make_str_magenta(self):
        """Verify can color strings magenta"""
        self.assertEqual(
            colors.magenta("colored"),
            "\033[95mcolored\033[0m"
        )

    def test_make_str_blue(self):
        """Verify can color strings blue"""
        self.assertEqual(
            colors.blue("colored"),
            "\033[94mcolored\033[0m"
        )

    def test_make_str_green(self):
        """Verify can color strings green"""
        self.assertEqual(
            colors.green("colored"),
            "\033[92mcolored\033[0m"
        )

    def test_make_str_yellow(self):
        """Verify can color strings yellow"""
        self.assertEqual(
            colors.yellow("colored"),
            "\033[93mcolored\033[0m"
        )

    def test_make_str_red(self):
        """Verify can color strings red"""
        self.assertEqual(
            colors.red("colored"),
            "\033[91mcolored\033[0m"
        )

    def test_make_str_cyan(self):
        """Verify can color strings cyan"""
        self.assertEqual(
            colors.cyan("colored"),
            "\033[96mcolored\033[0m"
        )

    def test_make_str_white(self):
        """Verify can color strings white"""
        self.assertEqual(
            colors.white("colored"),
            "\033[97mcolored\033[0m"
        )

    def test_strip_colors(self):
        """Make sure colors can be stripped from a string"""
        self.assertEqual(
            colors.strip_color(
                "\033[97mwhite\033[0m \033[96mcyan\033[0m "
                "\033[92mgreen\033[0m"
            ),
            "white cyan green"
        )
