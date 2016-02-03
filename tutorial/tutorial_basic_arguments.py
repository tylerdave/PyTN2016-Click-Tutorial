#!/usr/bin/env python
from .base import BaseTutorialLesson

class TestTutorialBasicArguments(BaseTutorialLesson):

    def test_00_cli_with_single_argument(self):
        result = self.run_command(['PyTennessee'])
        assert result.output == 'name: PyTennessee\n'

    def test_01_cli_with_three_arguments(self):
        result = self.run_command(['PyTN', 'Pythonistas', 'Everybody'])
        assert result.output == "name: PyTN\nname: Pythonistas\nname: Everybody\n"

    def test_02_cli_with_more_arguments(self):
        result = self.run_command(['PyTN', 'A', 'b', 'C', '1', '2'])
        assert result.output == "name: PyTN\nname: A\nname: b\nname: C\nname: 1\nname: 2\n"
