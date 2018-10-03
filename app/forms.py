from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from .models import User


class LoginForm(FlaskForm):
    username = StringField('Username')
    password = PasswordField('Password')
    submit = SubmitField('Sign In')
