"""
LogColor Tests
==============
Test module for LogColor and custom TestCase with additional asserts
"""
# Standard
from unittest import TestCase as BaseTestCase


class TestCase(BaseTestCase):

    def assertIn(self, item, collection, msg=None):
        self.assertTrue(item in collection, msg)

    def assertIsNone(self, item, msg=None):
        self.assertTrue(item is None, msg)

    def assertIsNotNone(self, item, msg=None):
        self.assertTrue(item is not None, msg)

    def assertIsInstance(self, item, type_, msg=None):
        self.assertTrue(isinstance(item, type_), msg)

    def assertIs(self, item1, item2, msg=None):
        self.assertTrue(item1 is item2, msg)

    def assertGreaterEqual(self, a, b, msg=None):
        self.assertTrue(a >= b, msg)

    def assertLessEqual(self, a, b, msg=None):
        self.assertTrue(a <= b, msg)
