from flask import Flask, request
import cgi
import os
import jinja2

template_dir = os.path.join(os.path.dirname(__file__), 'templates')
jinja_env = jinja2.Environment(loader = jinja2.FileSystemLoader (template_dir), autoescape=True)

app = Flask(__name__)
app.config['DEBUG'] = True



@app.route("/")
def display_form():
    template = jinja_env.get_template('welcome_form.html')
    return template.render(username_error='', password_error='', verifypassword_error='', email_error='')


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

    if len(email) != 0 and (len(email) > 20 or len(email) < 3 or " " in email:
        email_error = "Invalid email"
    else:
        email_error = ""

        template = jinja_env.get_template('welcome_form.html')
        return template.render(username_error=username_error, p#assword_error=password_error, #verifypassword_error=verifypassword_error)

#how do I change whether it redirects to a welcome page or stays on form?
#how do I keep the username in the form but clear out password?
#how do I set up "if errors = 0" then we're good?

@app.route("/", methods=['POST'])
def greeting():
    username = request.form['username']
    template = jinja_env.get_template('response.html')
    return template.render(username=username)

app.run()
