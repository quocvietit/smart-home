"""
==============================================================
   - Author: NoName
   - Version: 1.0
   - Since: 4/26/2019
   - Copy right @SmartHome
==============================================================
"""
import os
from utils.logger_initializer import initialize_logger
from flask import Flask

from configs.database_config import DatabaseConfig
from configs.mqtt_config import MQTTConfig
from configs.config import Config
from configs.mail_config import MailConfig
from flask_sqlalchemy import SQLAlchemy

def init_app():
    # Create flask
    app = Flask(__name__)

    # Add config flask
    DatabaseConfig(app)
    Config(app)
    MQTTConfig(app)
    MailConfig(app)

    app.app_context().push()

    return app


def init_log(xpath):
    # Init logger
    DIR_PATH = os.path.dirname(xpath)
    initialize_logger(DIR_PATH)


def register_bluesprint(app):
    from controllers.home import home
    from controllers.device_controller import device_controller
    from controllers.device_status_controller import device_status_controller
    from controllers.mail_controller import mail_controller
    from controllers.test_controler import test as t

    app.register_blueprint(home)
    app.register_blueprint(device_controller)
    app.register_blueprint(device_status_controller)
    app.register_blueprint(mail_controller)
    app.register_blueprint(t)


def register_topic():
    from services.util_service import UtilService

    UtilService.init_subscribe_topic()
