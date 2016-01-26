#!/usr/bin/env python
import unittest
from click.testing import CliRunner

import click_tutorial.cli


class TestTutorialStep1(unittest.TestCase):

    def setUp(self):
        self.runner = CliRunner()

    def test_hello_world_takes_name_option(self):
        result = self.runner.invoke(click_tutorial.cli.cli, ['Dave'])
        assert result.output == 'Hello, Dave!\n'
