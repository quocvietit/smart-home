"""
==============================================================
   - Author: NoName
   - Version: 1.0
   - Since: 5/2/2019
   - Copy right @SmartHome
==============================================================
"""

from models.device_type import DeviceType


class DeviceTypeService:
    def __init__(self):
        pass

    @staticmethod
    def get_all():
        return DeviceType.get_all()
