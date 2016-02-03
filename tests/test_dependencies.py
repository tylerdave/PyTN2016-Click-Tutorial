#!/usr/bin/env python

import json
import unittest

class TestClick(unittest.TestCase):

    def test_click_installed(self):
        import click
        term_x, term_y = click.get_terminal_size()
        assert isinstance(term_x, int)
        assert isinstance(term_y, int)


class TestColorama(unittest.TestCase):

    def test_clorama_installed(self):
        import colorama
        assert colorama.Style.BRIGHT == '\x1b[1m'

