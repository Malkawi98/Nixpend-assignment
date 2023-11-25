import phonenumbers
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired, ValidationError
from wtforms.validators import InputRequired, Email


class Signup(FlaskForm):
    fullName = StringField('Full Name', validators=[InputRequired()], render_kw={"autocomplete": "off"})
    email = StringField('Email', validators=[InputRequired(), Email()], render_kw={"autocomplete": "off"})
    phone = StringField('Phone', validators=[DataRequired()], render_kw={"autocomplete": "off"})
    submit = SubmitField('Submit', render_kw={'placeholder': 'Generate Card'})