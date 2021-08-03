from werkzeug.security import generate_password_hash, check_password_hash
from . import db


class User(db.Model):
    __tablename__ = 'user'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(255))
    password_hash = db.Column(db.String(255))

    def __init__(self, username, password='000000'):
        self.username = username
        self.password = password

    @property
    def password(self):
        return "Password is not readable!"

    @password.setter
    def password(self, value):
        self.password_hash = generate_password_hash(value)

    def check_password(self, user_pwd):
        return check_password_hash(self.password_hash, user_pwd)
