#!/usr/bin/env python
from .base import BaseTutorialLesson

class TestTutorialPrompts(BaseTutorialLesson):

    def test_00_cli_with_prompt_option(self):
        result = self.run_command(['prompt1'], input='PyTN')
        assert result.output == "Data: PyTN\ndata: PyTN\n"

    def test_01_cli_with_custom_prompt_option(self):
        result = self.run_command(['prompt2'], input='PyTN')
        assert result.output == "Custom prompt text: PyTN\ndata: PyTN\n"

    def test_02_cli_with_password_prompt(self):
        result = self.run_command(['prompt3'], input='PyTN\nPyTN')
        assert result.output.endswith(
                "Password: \nRepeat for confirmation: \npassword: PyTN\n"
                )

    def test_03_cli_with_password_prompt_helper(self):
        result = self.run_command(['prompt4'], input='PyTN\nPyTN')
        assert result.output.endswith(
                "Password: \nRepeat for confirmation: \npassword: PyTN\n"
                )

    def test_04_cli_with_confirmation_option_answered_yes(self):
        result = self.run_command(['prompt5'], input='yes')
        assert result.output.endswith("Doing something...\n")
        assert result.exit_code == 0

    def test_05_cli_with_confirmation_option_answered_no(self):
        result = self.run_command(['prompt5'], input='no')
        assert result.output.endswith("Aborted!\n")
        assert result.exit_code == 1

