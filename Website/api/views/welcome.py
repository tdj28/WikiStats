from flask import redirect, render_template, url_for, session
from api import app
from decorators.login_required import login_required

@app.route('/')
@login_required(session)
def welcome():
     return render_template('welcome.html', username=session['username'])