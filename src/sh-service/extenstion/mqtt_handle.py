"""
==============================================================
   - Author: NoName
   - Version: 1.0
   - Since: 5/4/2019
   - Copy right @SmartHome
==============================================================
"""
from datetime import datetime
import requests
import json
import logging

from setting import MQTTConfiguration
from extenstion.mqtt_core import mqtt
from application import db, app
from models.device_status import DeviceStatus
from services.socketio_service import SocketIoService
from services.mail_service import MailService
from utils.IP import ip

IP = ip().getIP()

@mqtt.on_message()
def handle_mqtt_message(client, userdata, message):
    topic = message.topic
    payload = message.payload.decode()

    # from services.mqtt_service import MQTTService
    # MQTTService.handle_data_topic(topic, payload)

    if topic == MQTTConfiguration.TOPIC_TEMPERATURE:
        save_device(payload, 1)
        if int(payload) >=40 or int(payload) <= 10:
           notification(1)
        print("send temperature")
        SocketIoService.send_message("temperature", payload)

    elif topic == MQTTConfiguration.TOPIC_HUMIDITY:
        save_device(payload, 2)
        if int(payload) >=100 or int(payload) <= 0:
            notification(2)
        SocketIoService.send_message("humidity", payload)

    elif topic == MQTTConfiguration.TOPIC_LIGHT:
        save_device(payload, 3)
        SocketIoService.send_message("light", payload)

    elif topic == MQTTConfiguration.TOPIC_GAS:
        save_device(payload, 4)
        if int(payload) == 1:
            notification(4)
        SocketIoService.send_message("gas", payload)

    elif topic == MQTTConfiguration.TOPIC_FLASH_LIGHT:
        save_device(payload, 5)
        SocketIoService.send_message("flashLight", payload)


def save_device(value, device_id):
    try:
        device_status = DeviceStatus(device_id, value, datetime.now())
        with app.app_context():
            db.session.add(device_status)
            db.session.commit()
    except Exception as ex:
        print(ex)

def notification(device_id):
    try:
        requests.get("http://" + str(IP) + ":8888/mail/send/"+str(device_id)).json()
    except Exception as ex:
        logging.info("Request send mail error: {}".format(ex))
