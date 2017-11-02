# Test Module
from . import TestCase

# Project
from log_color import colors


class TestColorModule(TestCase):

    def test_make_str_magenta(self):
        """Verify can color strings magenta"""
        self.assertEqual(
            colors.ColorStr('colored', colors.COLOR_MAP['m'], force_seq=True),
            '\033[95mcolored\033[0m'
        )

    def test_make_str_blue(self):
        """Verify can color strings blue"""
        self.assertEqual(
            colors.ColorStr('colored', colors.COLOR_MAP['b'], force_seq=True),
            '\033[94mcolored\033[0m'
        )

    def test_make_str_green(self):
        """Verify can color strings green"""
        self.assertEqual(
            colors.ColorStr('colored', colors.COLOR_MAP['g'], force_seq=True),
            '\033[92mcolored\033[0m'
        )

    def test_make_str_yellow(self):
        """Verify can color strings yellow"""
        self.assertEqual(
            colors.ColorStr('colored', colors.COLOR_MAP['y'], force_seq=True),
            "\033[93mcolored\033[0m"
        )

    def test_make_str_red(self):
        """Verify can color strings red"""
        self.assertEqual(
            colors.ColorStr('colored', colors.COLOR_MAP['r'], force_seq=True),
            '\033[91mcolored\033[0m'
        )

    def test_make_str_cyan(self):
        """Verify can color strings cyan"""
        self.assertEqual(
            colors.ColorStr('colored', colors.COLOR_MAP['c'], force_seq=True),
            '\033[96mcolored\033[0m'
        )

    def test_make_str_white(self):
        """Verify can color strings white"""
        self.assertEqual(
            colors.ColorStr('colored', colors.COLOR_MAP['w'], force_seq=True),
            '\033[97mcolored\033[0m'
        )

    def test_make_str_magenta_unsupported(self):
        """Verify no color sequences on magenta"""
        self.assertEqual(
            colors.ColorStr('colored', colors.COLOR_MAP['m'], force_seq=False),
            'colored'
        )

    def test_make_str_blue_unsupported(self):
        """Verify no color sequences on blue"""
        self.assertEqual(
            colors.ColorStr('colored', colors.COLOR_MAP['b'], force_seq=False),
            'colored'
        )

    def test_make_str_green_unsupported(self):
        """Verify no color sequences on green"""
        self.assertEqual(
            colors.ColorStr('colored', colors.COLOR_MAP['g'], force_seq=False),
            'colored'
        )

    def test_make_str_yellow_unsupported(self):
        """Verify no color sequences on yellow"""
        self.assertEqual(
            colors.ColorStr('colored', colors.COLOR_MAP['y'], force_seq=False),
            'colored'
        )

    def test_make_str_red_unsupported(self):
        """Verify no color sequences on red"""
        self.assertEqual(
            colors.ColorStr('colored', colors.COLOR_MAP['r'], force_seq=False),
            'colored'
        )

    def test_make_str_cyan_unsupported(self):
        """Verify no color sequences on cyan"""
        self.assertEqual(
            colors.ColorStr('colored', colors.COLOR_MAP['c'], force_seq=False),
            'colored'
        )

    def test_make_str_white_unsupported(self):
        """Verify no color sequences on white"""
        self.assertEqual(
            colors.ColorStr('colored', colors.COLOR_MAP['w'], force_seq=False),
            'colored'
        )

    def test_plat_det(self):
        """Attempt to run color sequence support detection"""
        # This test doesn't really DO much, but it at least attempts to run the
        # code which is very slightly better than no test at all.
        self.assertIn(colors.ColorStr.color_supported(), (True, False, ))

    def test_strip_colors(self):
        """Make sure colors can be stripped from a string"""
        self.assertEqual(
            colors.strip_color(
                '\033[97mwhite\033[0m \033[96mcyan\033[0m '
                '\033[92mgreen\033[0m'
            ),
            'white cyan green'
        )
