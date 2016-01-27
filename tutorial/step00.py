#!/usr/bin/env python
"""
Tutorial Step 00: Hello, World!
-------------------------------

This test should pass when you first start. Once you start adding features it
will begin to fail.

"""
import unittest
from click.testing import CliRunner

import click_tutorial


class TestTutorialStep00(unittest.TestCase):

    def setUp(self):
        self.runner = CliRunner()

    def test_hello_world(self):
        result = self.runner.invoke(click_tutorial.hello.cli)
        assert result.output == 'Hello, World!\n'
