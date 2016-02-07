import unittest
from click.testing import CliRunner

import click_tutorial


class BaseTutorialLesson(unittest.TestCase):

    def setUp(self):
        self.runner = CliRunner()
        self.command = click_tutorial.cli.cli

    def run_command(self, arguments=None, **kwargs):
        result = self.runner.invoke(self.command, arguments, **kwargs)
        return result
