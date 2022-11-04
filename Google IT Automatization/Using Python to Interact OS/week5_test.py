#!/usr/bin/env python3
from week5 import rearrange_name
import unittest


class TestWeek5(unittest.TestCase):
    def test_basic(self):
        testcase = "Rios, Julian"
        expected = "Julian, Rios"
        self.assertEqual(rearrange_name(testcase), expected)

    def test_empty(self):
        testcase = ""
        expected = ""
        self.assertEqual(rearrange_name(testcase), expected)


unittest.main()
