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

    directions = "make this work!"
    example_input = "command --help"
    example_output = "Help!"
    reference_urls = ['http://www.example.com/']

    def setUp(self):
        self.runner = CliRunner()
        self._tutorial_setup()

    @classmethod
    def print_instructions(cls):
        click.secho('Instructions', bold=True)
        click.secho(cls.directions+'\n', fg='blue')
        click.secho('Example input:', color='white')
        click.secho(cls.example_input+'\n')
        click.secho('Example output:', color='white')
        click.secho(cls.example_output+'\n')

