"""
==============================================================
   - Author: NoName
   - Version: 1.0
   - Since: 5/2/2019
   - Copy right @SmartHome
==============================================================
"""

from . import DeviceStatus
from repositories.device_repository import DeviceRepository


class DeviceStatusRepository:

    @staticmethod
    def get_all():
        return DeviceStatus.query.all()

    @staticmethod
    def get_by_id(id):
        return DeviceStatus.query.get(id)

    @staticmethod
    def get_by_device_id(id):
        return DeviceStatus.query.filter_by(device_id=id).all()

    @staticmethod
    def get_by_device_topic(topic):
        device = DeviceRepository.get_by_mqtt_topic(topic)
        return DeviceStatusRepository.get_by_device_id(device.id)
