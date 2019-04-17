
import os
import datetime
import logging
from setting import *
import json

from utils.constants import *
from utils.logger_initializer import initialize_logger

from flask import Flask, request
from flask_sqlalchemy import SQLAlchemy
from flask_mqtt import Mqtt, MQTT_LOG_ERR
from flask_socketio import SocketIO


# Init logger
DIR_PATH = os.path.dirname(os.path.realpath(__file__))
initialize_logger(DIR_PATH)

# Create flask
app = Flask(__name__)

# Add config flask
app.secret_key = os.urandom(SECRET_KEY_LENGTH)
# MQTT Config
app.config[MQTTParam.BROKER_URL] = MQTTConfig.SERVER
app.config[MQTTParam.BROKER_PORT] = MQTTConfig.PORT
app.config[MQTTParam.CLIENT_ID] = MQTTConfig.CLIENT_NAME
app.config[MQTTParam.USERNAME] = MQTTConfig.USER_NAME
app.config[MQTTParam.PASSWORD] = MQTTConfig.PASSWORD
app.config[MQTTParam.KEEP_ALIVE] = MQTTConfig.KEEP_ALIVE
app.config[MQTTParam.TLS_ENABLED] = MQTTConfig.TLS_ENABLED
# SQL Config
app.config[SQLParams.DATABASE_URI] = DatabaseConfig.URI
app.config[SQLParams.TRACK_MODIFICATION] = DatabaseConfig.TRACK_MODIFICATION
app.config[SQLParams.ECHO] = DatabaseConfig.ECHO

# Init other app
mqtt = Mqtt(app)
socketio = SocketIO(app)
db = SQLAlchemy(app)

from models.type_model import TypeModel
from models.device_model import DeviceModel
from models.history_model import HistoryModel

# Register blueprint
from views.home import home
from views.temperature import temperature
app.register_blueprint(home)
app.register_blueprint(temperature)

from services.history_services import HistoryService

clients = []

@socketio.on('connect')
def handle_connect():
    print('Client connected')
    clients.append(request.sid)

@socketio.on('disconnect')
def handle_disconnect():
    print('Client disconnected')
    clients.remove(request.sid)

@socketio.on('publish')
def handle_publish(json_str):
    data = json.loads(json_str)
    mqtt.publish(data['topic'], data['message'])

@socketio.on('subscribe')
def handle_subscribe(json_str):
    data = json.loads(json_str)
    mqtt.subscribe(data['topic'])

@mqtt.on_connect()
def handle_connect(client, userdata, flags, rc):
    pass


@mqtt.on_message()
def handle_mqtt_message(client, userdata, message):
    data = dict(
        topic=message.topic,
        payload=message.payload.decode()
    )
    print(data)
    socketio.emit('temperature', data=data['payload']);
    if data['topic'] == MQTTConfig.TOPIC_TEMPERATURE:
        save_device(data['payload'], 1)
    elif data['topic'] == MQTTConfig.TOPIC_LIGHT:
        save_device(data['payload'], 2)
    elif data['topic'] == MQTTConfig.TOPIC_GAS:
        save_device(data['payload'], 3)
    elif data['topic'] == MQTTConfig.TOPIC_FLASH_LIGHT:
        save_device(data['payload'], 4)
    elif data['topic'] == MQTTConfig.TOPIC_HUMIDITY:
        save_device(data['payload'], 5)

@mqtt.on_log()
def handle_logging(client, userdata, level, buf):
    if level == MQTT_LOG_ERR:
        logging.info('MQTT-Error: {}'.format(buf))




def save_device(value, device_id):
    history = HistoryModel(value, datetime.datetime.now(), device_id)
    db.session.add(history)
    db.session.commit()

def subscribe_topics():
    mqtt.subscribe(MQTTConfig.TOPIC_TEMPERATURE)
    mqtt.subscribe(MQTTConfig.TOPIC_HUMIDITY)
    mqtt.subscribe(MQTTConfig.TOPIC_LIGHT)
    mqtt.subscribe(MQTTConfig.TOPIC_GAS)
    mqtt.subscribe(MQTTConfig.TOPIC_FLASH_LIGHT)



if __name__ == '__main__':
    subscribe_topics()
    app.run(debug=True, host=os.getenv('IP', '0.0.0.0'), port=int(os.getenv('PORT', 80)))
    socketio.run(app)
