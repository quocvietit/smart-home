"""
==============================================================
   - Author: NoName
   - Version: 1.0
   - Since: 4/23/2019
   - Copy right @SmartHome
==============================================================
"""
import logging

from services.device_service import DeviceService
from services.mqtt_service import MQTTService


class UtilService:
    def __init__(self):
        pass

    @staticmethod
    def init_subscribe_topic():
        devices = DeviceService.get_all()
        for device in devices:
            if device.is_enable and not device.is_control:
                try:
                    MQTTService.subscribe(device.mqtt_topic)
                except Exception as ex:
                    logging.error('Subscribed error: {}'.format(ex))
