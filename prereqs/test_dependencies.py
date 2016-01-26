#!/usr/bin/env python

import json
import unittest

class TestHttpbin(unittest.TestCase):

    def setUp(self):
        import httpbin
        httpbin.core.app.config['TESTING'] = True
        self.app = httpbin.core.app.test_client()

    def test_httpbin_responds(self):
        result = self.app.get('/get?arg=example_value')
        result_data = json.loads(result.data.decode('utf8'))
        assert (result_data.get('args', {}).get('arg', {}) == 'example_value'), \
                 "Didn't get the argument value returned as expected. " \
                 "Is httpbin installed and working correctly?"

class TestRequests(unittest.TestCase):

    def test_requests_installed(self):
        import requests
        parsed_url = requests.utils.urlparse("http://www.example.com/path?arg1=value1#anchor1")
        assert (parsed_url[0] == 'http')


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

class TestReqcli(unittest.TestCase):

    def test_reqcli_installed(self):
        import reqcli

