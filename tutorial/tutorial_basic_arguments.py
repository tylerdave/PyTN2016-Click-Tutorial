#!/usr/bin/env python
from .base import BaseTutorialLesson

class TestTutorialBasicArguments(BaseTutorialLesson):

    def test_00_hello_world_with_single_argument(self):
        result = self.run_command(['PyTennessee'])
        assert result.output == 'Hello, PyTennessee!\n'

    def test_01_hello_world_with_three_arguments(self):
        result = self.run_command(['PyTN', 'Pythonistas', 'Everybody'])
        assert result.output == "Hello, PyTN!\nHello, Pythonistas!\nHello, Everybody!\n"

    def test_02_hello_world_with_more_arguments(self):
        result = self.run_command(['PyTN', 'A', 'b', 'C', '1', '2'])
        assert result.output == "Hello, PyTN!\nHello, A!\nHello, b!\nHello, C!\nHello, 1!\nHello, 2!\n"
