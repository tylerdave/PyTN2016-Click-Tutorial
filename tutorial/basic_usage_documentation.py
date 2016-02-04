#!/usr/bin/env python
from .base import BaseTutorialLesson

class TestTutorialBasicSubcommands(BaseTutorialLesson):

    def test_00_cli_without_command_prints_usage(self):
        result = self.run_command()
        assert result.output.startswith('Usage: pytn [OPTIONS] COMMAND [ARGS]...')
        assert result.exit_code == 0

    def test_01_cli_with_status_command(self):
        result = self.run_command(['status'])
        assert result.output == 'status: ok\n'
        assert result.exit_code == 0

    def test_02_cli_wth_invalid_command(self):
        result = self.run_command(['totally-invalid'])
        assert result.output.startswith('Usage: pytn [OPTIONS] COMMAND [ARGS]...')
        assert 'Error: No such command "totally-invalid".' in result.output
        assert result.exit_code == 2


