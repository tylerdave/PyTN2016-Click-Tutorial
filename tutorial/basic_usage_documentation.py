#!/usr/bin/env python
import re

from .base import BaseTutorialLesson

class TestTutorialBasicUsageDocumentation(BaseTutorialLesson):

    def test_00_cli_gets_help_output_from_docstring(self):
        result = self.run_command(['--help'])
        assert result.output.startswith('Usage: pytn')
        assert "Outputs messages." in result.output

    def test_01_cli_includes_help_text_from_option(self):
        result = self.run_command(['--help'])
        assert re.search("--input-string1 TEXT\W+Optional input string\.", result.output)

    def test_02_cli_help_has_renamed_variables(self):
        result = self.run_command(['--help'])
        assert re.search("--input-string2 <string>\W+Another optional input string\.", result.output)

    def test_03_cli_with_subcommand_shows_short_help(self):
        result = self.run_command(['--help'])
        assert re.search("hello\W+Says hello\.", result.output)
