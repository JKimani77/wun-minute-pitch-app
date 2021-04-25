from . import db
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin
from . import login_manager

class User(db.Model, UserMixin):
    __tablename__ = 'users'

    id = db.Column(db.Integer,primary_key=True)
    name = db.Column(db.String(225))
    email = db.Column(db.String(255),unique=True)
    pass_secure = db.Column(db.String(255))
    pass_hash = db.Column(db.String(255))
    profile_pic = db.Column(db.String(255))
    pitch = db.relationship('Pitch',backref = 'user',lazy='dynamic')
    #comment = db.relationship('Comment', backref = 'user', lazy= 'dynamic')

    @login_manager.user_loader #gets that user with that id when database query
    def load_user(user_id):
        return User.query.get(int(user_id))

    @property #make password write-only
    def password(self):
        raise AttributeError('You cant read password attribute')
    
    @password.setter #create password hash
    def password(self,password):
        self.pass_secure = generate_password_hash(password)

     #check if hash has bin stored   
    def verify_password(self, password):
        return check_password_hash(self.pass_secure, password)
    
    #for debugging
    def __repr__(self):
        return f'User {self.name}'


class Pitch(db.Model):
    __tablename__ = 'pitches'
    id = db.Column(db.Integer, primary_key=True)
    nametype = db.Column(db.String(255))
    pitch_info = db.Column(db.String(255))
    user_id = db.Column(db.Integer,db.ForeignKey('users.id'))
    #comment = db.relationship('Comment', backref = 'pitch', lazy= 'dynamic')

    def save_pitch(self):
        db.session.add(self)
        db.session.commit()
        
    def getpitchcategory(cls, category):
        pitches = Pitch.query.filter_by(category=category).all()
        return pitches

    def get_pitch_by_id(cls, id):
        allpitches = Pitch.query.filter_by(id = id).all()
        return allpitches