#!/usr/bin/env python
from .base import BaseTutorialLesson

class TestFileTypes(BaseTutorialLesson):

    # TODO: add tests


    def test_00_cli_file_input_stdout(self):
        with self.runner.isolated_filesystem():
            with open('infile.txt', 'w') as f:
                f.write('Input data.')
            result = self.run_command(['infile.txt'])
            assert 'Input data.\n' in result.output

    def test_01_cli_file_input_file_output(self):
        with self.runner.isolated_filesystem():
            with open('infile.txt', 'w') as f:
                f.write('Input data.')
            result = self.run_command(['infile.txt', 'outfile.txt'])
            with open('outfile.txt', 'r') as f:
                data = f.read()
            assert data == 'Input data.\n'
            assert 'Input data.' not in result.output

    def test_02_cli_stdin_file_output(self):
        with self.runner.isolated_filesystem():
            result = self.run_command(['-', 'outfile.txt'], input="Input data.")
            with open('outfile.txt', 'r') as f:
                data = f.read()
            assert data == 'Input data.\n'
            assert 'Input data.' not in result.output
