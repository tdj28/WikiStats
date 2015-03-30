import unittest
from flask import request, jsonify
from mock import patch
from api import app
from decorators.secured import secured


class SecuredTest(unittest.TestCase):
    def test_secured_decorator(self):
        # Create a dummy function to mock a route
        @secured
        def fake_route():
            return 'hello world'

        # Fake out the request ctx without auth
        with app.test_request_context('/'):
            self.assertEquals(('Not Authorized', 401), fake_route())

        # Fake out the request ctx with valid headers
        headers = {'X-Authentication-Token': 'an-auth-token'}
        with app.test_request_context('/', headers=headers):
            self.assertEquals('hello world', fake_route())

    @patch('decorators.secured._validate_authentication_token')
    def test_patched_validation(self, patched_validate):
        @secured
        def fake_route():
            return 'hello world'

        headers = {'X-Authentication-Token': 'another-auth-token'}
        with app.test_request_context('/', headers=headers):
            self.assertEquals('hello world', fake_route())
        self.assertEquals(1, patched_validate.call_count)
        self.assertEquals('another-auth-token',
                          patched_validate.call_args[0][0])
