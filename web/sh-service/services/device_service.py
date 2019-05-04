"""
==============================================================
   - Author: NoName
   - Version: 1.0
   - Since: 4/23/2019
   - Copy right @SmartHome
==============================================================
"""

from models.device import Device


class DeviceService:
    def __init__(self):
        pass

    @staticmethod
    def get_all():
        return Device.get_all()
