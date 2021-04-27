from wtforms import SubmitField,TextAreaField, SelectField, ValidationError
from ..models import User, Pitch
from flask_wtf import FlaskForm
from wtforms.validators import Required


class UpdateProfile(FlaskForm):
    bio = TextAreaField('Tell us about you.',validators = [Required()])
    submit = SubmitField('Submit')


    ##form fields to create new pitch

class CreatePitch(FlaskForm):
    pitchtype = SelectField(u'Pitch Type', choices = [('Product-Pitch', 'Product'),('One-Liner', 'One-liner'), ('Promotion-Pitch', 'Promotion')])
    pitch = TextAreaField('post a pitch here')
    submit = SubmitField('Create')

class CreateComment(FlaskForm):
    comment = TextAreaField('what do you think about that pitch')
    vote = SelectField(u'vote', choices = [('One-star', 'One'),('One-star', 'One'),('Two-stars', 'Two'),('Three-stars', 'Three'),('Four-stars', 'Four'),('Five-stars', 'Five')])
    submit = SubmitField('post comment') 