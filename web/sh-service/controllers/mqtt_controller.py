"""
==============================================================
   - Author: NoName
   - Version: 1.0
   - Since: 4/18/2019
   - Copy right @SmartHome
==============================================================
"""

from flask import Blueprint, jsonify, request

from services.mqtt_service import MQTTService

mqtt_controller = home = Blueprint(__name__, "mqtt", template_folder='templates')


@mqtt_controller.route('/subscribe', methods=['POST'])
def subscribe_topic():
    topic = str(request.data.get('topic', ''))
    MQTTService.subscribe(topic)
    return "OK"


@mqtt_controller.route('/unsubscribe', methods=['POST'])
def unsubscribe_topic():
    topic = str(request.data.get('topic', ''))
    MQTTService.unsubscribe(topic)
    return "OK"
