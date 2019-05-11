"""
==============================================================
   - Author: NoName
   - Version: 1.0
   - Since: 5/2/2019
   - Copy right @SmartHome
==============================================================
"""

from datetime import datetime, timedelta
from decimal import Decimal as D
import json

from models.device_status import DeviceStatus
from services.analytic_service import AnalyticService


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

    def get_data_for_analytic(self, hour):
        now = datetime.now()
        hours_ago = now - timedelta(hours=int(hour))

        record = DeviceStatus.query.filter(DeviceStatus.time > hours_ago).filter(DeviceStatus.time < now).order_by(
            DeviceStatus.time.desc()).all()

        temperature_data = self.filter_data(record, 1)
        temperature_res = AnalyticService.analytic(temperature_data)
        temperature = {
            "mean": str(temperature_res[0]),
            "min": str(temperature_res[1]),
            "max": str(temperature_res[2]),
            "mode": str(temperature_res[3])
        }

        humidity_data = self.filter_data(record, 2)
        humidity_res = AnalyticService.analytic(humidity_data)
        humidity = {
            "mean": str(humidity_res[0])[:-4],
            "min": str(humidity_res[1]),
            "max": str(humidity_res[2]),
            "mode": str(humidity_res[3])
        }

        light_data = self.filter_data(record, 3)
        light_res = AnalyticService.analytic_2(light_data)
        light = {
            "count": str(light_res[0]),
            "persent": str(light_res[1])
        }

        gas_data = self.filter_data(record, 4)
        gas_res = AnalyticService.analytic_2(gas_data)
        gas = {
            "count": str(gas_res[0]),
            "persent": str(gas_res[1])
        }

        flash_light_data = self.filter_data(record, 5)
        flash_light = {
            "count": self.count_flash_light(flash_light_data)
        }

        data = {
            "temperature": temperature,
            "humidity": humidity,
            "light": light,
            "gas": gas,
            "flash_light": flash_light
            #"data": DeviceStatus.serialize_list(record)
        }

        return data

    def filter_data(self, record, device_id):
        data = []
        for i in record:
            if i.device_id == device_id:
                data.append(D(i.value))
        return data

    def count_flash_light(self, data):
        count = 0

        if int(data[0]) == 1:
            count = 1

        for i in range(1, len(data)):
            if int(data[i]) != int(data[i-1]):
                count+=1

        return count
