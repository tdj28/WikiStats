import json
import unittest
from api import app


class AuthenticationTest(unittest.TestCase):
    def setUp(self):
        self.app = app.test_client()

    def test_authentication(self):
        headers = {'X-Authentication-Token': 'an-auth-token'}
        res = self.app.post('/auth/', headers=headers)
        self.assertEquals('an-auth-token', json.loads(res.data).get('token'))
