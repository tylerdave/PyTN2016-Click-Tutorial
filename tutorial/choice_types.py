#!/usr/bin/env python
from .base import BaseTutorialLesson

class TestChoiceTypes(BaseTutorialLesson):

    # TODO: add tests

    def test_00_cli_valid_letter_choice(self):
        result = self.run_command(['--letter', 'b'])
        assert "letter: b\n" in result.output

    def test_01_cli_invalid_letter_choice(self):
        result = self.run_command(['--letter', 'x'])
        assert 'Error: Invalid value for "--letter"' in result.output
        assert result.exit_code == 2

    def test_02_cli_valid_number_choice(self):
        result = self.run_command(['--number', '50'])
        assert "number: 50\n" in result.output

    def test_03_cli_invalid_number_choice(self):
        result = self.run_command(['--number', '101'])
        assert 'Error: Invalid value for "--number"' in result.output
        assert result.exit_code == 2

    def test_04_cli_valid_clamped_number_choice(self):
        result = self.run_command(['--clamped-number', '50'])
        assert "clamped_number: 50\n" in result.output

    def test_05_cli_invalid_clamped_number_choice(self):
        result = self.run_command(['--clamped-number', 'x'])
        assert 'Error: Invalid value for "--clamped-number"' in result.output
        assert result.exit_code == 2

    def test_06_cli_valid_clamped_number_choice(self):
        result = self.run_command(['--clamped-number', '101'])
        assert "clamped_number: 100\n" in result.output

    def test_07_cli_valid_clamped_number_choice(self):
        result = self.run_command(['--clamped-number', '-100'])
        assert "clamped_number: 0\n" in result.output


