from . import db


class Base(db.Model):
    __tablename__ = 'base'
    id = db.Column(db.Integer, primary_key=True)
    image = db.Column(db.String(255))
    title = db.Column(db.String(255))
    text = db.Column(db.Text)

    def __init__(self, image, title, text):
        self.image = image
        self.title = title
        self.text = text
