"""
==============================================================
   - Author: NoName
   - Version: 1.0
   - Since: 5/2/2019
   - Copy right @SmartHome
==============================================================
"""
from models.device_status import DeviceStatus


class DeviceStatusService:
    def __int__(self):
        pass

    def get_data(self, device_id):
        record = DeviceStatus.query.filter_by(device_id=device_id).order_by(DeviceStatus.time.desc()).first()

        if record is None:
            return {}
        return record.serialize()

    def get_data_for_chart(self, device_id):
        record = DeviceStatus.query.filter_by(device_id=device_id).order_by(DeviceStatus.time.desc()).limit(10).all()

        if record is None:
            return {}
        return DeviceStatus.serialize_list(record)

