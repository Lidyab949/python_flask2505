# Our site's login/sign-up form
from wsgiref.validate import validator

# Get the required modules
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, EmailField, PasswordField, BooleanField
from wtfforms.validators import DataRequired, Length

#Declare the Login Form class
class LoginForm(FlaskForm):
    email = EmailField('Email', validators=[DataRequired()],
                      render_kw={'placeholder': 'me@email.com',
                                 'title': 'Please enter your email', 'tabindex':10})
    password = PasswordField('Password', validators=[DataRequired(),Length(min=8)],
                             render_kw={'placeholder':'Secret password', 'tabindex':20})
    # optional remember me checkbox
    remeber = BooleanField('Remember me')

    # Submit and Reset buttons
    submit = SubmitField('Login',
                         render_kw={'title': 'Login/sign-in to the site',
                                   'tabindex':30})
    reset = SubmitField('Reset',
                         render_kw={'title': 'Clear all fields',
                                    'tabindex': 90})

