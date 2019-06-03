"""
==============================================================
   - Author: NoName
   - Version: 1.0
   - Since: 3/30/2019
   - Copy right @SmartHome
==============================================================
"""

from flask import Blueprint, jsonify

from services.device_status_service import  DeviceStatusService

temperature = Blueprint(__name__, __name__, template_folder='templates')


@temperature.route('/temperature', methods=['GET'])
def get_temperature_current():
    service = DeviceStatusService()
    temperature_data = service.get_data_for_chart(1)

    return jsonify(temperature_data[::-1])
