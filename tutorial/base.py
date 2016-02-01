import unittest
from click.testing import CliRunner

import click_tutorial


class BaseTutorialStep(unittest.TestCase):

    def setUp(self):
        self.runner = CliRunner()
        self.command = click_tutorial.cli.cli

    def run_command(self, arguments=None):
        result = self.runner.invoke(self.command, arguments)
        return result
