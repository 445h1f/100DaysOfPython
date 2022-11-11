from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired, Length, Email

class LoginForm(FlaskForm):
    """Creating Login form."""

    email = StringField(label='E-Mail: ', validators=[DataRequired(), Email()]) #string field with email validation
    password = PasswordField(label='Password: ', validators=[DataRequired(), Length(min=8)]) # password field with min 8 characters
    submit = SubmitField(label='Log in')
