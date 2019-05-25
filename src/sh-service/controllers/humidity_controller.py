"""
==============================================================
   - Author: NoName
   - Version: 1.0
   - Since: 5/9/2019
   - Copy right @SmartHome
==============================================================
"""

from flask import Blueprint, jsonify

from services.device_status_service import  DeviceStatusService

humidity = Blueprint(__name__, __name__, template_folder='templates')


@humidity.route('/temperature', methods=['GET'])
def get_temperature_current():
    data = {
        "data": [10, 20, 30, 40, 10, 30, 20, 8, 19, 10],
        "label": ["22:00:00", "22:00:05", "22:00:10", "22:00:15", "22:00:20", "22:00:25", "22:00:30", "22:00:00",
                  "22:00:00", "22:00:00"]
    }

    service = DeviceStatusService()
    temperature_data = service.get_data_for_chart(1)

    return jsonify(temperature_data[::-1])