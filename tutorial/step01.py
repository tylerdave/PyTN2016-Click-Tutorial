#!/usr/bin/env python
"""
Tutorial Step 01: Arguments
---------------------------

In this step you will be adding a positional argument to your command. It
should accept a NAME and print that name instead of 'World'.

Arguments are added using the @click.argument() decorator.

Example Input:

pytn Dave

Example Output:

Hello, Dave!


See here: http://click.pocoo.org/latest/arguments/
"""
import unittest
from click.testing import CliRunner

import click_tutorial.cli


class TestTutorialStep1(unittest.TestCase):

    def setUp(self):
        self.runner = CliRunner()

    def test_hello_world_takes_name_option(self):
        result = self.runner.invoke(click_tutorial.cli.cli, ['Dave'])
        assert result.output == 'Hello, Dave!\n'
