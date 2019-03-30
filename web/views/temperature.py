"""
==============================================================
   - Author: NoName
   - Version: 1.0
   - Since: 3/30/2019
   - Copy right @SmartHome
==============================================================
"""

import logging
from flask import Blueprint, render_template, jsonify

from utils.constants import *
from models.type_model import TypeModel
from models.device_model import DeviceModel

temperature = Blueprint(__name__, __name__, template_folder='templates')

@temperature.route('/info')
def get_info():
    temperature_type = TypeModel.get_by_name(TEMPERATURE)
    device = DeviceModel.get_by_type(temperature_type.id)
    return jsonify(device.serialize())
    return "ok"



