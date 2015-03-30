from api import app
from flask import request, render_template, redirect, url_for, flash, make_response, session
from decorators.login_required import login_required
from api import mysql

@app.route('/login', methods=['GET', 'POST'])
def login():
    error = None
    if request.method == 'POST':
        if valid_login(
            request.form.get('username'),
            request.form.get('password')
        ):
            flash("Successfully logged in.")
            session['username'] = request.form.get('username')
            return redirect(url_for('welcome'))
        else:
            error = "Incorrect username and password"
            app.logger.warning("Incorrect username and password for user {}".format(request.form.get("username")))
    return render_template('login.html', error=error)

def valid_login(username, password):
    cursor = mysql.connect().cursor()
    cursor.execute("SELECT username, password FROM user WHERE username='{0}' AND password='{1}'".format(username,password))
    data = cursor.fetchone()
    if data:
        return True
    else:
        return False
