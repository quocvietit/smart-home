"""
==============================================================
   - Author: NoName
   - Version: 1.0
   - Since: 3/29/2019
   - Copy right @SmartHome
==============================================================
"""

import logging
from flask import Blueprint, render_template, jsonify

from utils.constants import *

from models.type_model import TypeModel
from models.device_model import DeviceModel

home = Blueprint(__name__, __name__, template_folder='templates')


@home.route('/')
@home.route('/index')
@home.route('/home')
def home_view():
    data = dict()
    try:
        logging.info("Get device")
        temperature_type = TypeModel.get_by_name(TEMPERATURE)
        temperature_device = DeviceModel.get_by_type(temperature_type.id)
        logging.info(temperature_device.id)

        light_type = TypeModel.get_by_name(LIGHT)
        light_device = DeviceModel.get_by_type(light_type.id)
        logging.info(light_device.id)

        gas_type = TypeModel.get_by_name(GAS)
        gas_device = DeviceModel.get_by_type(gas_type.id)
        logging.info(gas_device.id)

        data['value'] = "Can not load value!"

        if temperature_device.is_connect:
            data['temperature.is_connect'] = temperature_device.is_connect

        if temperature_device.is_enable:
            data['temperature.is_enable'] = temperature_device.is_enable

        data['temperature.last_activity'] = str(temperature_device.last_activity)[0:19]

        if light_device.is_connect:
            data['light.is_connect'] = light_device.is_connect

        if light_device.is_enable:
            data['light.is_enable'] = light_device.is_enable

        data['light.last_activity'] = str(light_device.last_activity)[0:19]

        if gas_device.is_connect:
            data['gas.is_connect'] = gas_device.is_connect

        if gas_device.is_enable:
            data['gas.is_enable'] = gas_device.is_enable

        data['gas.last_activity'] = str(gas_device.last_activity)[0:19]

        return render_template('home/index.html', data=data)
    except:
        pass

    return render_template('home/index.html', data=data)


@home.route('/tem')
def test():
    logging.info("get Date")
    data = TypeModel.get(1)
    print (data.name)
    if data:
        return jsonify(data.serialize())
    return  (jsonify([data.serialize() for data in TypeModel.query.all()]))
