from flask import redirect, url_for, session
from functools import wraps
from api import app, mysql


def login_required(session):
    def decorator(f):
        @wraps(f)
        def decorated_function(*args, **kwargs):
            if f:
                if 'username' not in session:
                    return redirect(url_for('login'))
            return f(*args, **kwargs)
        return decorated_function
    return decorator

