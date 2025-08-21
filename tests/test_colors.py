from __future__ import annotations

from unittest import TestCase

from log_color.colors import ColorStr
from log_color.lib import COLOR_MAP, strip_color


class TestColorModule(TestCase):
    def test_make_str_magenta(self):
        """Strings can be output as magenta."""
        self.assertEqual(
            "\033[95mcolored\033[0m",
            ColorStr("colored", COLOR_MAP["m"], force_seq=True),
        )

    def test_make_str_blue(self):
        """Strings can be output as blue."""
        self.assertEqual(
            ColorStr("colored", COLOR_MAP["b"], force_seq=True),
            "\033[94mcolored\033[0m",
        )

    def test_make_str_green(self):
        """Strings can be output as green."""
        self.assertEqual(
            "\033[92mcolored\033[0m",
            ColorStr("colored", COLOR_MAP["g"], force_seq=True),
        )

    def test_make_str_yellow(self):
        """Strings can be output as yellow."""
        self.assertEqual(
            "\033[93mcolored\033[0m",
            ColorStr("colored", COLOR_MAP["y"], force_seq=True),
        )

    def test_make_str_red(self):
        """Strings can be output as red."""
        self.assertEqual(
            "\033[91mcolored\033[0m",
            ColorStr("colored", COLOR_MAP["r"], force_seq=True),
        )

    def test_make_str_cyan(self):
        """Strings can be output as cyan."""
        self.assertEqual(
            "\033[96mcolored\033[0m",
            ColorStr("colored", COLOR_MAP["c"], force_seq=True),
        )

    def test_make_str_white(self):
        """Strings can be output as white."""
        self.assertEqual(
            "\033[97mcolored\033[0m",
            ColorStr("colored", COLOR_MAP["w"], force_seq=True),
        )

    def test_make_str_dark_magenta(self):
        """Strings can be output as dark magenta."""
        self.assertEqual(
            "\033[35mcolored\033[0m",
            ColorStr("colored", COLOR_MAP["dm"], force_seq=True),
        )

    def test_make_str_dark_blue(self):
        """Strings can be output as dark blue."""
        self.assertEqual(
            ColorStr("colored", COLOR_MAP["db"], force_seq=True),
            "\033[34mcolored\033[0m",
        )

    def test_make_str_dark_green(self):
        """Strings can be output as dark green."""
        self.assertEqual(
            "\033[32mcolored\033[0m",
            ColorStr("colored", COLOR_MAP["dg"], force_seq=True),
        )

    def test_make_str_dark_yellow(self):
        """Strings can be output as dark yellow."""
        self.assertEqual(
            "\033[33mcolored\033[0m",
            ColorStr("colored", COLOR_MAP["dy"], force_seq=True),
        )

    def test_make_str_dark_red(self):
        """Strings can be output as dark red."""
        self.assertEqual(
            ColorStr("colored", COLOR_MAP["dr"], force_seq=True),
            "\033[31mcolored\033[0m",
        )

    def test_make_str_dark_cyan(self):
        """Strings can be output as dark cyan."""
        self.assertEqual(
            "\033[36mcolored\033[0m",
            ColorStr("colored", COLOR_MAP["dc"], force_seq=True),
        )

    def test_make_str_magenta_unsupported(self):
        """Verify no color sequences on magenta when color codes are not supported."""
        self.assertEqual("colored", ColorStr("colored", COLOR_MAP["m"], force_seq=False))

    def test_make_str_blue_unsupported(self):
        """Verify no blue sequences when color codes are not supported."""
        self.assertEqual("colored", ColorStr("colored", COLOR_MAP["b"], force_seq=False))

    def test_make_str_green_unsupported(self):
        """Verify no green sequences when color codes are not supported."""
        self.assertEqual("colored", ColorStr("colored", COLOR_MAP["g"], force_seq=False))

    def test_make_str_yellow_unsupported(self):
        """Verify no yellow sequences when color codes are not supported."""
        self.assertEqual("colored", ColorStr("colored", COLOR_MAP["y"], force_seq=False))

    def test_make_str_red_unsupported(self):
        """Verify no red sequences when color codes are not supported."""
        self.assertEqual("colored", ColorStr("colored", COLOR_MAP["r"], force_seq=False))

    def test_make_str_cyan_unsupported(self):
        """Verify no cyan sequences when color codes are not supported."""
        self.assertEqual("colored", ColorStr("colored", COLOR_MAP["c"], force_seq=False))

    def test_make_str_white_unsupported(self):
        """Verify no white sequences when color codes are not supported."""
        self.assertEqual("colored", ColorStr("colored", COLOR_MAP["w"], force_seq=False))

    def test_make_str_dark_magenta_unsupported(self):
        """Verify no color sequences on dark magenta when color codes are not supported."""
        self.assertEqual("colored", ColorStr("colored", COLOR_MAP["dm"], force_seq=False))

    def test_make_str_dark_blue_unsupported(self):
        """Verify no color sequences on dark blue when color codes are not supported."""
        self.assertEqual("colored", ColorStr("colored", COLOR_MAP["db"], force_seq=False))

    def test_make_str_dark_green_unsupported(self):
        """Verify no color sequences on dark green when color codes are not supported."""
        self.assertEqual("colored", ColorStr("colored", COLOR_MAP["dg"], force_seq=False))

    def test_make_str_dark_yellow_unsupported(self):
        """Verify no color sequences on dark yellow when color codes are not supported."""
        self.assertEqual("colored", ColorStr("colored", COLOR_MAP["dy"], force_seq=False))

    def test_make_str_dark_red_unsupported(self):
        """Verify no color sequences on dark red when color codes are not supported."""
        self.assertEqual("colored", ColorStr("colored", COLOR_MAP["dr"], force_seq=False))

    def test_make_str_dark_cyan_unsupported(self):
        """Verify no color sequences on dark cyan when color codes are not supported."""
        self.assertEqual("colored", ColorStr("colored", COLOR_MAP["dc"], force_seq=False))

    def test_plat_det(self):
        """Attempt to run color sequence support detection when color codes are not supported."""
        # This test doesn't really DO much, but it at least attempts to run the
        # code which is very slightly better than no test at all.
        self.assertIn(ColorStr.color_supported(), (True, False))

    def test_strip_colors(self):
        """Colors can be stripped from a string."""
        self.assertEqual(
            strip_color("\033[97mwhite\033[0m \033[96mcyan\033[0m \033[92mgreen\033[0m"),
            "white cyan green",
        )
