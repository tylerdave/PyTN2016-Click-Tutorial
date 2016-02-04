#!/usr/bin/env python
from .base import BaseTutorialLesson

class TestTutorialBasicArguments(BaseTutorialLesson):

    def test_00_cli_with_single_argument(self):
        result = self.run_command()
        assert result.output == 'Hello, PyTN!\n'
