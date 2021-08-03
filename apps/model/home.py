from apps.model.base import Base
from . import db


class Home(Base):
    __tablename__ = 'home'
    video = db.Column(db.String(255))

    def __init__(self, video, image, title, text):
        super(Home, self).__init__(image=image, title=title, text=text)
        self.video = video

