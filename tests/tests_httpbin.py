from __future__ import print_function

import os
import httpbin
import unittest
import tempfile
import json

class TestHttpbin(unittest.TestCase):

    def setUp(self):
      #  self.db_fd, httpbin.core.app.config['DATABASE'] = tempfile.mkstemp()
        httpbin.core.app.config['TESTING'] = True
        self.app = httpbin.core.app.test_client()
       # httpbin.core.init_db()

    def tearDown(self):
        #os.close(self.db_fd)
        #os.unlink(httpbin.core.app.config['DATABASE'])

        pass

    def test_homepage(self):
        result = self.app.get('/get?arg1=example')
        result_data = json.loads(result.data.decode('utf8'))
        assert(result_data['args']['arg1'] == 'example')
