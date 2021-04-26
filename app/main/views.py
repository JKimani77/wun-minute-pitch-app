  
from flask import render_template,redirect, url_for,request,flash, abort
from . import main
from .forms import UpdateProfile
##from .forms import PitchForm, CommentForm
from flask_login import current_user, login_required
from ..models import Pitch, User, comment
from .. import db



#home page
@main.route('/')
def home():
    pitches = Pitch.query.all()
    if 
    
    return render_template('home.html',pitches=pitches)

#function for profile page
@main.route('/user/<uname>')
def profile(uname):
    user = User.query.filter_by(name = uname).first()

    if user is None:
        abort(404)

    return render_template("profile/profile.html", user = user)

#view to handle editing profile details
@main.route('/user/<uname>/update',methods = ['GET','POST'])
@login_required
def update_profile(uname):
    user = User.query.filter_by(name = uname).first()
    if user is None:
        abort(404)

    form = UpdateProfile()

    if form.validate_on_submit():
        user.bio = form.bio.data

        db.session.add(user)
        db.session.commit()

        return redirect(url_for('.profile',uname=user.name))

    return render_template('profile/update.html',form =form)