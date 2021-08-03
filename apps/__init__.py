from flask import Flask
from config import DevConfig
from flask_script import Manager
from flask_migrate import Migrate
from flask_restful import Api
from flask_cors import CORS
from apps.model import db
from apps.model.home import HomePage
from apps.model.user import User


def create_app():
    app = Flask(__name__)
    app.config.from_object(DevConfig)
    cors = CORS(app)
    cors.init_app(app)
    api = Api(app=app)
    api.init_app(app)
    migrate = Migrate(app, db)
    migrate.init_app(app)
    manager = Manager(app)
    api.add_resource(HomePage, '/homepage', endpoint='homepage')
    @manager.shell
    def make_shell_context():
        return dict(app=app, db=db, User=User, Page=Page)

    return app
