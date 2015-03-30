from flask import request
from functools import wraps


def _validate_authentication_token(token):
    return token == 'an-auth-token'


def secured(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        if 'X-Authentication-Token' in request.headers and \
                _validate_authentication_token(
                request.headers.get('X-Authentication-Token')):
            return f(*args, **kwargs)
        else:
            return 'Not Authorized', 401
    return decorated
