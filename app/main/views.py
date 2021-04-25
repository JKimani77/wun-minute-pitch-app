  
from flask import render_template,redirect, url_for,request,flash, abort
from . import main
##from .forms import PitchForm, CommentForm
##from flask_login import current_user, login_required
from ..models import Pitch,User ###comment
##from .. import photos,db

@main.route('/')
def home():
    pitches = Pitch.query.all()
    
    return render_template('home.html',pitches=pitches)


@main.route('/user/<uname>')
def profile(uname):
    user = User.query.filter_by(name = uname).first()

    if user is None:
        abort(404)

    return render_template("profile/profile.html", user = user)

