"""
==============================================================
   - Author: NoName
   - Version: 1.0
   - Since: 4/23/2019
   - Copy right @SmartHome
==============================================================
"""
import logging
from datetime import datetime
from flask_mqtt import Mqtt, MQTT_LOG_ERR

from application import app, db
from services.socketio_service import SocketIoService
from setting import MQTTConfiguration
from models.device_status import DeviceStatus

mqtt = Mqtt()

try:
    mqtt.init_app(app)
except Exception as ex:
    logging.error(f"Init MQTT Error: {ex}")


@mqtt.on_connect()
def handle_connect(client, userdata, flags, rc):
    pass


@mqtt.on_disconnect()
def handle_disconnect(client, userdata, flas, rc):
    pass

@mqtt.on_log()
def handle_logging(self, client, userdata, level, buf):
    if level == MQTT_LOG_ERR:
        logging.info('MQTT-Error: {}'.format(buf))

# @mqtt.on_message()
# def handle_mqtt_message(client, userdata, message):
#     topic = message.topic
#     payload = message.payload.decode()
#
#     # from services.mqtt_service import MQTTService
#     # MQTTService.handle_data_topic(topic, payload)
#
#     if topic == MQTTConfiguration.TOPIC_TEMPERATURE:
#         save_device(payload, 1)
#         SocketIoService.send_message("temperature", payload)
#     elif topic == MQTTConfiguration.TOPIC_HUMIDITY:
#         save_device(payload, 2)
#         SocketIoService.send_message("humidity", payload)
#     elif topic == MQTTConfiguration.TOPIC_LIGHT:
#         save_device(payload, 3)
#         SocketIoService.send_message("light", payload)
#     elif topic == MQTTConfiguration.TOPIC_GAS:
#         save_device(payload, 4)
#         SocketIoService.send_message("gas", payload)
#     elif topic == MQTTConfiguration.TOPIC_FLASH_LIGHT:
#         save_device(payload, 5)
#         SocketIoService.send_message("flashLight", payload)
#
#
# def save_device(value, device_id):
#     try:
#         device_status = DeviceStatus(device_id, value, datetime.now())
#         with app.app_context():
#             db.session.add(device_status)
#             db.session.commit()
#     except Exception as ex:
#         print(ex)

