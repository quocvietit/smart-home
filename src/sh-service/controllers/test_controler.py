"""
==============================================================
   - Author: NoName
   - Version: 1.0
   - Since: 5/2/2019
   - Copy right @SmartHome
==============================================================
"""

from flask import Blueprint, jsonify

from services.device_type_service import DeviceTypeService
from repositories.device_status_repository import DeviceStatusRepository
from extenstion.socketio_core import socketio

test = Blueprint(__name__, __name__, template_folder='templates')

@test.route('/test/socket')
def test_socket():
    socketio.emit("temperature", "test")
    return "DOne"

@test.route('/test/device_type')
def test_device_type():
    return jsonify(DeviceTypeService.get_all())


@test.route('/test/device_configuration')
def test_device_configuration():
    return jsonify(DeviceTypeService.get_all())


@test.route('/test/device')
def test_device():
    return jsonify(DeviceTypeService.get_all())


@test.route('/test/device_status')
def test_device_status():
    return jsonify(DeviceStatusRepository.get_by_device_topic("LIVINGROOM/TEMPERATURE"))
