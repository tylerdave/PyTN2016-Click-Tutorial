#!/usr/bin/env python
from .base import BaseTutorialLesson

class TestTutorialPrompts(BaseTutorialLesson):

    def test_00_cli_with_input_prompt(self):
        result = self.run_command(['prompt1'], input='PyTN')
        assert result.output == "Data: PyTN\ndata: PyTN\n"

    def test_01_cli_with_input_confirmation_yes(self):
        result = self.run_command(['prompt2'], input='yes')
        assert result.output.endswith("OK\n")
        assert result.exit_code == 0

    def test_02_cli_with_input_confirmation_no(self):
        result = self.run_command(['prompt2'], input='no')
        assert result.output.endswith("Aborted!\n")
        assert result.exit_code == 1


