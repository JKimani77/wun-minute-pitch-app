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
    vote = SelectField(u'vote', choices = [('One-star', '1-Star'),('Two-star', '2 Stars'),('Two-stars', '2-Stars'),('Three-stars', '3-Stars'),('Four-stars', '4-Stars'),('Five-stars', '5-Stars')])
    submit = SubmitField('post comment') 