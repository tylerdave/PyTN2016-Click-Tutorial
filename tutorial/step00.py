#!/usr/bin/env python
from .base import BaseTutorialStep

class TestTutorialStep00(BaseTutorialStep):

    def test_hello_world(self):
        result = self.run_command()
        assert result.output == 'Hello, PyTN!\n'
