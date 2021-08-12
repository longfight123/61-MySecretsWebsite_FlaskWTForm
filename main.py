"""My secrets website

This 'Flask' app website has 4 web pages. The index, success, denied, and login page.
The template 'base.html' is used as a parent template where all other templates
inherit the same design using 'Jinja' templating. The username to access the secret
is admin@gmail.com and the password is '12345678'.

This script requires that 'Flask', 'Flask-WTF' and 'Flask-Bootstrap' be installed within the Python
environment you are running this script in.

"""

from flask import Flask, render_template
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired, Email, Length
from flask_bootstrap import Bootstrap

#Create the WTForm fields
class MyForm(FlaskForm):
    """
    A class used to create a WTForm.

    ...

    Attributes
    ----------
    email: str
        a StringField to enter emails
    password: str
        a PasswordField

    """
    email = StringField(label='email', validators=[DataRequired(message='Field must be entered.'), Email(message= 'Enter a valid email')])
    password = PasswordField(label='password', validators=[DataRequired(message='Field must be entered.'), Length(min=6, message=
                                                                                                                  'Field must be atleast 6 characters long')])
    submit = SubmitField(label='submit')
#Create the app and load the templtes into the app? This is from the basic usage documentation for flask-bootstrap
def create_app():
    """loads the Bootstrap extension"""
    app = Flask(__name__)
    Bootstrap(app)
    return app

app = create_app()
app.secret_key = "some secret string"

@app.route("/")
def home():
    """the landing page

    GET: Landing page
    """
    return render_template('index.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    """the login page

    GET: login page
    POST: redirects to success.html/denied.html
    """
    form = MyForm()
    # Only returns true or false when the form is actually submitted through a POST
    if form.validate_on_submit():
        if form.email.data == 'admin@gmail.com' and form.password.data =='12345678':
            return render_template('success.html')
        else:
            return render_template('denied.html')
    # Renders the template if the method is a GET
    return render_template('login.html', form=form)

if __name__ == '__main__':
    app.run(debug=True)