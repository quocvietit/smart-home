"""
==============================================================
   - Author: NoName
   - Version: 1.0
   - Since: 5/4/2019
   - Copy right @SmartHome
==============================================================
"""
from datetime import datetime

from setting import MQTTConfiguration
from extenstion.mqtt_core import mqtt
from application import db, app, socketio
from models.device_status import DeviceStatus



@mqtt.on_message()
def handle_mqtt_message(client, userdata, message):
    topic = message.topic
    payload = message.payload.decode()

    # from services.mqtt_service import MQTTService
    # MQTTService.handle_data_topic(topic, payload)

    if topic == MQTTConfiguration.TOPIC_TEMPERATURE:
        save_device(payload, 1)
    elif topic == MQTTConfiguration.TOPIC_HUMIDITY:
        save_device(payload, 2)
    elif topic == MQTTConfiguration.TOPIC_LIGHT:
        save_device(payload, 3)
    elif topic == MQTTConfiguration.TOPIC_GAS:
        save_device(payload, 4)
    elif topic == MQTTConfiguration.TOPIC_FLASH_LIGHT:
        save_device(payload, 5)

    socketio.send_message("temperature", payload)


def save_device(value, device_id):
    try:
        device_status = DeviceStatus(device_id, value, datetime.now())
        with app.app_context():
            db.session.add(device_status)
            db.session.commit()
    except Exception as ex:
        print(ex)
