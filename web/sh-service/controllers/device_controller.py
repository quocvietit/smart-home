"""
==============================================================
   - Author: NoName
   - Version: 1.0
   - Since: 5/9/2019
   - Copy right @SmartHome
==============================================================
"""

from flask import Blueprint
from extenstion.mqtt_core import mqtt
from setting import MQTTConfiguration

device_controller = Blueprint(__name__, __name__, template_folder='templates')


@device_controller.route('/device/flash-light/control/on', methods=['GET'])
def turn_on_light():
    mqtt.publish(MQTTConfiguration.TOPIC_FLASH_LIGHT_CONTROL, "1")
    return "Ok"


@device_controller.route('/device/flash-light/control/off', methods=['GET'])
def turn_off_light():
    mqtt.publish(MQTTConfiguration.TOPIC_FLASH_LIGHT_CONTROL, "0")
    return "Ok"


