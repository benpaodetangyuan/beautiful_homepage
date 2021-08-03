class Config(object):
    SECRET_KEY = '123'
    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://root:Dev%40123@localhost:3306/little_test?charset:utf8'
    SQLALCHEMY_TRACK_MODIFICATIONS = 'FALSE'


class ProdConfig(Config):
    pass


class DevConfig(Config):
    ENV = 'DEVELOPMENT'
    DEBUG = True