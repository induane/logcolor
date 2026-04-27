from doctest import DocTestSuite
from unittest import BaseTestSuite, TestLoader

from log_color import lib


def load_tests(loader: TestLoader, tests: BaseTestSuite, ignore: str) -> BaseTestSuite:
    """Add doctests to the testsuite."""
    tests.addTests(DocTestSuite(lib))
    return tests
