import json
import unittest
from api import app
from api.views import hits


class AuthenticationTest(unittest.TestCase):
    def setUp(self):
        self.app = app.test_client()

# To start with, can we submit the right token and get the right results?
    def test_hitme_good(self):
        headers = {'X-Authentication-Token': 'an-auth-token'}
        res = self.app.post('/hits/', headers=headers)
        self.assertEquals('an-auth-token-hit',
                          json.loads(res.data).get('token'))

# Next, let's submit a bad token, we should not get the right result:
    def test_hitme_bad(self):
        headers = {'X-Authentication-Token': 'fake-auth-token'}
        res = self.app.post('/hits/', headers=headers)
        self.assertEquals('Not Authorized', res.data)
