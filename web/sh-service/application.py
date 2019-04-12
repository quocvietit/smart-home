import os
import datetime
import logging
from setting import *
from flask import Flask

from utils import constants
from utils.logger_initializer import initialize_logger


from flask_sqlalchemy import SQLAlchemy
from flask_mqtt import Mqtt

app = Flask(__name__)
app.config['MQTT_BROKER_URL'] = 'localhost'  # use the free broker from HIVEMQ
app.config['MQTT_BROKER_PORT'] = 1883  # default port for non-tls connection
app.config['MQTT_CLIENT_ID'] = 'raspberry'
app.config['MQTT_USERNAME'] = 'pi'  # set the username here if you need authentication for the broker
app.config['MQTT_PASSWORD'] = '123'  # set the password here if the broker demands authentication
app.config['MQTT_KEEPALIVE'] = 60  # set the time interval for sending a ping to the broker to 5 seconds
app.config['MQTT_TLS_ENABLED'] = False
mqtt = Mqtt(app)

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
    'pw': 'admin',
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

from services.history_services import HistoryService

@mqtt.on_connect()
def handle_connect(client, userdata, flags, rc):
    print ("AHihi")



@mqtt.on_message()
def handle_mqtt_message(client, userdata, message):
    data = dict(
        topic=message.topic,
        payload=message.payload.decode()
    )
    print (data)
    if data['topic'] == MQTT.TOPIC_TEMPERATURE:
        save_device(data['payload'], 1)
    elif data['topic'] == MQTT.TOPIC_LIGHT:
        save_device(data['payload'], 2)
    elif data['topic'] == MQTT.TOPIC_GAS:
        save_device(data['payload'], 3)
    elif data['topic'] == MQTT.TOPIC_FLASH_LIGHT:
        save_device(data['payload'], 4)
    elif data['topic'] == MQTT.TOPIC_HUMIDITY:
        save_device(data['payload'], 5)


def save_device(value, device_id):
    history = HistoryModel(value, datetime.datetime.now(),device_id)
    db.session.add(history)
    db.session.commit()
    HistoryService.save(value, device_id)

if __name__ == '__main__':
    init()
    mqtt.subscribe(MQTT.TOPIC_TEMPERATURE)
    mqtt.subscribe(MQTT.TOPIC_HUMIDITY)
    mqtt.subscribe(MQTT.TOPIC_LIGHT)
    mqtt.subscribe(MQTT.TOPIC_GAS)
    mqtt.subscribe(MQTT.TOPIC_FLASH_LIGHT)
    logging.info(app.config.get('SQLALCHEMY_DATABASE_URI'))
    app.run(debug=True, host=os.getenv('IP', '0.0.0.0'), port=int(os.getenv('PORT', 80)))

