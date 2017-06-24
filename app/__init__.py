from flask import Flask, render_template
from flask_mail import Message, Mail
from config import config


mail = Mail()

def create_app(config_name):
    app = Flask(__name__)
    app.config.from_object(config[config_name])
    config[config_name].init_app(app)
    mail.init_app(app)

    # registering blueprints
    from .main import main as main_blueprint
    app.register_blueprint(main_blueprint)
    return app
