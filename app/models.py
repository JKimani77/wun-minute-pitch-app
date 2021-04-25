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
    comment = db.relationship('Comment', backref = 'user', lazy= 'dynamic')

    @login_manager.user_loader
    def load_user(user_id):
        return User.query.get(int(user_id))

    def password(self):
        raise AttributeError('You cant read password attribute')
    
    def password(self,password):
        self.pass_secure = generate_password_hash(password)
        
    def verify_password(self, password):
        return check_password_hash(self.pass_secure, password)
    
    def __repr__(self):
        return f'User {self.name}'