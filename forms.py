from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired

class UserForm(FlaskForm):
    username = StringField("Username", validators=[DataRequired(message="Username is required")])
    email = StringField("Email", validators=[DataRequired(message="Email is required")])
    submit = SubmitField("Submit")