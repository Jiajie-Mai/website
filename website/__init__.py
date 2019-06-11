from flask import Flask, render_template, request, session, url_for, redirect, flash

import os

app = Flask(__name__)

app.secret_key = os.urandom(32)

users = [{'user' : 'alex', 'pass' : 'starwars4'}]

@app.route('/', methods = ["GET", "POST"] )
def disp_login():
    if 'username' in session:
        return render_template("welcome.html", username = session['username'])
    else:
        return redirect('/auth')

@app.route('/auth', methods = ["GET", "POST"] )
def authenticate():
    if request.method == "GET":
        # if logged in
        if 'username' in session:
            return render_template("welcome.html", username = session['username'])
        # if not logged in
        else:
            return render_template("login.html")

    username = request.form['username']
    password = request.form['password']

    ### Invalid username: ===================================
    if username not in users.keys():
        return redirect("/")

    ### Invalid password: ===================================
    elif userDict['alex'] != password:
        return redirect("/")

    ### Both username and password are valid ================
    elif username in userDict.keys() and userDict['alex'] == password:
        session['username'] = username
        return redirect("/")

    ### All other invalid cases =============================
    else:
        return redirect("/")

@app.route('/logout')
def logout():
    session.pop('username')
    flash("You have been successfully logged out.")
    #return ( render_template ( "login.html", message = "You have been successfully logged out."))
    return redirect("/")

if __name__ == "__main__":
    app.debug = True
app.run()
