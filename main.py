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

    if len(username) > 20 or len(username) < 3:
        username_error = "Invalid username"
        template = jinja_env.get_template('welcome_form.html')
        return template.render(username_error=username_error)

    if len(password) > 20 or len(password) < 3:
        password_error = "Invalid password"
        template = jinja_env.get_template('welcome_form.html')
        return template.render(password_error=password_error)

    if password != verifypassword:
        verifypassword_error = "Passwords do not match"
        template = jinja_env.get_template('welcome_form.html')
        return template.render(verifypassword_error=verifypassword_error)

@app.route("/welcome", methods=['POST'])
def welcome():
    username = request.form['username']
    template = jinja_env.get_template('response.html')
    return template.render(username=username)    


app.run()