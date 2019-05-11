"""
==============================================================
   - Author: NoName
   - Version: 1.0
   - Since: 5/9/2019
   - Copy right @SmartHome
==============================================================
"""

from flask import Blueprint, jsonify

from services.device_status_service import DeviceStatusService

device_status_controller = Blueprint(__name__, __name__, template_folder='templates')


@device_status_controller.route('/device-status/<device_id>', methods=['GET'])
def get_data(device_id):
    service = DeviceStatusService()
    data = service.get_data(device_id)
    print(data)
    return jsonify(data)


@device_status_controller.route('/device-status/chart/<device_id>', methods=['GET'])
def get_data_chart(device_id):
    service = DeviceStatusService()
    data = service.get_data_for_chart(device_id)

    return jsonify(data[::-1])


@device_status_controller.route('/device-status/analytic/<time>', methods=['GET'])
def get_analytic(time):
    service = DeviceStatusService()
    data = service.get_data_for_analytic(time)
    print(type)
    return jsonify(data)
