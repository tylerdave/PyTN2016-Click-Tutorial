#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
test_click_tutorial
----------------------------------

Tests for `click_tutorial` module.
"""

import unittest

import click_tutorial


class TestPytn2016_click_tutorial(unittest.TestCase):

    def setUp(self):
        pass

    def test_something(self):
        assert(click_tutorial.hello_world())
        pass

    def tearDown(self):
        pass
