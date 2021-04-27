  
from flask import render_template,redirect, url_for,request,flash, abort
from . import main
from .forms import UpdateProfile
from .forms import CreatePitch, CreateComment
from flask_login import current_user, login_required
from ..models import Pitch, User, Comment
from .. import db



#home page
@main.route('/')
def home():
    pitches = Pitch.query.all() 
    
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


#view to create pitch
@main.route('/add',methods = ["GET", "POST"])
@login_required
def create_pitch():
    createpitchform = CreatePitch()
    if createpitchform.validate_on_submit():
        pitchtype = createpitchform.pitchtype.data
        create_peach = Pitch(nametype= pitchtype, pitch_info=createpitchform.pitch.data, user = current_user )
        create_peach.save_pitch()
        return redirect(url_for('main.home'))
    return render_template('peach.html', createpitchform = createpitchform)


#function to create comment
@main.route('/createcomment/<int:id>', methods = ["GET", "POST"])
@login_required
def createcomment(id):
    commentform = CreateComment()
    comment_peach = Pitch.query.get(id)
    if commentform.validate_on_submit():
        newcomment = Comment(thoughts = commentform.comment.data, user = current_user,pitch = comment_peach)
        newcomment.save_comment()

        return redirect(url_for('main.home'))

    return render_template('createcomment.html', commentform = commentform, comment_peach = comment_peach )

# function do get all comments and render them in template
@main.route('/seecomments/<int:id>')
@login_required
def getcomments(id):
    get_comments = Comment.query.filter_by(pitch_id= id).all()
    
    return render_template('seecomments.html', get_comments=get_comments)