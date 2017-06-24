import os

basedir = os.path.abspath(os.path.dirname(__file__))

class Config:
    SECRET_KEY = os.environ['SECRET_KEY']
    MAIL_SERVER = os.environ['MAIL_SERVER']
    MAIL_USERNAME = os.environ['MAIL_USERNAME']
    MAIL_PASSWORD = os.environ['MAIL_PASSWORD']
    MAIL_RECEIVER = os.environ['MAIL_RECEIVER']
    MAIL_PORT = 587
    MAIL_USE_TLS = True

    @staticmethod
    def init_app(app):
        pass

class DevelopmentConfig(Config):
    DEBUG = True


class TestingConfig(Config):
    TESTING = True

class ProductionConfig(Config):
    DEBUG = False
    PROD = True


config = {
    'development': DevelopmentConfig,
    'testing': TestingConfig,
    'production': ProductionConfig,
    'default': DevelopmentConfig
    }