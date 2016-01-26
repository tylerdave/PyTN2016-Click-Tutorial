#!/usr/bin/env python
"""
Tutorial Step 00: Hello, World!
-------------------------------

This test should be passing already!

"""
import unittest
from click.testing import CliRunner

import click_tutorial.cli


class TestTutorialStep0(unittest.TestCase):

    def setUp(self):
        self.runner = CliRunner()

    def test_hello_world(self):
        result = self.runner.invoke(click_tutorial.cli.cli)
        assert result.output == 'Hello, World!\n'
