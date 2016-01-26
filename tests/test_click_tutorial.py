#!/usr/bin/env python
import unittest
from click.testing import CliRunner

import click_tutorial.cli


class TestClickTutorial(unittest.TestCase):

    def setUp(self):
        self.runner = CliRunner()

    def test_hello_world(self):
        result = self.runner.invoke(click_tutorial.cli.cli)
        assert result.output == 'Hello, World!\n'
