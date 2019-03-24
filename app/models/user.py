from app import db
from app.models.role import roles_users
from flask_security import UserMixin

__author__ = 'Carlos Diaz'
__version__ = '1.0'
__email__ = 'alberto.carlos@gmail.com'


class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(255), unique=True)
    password = db.Column(db.String(255))
    active = db.Column(db.Boolean())
    confirmed_at = db.Column(db.DateTime())
    roles = db.relationship('Role', secondary=roles_users,
                            backref=db.backref('users', lazy='dynamic'))

    def verify_password(self, input_password):
        #from flask_security.utils import verify_password
        from werkzeug.security import check_password_hash
        return check_password_hash(input_password, self.password)

    def __init__(self, id_user, email, password, active):
        self.id = id_user
        self.email = email
        self.password = password
        self.active = active

    def __repr__(self):
        return '<User {0} {1} >'.format(self.email, self.active)
