from flask import redirect, render_template, url_for, session
from api import app

@app.route('/logout')
def logout():
    session.pop('username', None)
    return redirect(url_for('login'))
