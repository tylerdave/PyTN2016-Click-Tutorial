#!/usr/bin/env python
"""
Tutorial Step 02: Options
-------------------------

In this step you will be adding an optional parameter to your command. It
should accept --count with a default of 1 and cause the command to output the
Hello message COUNT number of times.

Options are added using the @click.option() decorator.

Example Input:

pytn --count 3 Dave

Example Output:

Hello, Dave!
Hello, Dave!
Hello, Dave!


See here: http://click.pocoo.org/latest/arguments/
"""
import unittest
from click.testing import CliRunner

import click_tutorial.cli


class TestTutorialStep1(unittest.TestCase):

    def setUp(self):
        self.runner = CliRunner()

    def test_hello_messages_is_output_1_time_by_default(self):
        result = self.runner.invoke(click_tutorial.cli.cli, ['Dave'])
        assert result.output == 'Hello, Dave!\n'

    def test_hello_messages_is_output_count_times(self):
        result = self.runner.invoke(click_tutorial.cli.cli, ['--count', '3', 'Dave'])
        assert result.output == 'Hello, Dave!\nHello, Dave!\nHello, Dave!\n'
