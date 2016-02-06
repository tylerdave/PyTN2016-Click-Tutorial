#!/usr/bin/env python
from .base import BaseTutorialLesson

class TestTutorialEchoAndStyle(BaseTutorialLesson):
    # TODO: Make these actually test stdout v. stderr and colored output.

    def test_00_cli_echo(self):
        result = self.run_command(['echo'])
        assert "\nThis is a message.\nThis" in result.output

    def test_01_cli_echo_with_no_newline(self):
        result = self.run_command(['echo', '--no-new-line'])
        assert "\nThis is a message.This" in result.output

    def test_02_cli_style(self):
        result = self.run_command(['style', '--fg', 'red'])
        assert result.output == "This is a message.\n"

    def test_03_cli_secho(self):
        result = self.run_command(['secho', '--fg', 'red'])
        assert result.output == "This is a message.\n"


