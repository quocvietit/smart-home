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

from extenstion.mqtt_core import mqtt
from models.device import Device
from repositories.device_repository import DeviceRepository
from models.device_status import DeviceStatus
from services.socketio_service import SocketIoService


class MQTTService:
    def __init__(self):
        pass

    @staticmethod
    def subscribe(topic):
        try:
            mqtt.subscribe(topic)
        except Exception as ex:
            logging.error("Subscribe Error: {}".format(ex))

    @staticmethod
    def unsubscribe(topic):
        try:
            mqtt.unsubscribe(topic)
        except Exception as ex:
            logging.error("Unsubscribe Error: {}".format(ex))

    @staticmethod
    def handle_data_topic(topic, value):
        print("co")
        try:
            device = Device.get_by_id(1)
        except Exception as ex:
            print("Ex: ", ex)
        print("value: ", device.mqtt_topic)
        if device and device.is_enable and not device.is_control:
            time = datetime.now()
            data = {
                'is_connect': True,
                'is_enable': time
            }
            device.update(data)
            device_status = DeviceStatus(device.id, value, time)
            device_status.save()

            if device.socket_topic:
                SocketIoService.send_message(device.socket_topic, value)
