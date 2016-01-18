#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
test_click_tutorial
----------------------------------

Tests for `click_tutorial` module.
"""

import unittest

import click_tutorial


class TestClickTutorial(unittest.TestCase):

    def setUp(self):
        pass

    def test_hello_world(self):
        assert(click_tutorial.hello_world())
        pass

    def test_httpbin(self):
        pass

    def tearDown(self):
        pass
