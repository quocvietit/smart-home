"""
==============================================================
   - Author: NoName
   - Version: 1.0
   - Since: 3/30/2019
   - Copy right @SmartHome
==============================================================
"""

import logging
import datetime
from flask import Blueprint, render_template, jsonify

from utils.constants import *
from models.type_model import TypeModel
from models.device_model import DeviceModel
from models.history_model import HistoryModel

temperature = Blueprint(__name__, __name__, template_folder='templates')

@temperature.route('/info')
def get_info():
    temperature_type = TypeModel.get_by_name(TEMPERATURE)
    device = DeviceModel.get_by_type(temperature_type.id)
    historyModel = HistoryModel("abc", datetime.datetime.now(), 1)
    historyModel.save()
    return jsonify(device.serialize())
    return "ok"
@staticmethod
def save_history(value, id):
    historyModel = HistoryModel(value, datetime.datetime.now(), id)
    historyModel.save()



