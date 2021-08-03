from flask import Flask
from config import DevConfig
from flask_script import Manager
from flask_migrate import Migrate
from flask_restful import Api
from flask_cors import CORS
from apps.model import db
from apps.model.home import Home
from apps.model.user import User
from apps.view.user import user_bp
from apps.view.page import page_bp, HomeResourse


def create_app():
    app = Flask(__name__)
    app.config.from_object(DevConfig)
    app.register_blueprint(user_bp)
    app.register_blueprint(page_bp)
    db.init_app(app)
    cors = CORS(app)
    cors.init_app(app)
    api = Api(app=app)
    api.init_app(app)
    migrate = Migrate(app, db)
    migrate.init_app(app)
    manager = Manager(app)
    api.add_resource(HomeResourse, '/home', endpoint='home')
    app.app_context().push()

    db.drop_all()
    db.create_all()
    print(Home.__tablename__)

    @manager.shell
    def make_shell_context():
        return dict(app=app, db=db, Home=Home, User=User)

    return app
