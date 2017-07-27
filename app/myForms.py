from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField
from wtforms.validators import InputRequired, Email, Length

class SignUpForm(FlaskForm):
    username = StringField("Name of User", validators=[InputRequired(), Length(min=5, max=10, message="Length needs to be between 5 and 10")])
    email = StringField("email", validators=[Email()])
    password = PasswordField("password", validators=[InputRequired()])

class LoginForm(FlaskForm):
    email = StringField("email", validators=[Email()])
    password = PasswordField("password", validators=[InputRequired()])