from flask import Flask, request, redirect, render_template
import cgi
import os

app = Flask(__name__)
app.config['DEBUG'] = True



@app.route("/")
def display_form():
    return render_template("welcome_form.html", username_error='', password_error='', verifypassword_error='', email_error='')


@app.route("/", methods=['POST'])
def validate_input():
    username = request.form['username']
    password = request.form['password']
    verifypassword = request.form['verifypassword']
    email = request.form['email']

    if len(username) > 20 or len(username) < 3 or " " in username:
        username_error = "Invalid username"
    else:
        username_error = ""

    if len(password) > 20 or len(password) < 3 or " " in password:
        password_error = "Invalid password"
    else:
        password_error = ""

    if password != verifypassword:
        verifypassword_error = "Passwords do not match"
    else:
        verifypassword_error = ""

    if len(email) < 3:
        email_error = "Invalid email"

    if len(email) != 0 and (len(email) > 20 or len(email) < 3):
        email_error = "Invalid email"
    elif " " in email:
        email_error = "Invalid email"
    elif "@" and "." not in email:
        email_error = "Invalid email"
    else:
        email_error = ""

    if not username_error and not password_error and not verifypassword_error and not email_error:
        return redirect('/welcome?username={0}'.format(username))
        
    else:
        return render_template("welcome_form.html", username=username, email=email, username_error=username_error, password_error=password_error, verifypassword_error=verifypassword_error, email_error=email_error)

@app.route("/welcome")
def welcome():
    username = request.args.get('username')
    return render_template("response.html", username=username)

app.run()
