"""
==============================================================
   - Author: NoName
   - Version: 1.0
   - Since: 5/2/2019
   - Copy right @SmartHome
==============================================================
"""

from . import Device


class DeviceRepository:
    @staticmethod
    def get_all():
        return Device.query.all()

    @staticmethod
    def get_by_id(id):
        return Device.query.get(id)

    @staticmethod
    def get_by_mqtt_topic(topic):
        return Device.query.filter_by(mqtt_topic=topic).first()

    @staticmethod
    def get_by_type_id_and_location_id(type_id, location_id):
        return Device.query.filter_by(type_id=type_id, location_id=location_id).first()
