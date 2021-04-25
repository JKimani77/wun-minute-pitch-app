from wtforms import SubmitField,TextAreaField
from ..models import User
from flask_wtf import FlaskForm
from wtforms.validators import Required


class UpdateProfile(FlaskForm):
    bio = TextAreaField('Tell us about you.',validators = [Required()])
    submit = SubmitField('Submit')


    ##form fields to create new pitch