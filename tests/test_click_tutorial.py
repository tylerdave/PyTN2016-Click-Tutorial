#!/usr/bin/env python
import unittest

import click_tutorial.cli


class TestClickTutorial(unittest.TestCase):

    def test_hello_world(self):
        assert click_tutorial.cli.cli()
