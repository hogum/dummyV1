from flask_wtf import FlaskForm
from wtforms import TextField, SubmitField, validators


class Contact(FlaskForm):
    name = TextField('Name of User', validators=[validators.Required()])
    email = TextField('What\'s your email?')
    submit = SubmitField('Submit')
