from flask import redirect, render_template, url_for, session
from api import app
from decorators.login_required import login_required

@app.route('/apiaccess')
@login_required(session)
def apiaccess():
     return render_template('apiaccess.html', username=session['username'])