#!/usr/bin/env python
"""
(hello.py) Tutorial Step 02: Options
------------------------------------

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
import click
from click.testing import CliRunner

import click_tutorial


class BaseTutorialStep(unittest.TestCase):

    def setUp(self):
        self.runner = CliRunner()
        self._tutorial_setup()

    def _tutorial_setup(self):
        self.directions = "make this work!"
        self.example_input = "command --help"
        self.example_output = "Help!"
        self.reference_urls = ['http://www.example.com/']

    def print_instructions(self):
        click.secho('Instructions', bold=True)
        click.secho(self.directions, fg='blue')
        click.secho('Example input:', color='white', bold='true')
        click.secho(self.example_input)
        click.secho('Example output:', color='white', bold='true')
        click.secho(self.example_output)

