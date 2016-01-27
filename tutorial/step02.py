#!/usr/bin/env python
"""
Tutorial Step 02: Options
-------------------------

In this step you will be adding an optional parameter to your command. It
should accept --count with a default of 1 and cause the command to output the
Hello message COUNT number of times.

Options are added using the @click.option() decorator.

Example Input:

hello --count 3 PyTN

Or:

hello -c 3 PyTN

Example Output:

Hello, PyTN!
Hello, PyTN!
Hello, PyTN!


See here: http://click.pocoo.org/latest/options/
"""
import unittest
from click.testing import CliRunner

import click_tutorial


class TestTutorialStep02(unittest.TestCase):

    def setUp(self):
        self.runner = CliRunner()

    def test_hello_messages_is_output_1_time_by_default(self):
        result = self.runner.invoke(click_tutorial.cli.cli, ['PyTN'])
        assert result.output == 'Hello, PyTN!\n'

    def test_hello_messages_is_output_count_times(self):
        result = self.runner.invoke(click_tutorial.hello.cli, ['--count', '3', 'PyTN'])
        assert result.output == 'Hello, PyTN!\nHello, PyTN!\nHello, PyTN!\n'

    def test_hello_messages_is_output_count_times_with_short_option(self):
        result = self.runner.invoke(click_tutorial.hello.cli, ['-c', '3', 'PyTN'])
        assert result.output == 'Hello, PyTN!\nHello, PyTN!\nHello, PyTN!\n'
