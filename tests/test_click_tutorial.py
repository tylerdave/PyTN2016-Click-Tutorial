#!/usr/bin/env python
import unittest
from click.testing import CliRunner

import click_tutorial.cli


class TestClickTutorial(unittest.TestCase):

    def setUp(self):
        self.runner = CliRunner()

    def test_hello_world(self):
        result = self.runner.invoke(click_tutorial.hello.cli)
        assert result.output == 'Hello, World!\n'

    def test_pytn_command(self):
        result = self.runner.invoke(click_tutorial.cli.cli, ['http://localhost:5000/get'])
        assert result.output == 'GET http://localhost:5000/get\n'
