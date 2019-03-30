import os
from setting import *
from flask import Flask

from utils import constants
from utils.logger_initializer import initialize_logger


from views.errors.page_not_found import page_not_found

from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

# Register blueprint


# Register error handler
# app.register_error_handler(404, page_not_found)


# @app.route('/')
# def index():
#     return 'Index Page'
#
#
# @app.route('/home')
# def hello_world():
#     return 'Hello World!'

POSTGRES = {
    'user': 'postgres',
    'pw': 'smarthome@2019',
    'db': 'smarthome',
    'host': 'localhost',
    'port': '5432',
}

def init():
    app.secret_key = os.urandom(constants.SECRET_KEY_LENGTH)
    app.config['DEBUG'] = True

import os

DIR_PATH = os.path.dirname(os.path.realpath(__file__))

initialize_logger(DIR_PATH)

app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://%(user)s:%(pw)s@%(host)s:%(port)s/%(db)s' % POSTGRES
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

from models.type_model import TypeModel
from models.device_model import DeviceModel
from models.history_model import HistoryModel

from views.home import home
from views.temperature import temperature
app.register_blueprint(home)
app.register_blueprint(temperature)


if __name__ == '__main__':
    init()
    print (app.config.get('SQLALCHEMY_db_URI'))
    app.run(debug=True, host=os.getenv('IP', '0.0.0.0'), port=int(os.getenv('PORT', 80)))
