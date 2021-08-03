from . import db


class Base(db.Model):
    __tablename__ = 'base'
    id = db.Column(db.Integer, primary_key=True)
    video = db.Column(db.String(255))
    image = db.Column(db.String(255))
    title = db.Column(db.String(255))
    text = db.Column(db.Text)
