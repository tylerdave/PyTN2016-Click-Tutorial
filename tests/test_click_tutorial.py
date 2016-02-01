#!/usr/bin/env python
import unittest
from click.testing import CliRunner

import click_tutorial.hello


class TestClickTutorial(unittest.TestCase):

    def setUp(self):
        self.runner = CliRunner()

    def test_hello_world(self):
        result = self.runner.invoke(click_tutorial.hello.cli, ['World'])
        assert result.output == 'Hello, World.\n'

    def test_hello_world_when_excited(self):
        result = self.runner.invoke(click_tutorial.hello.cli, ['World', '-e'])
        assert result.output == 'Hello, World!\n'

    def test_hello_world_help_message(self):
        result = self.runner.invoke(click_tutorial.hello.cli, ['--help'])
        assert "Given a NAME, outputs a greeting." in result.output
