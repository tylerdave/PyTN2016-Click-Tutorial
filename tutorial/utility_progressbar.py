#!/usr/bin/env python
from .base import BaseTutorialLesson

class TestTutorialProgressbar(BaseTutorialLesson):
    # TODO: Make these actually test progressbar output.

    def test_00_cli_iterable_progress_bar(self):
        result = self.run_command(['iterable-bar'])
        assert result.exit_code == 0

    def test_01_cli_explicit_progress_bar(self):
        result = self.run_command(['explicit-bar'])
        assert result.exit_code == 0

