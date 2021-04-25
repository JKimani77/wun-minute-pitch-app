from wtforms import SubmitField,TextAreaField
from ..models import User


class UpdateProfile(FlaskForm):
    bio = TextAreaField('Tell us about you.',validators = [Required()])
    submit = SubmitField('Submit')


    ##form fields to create new pitch