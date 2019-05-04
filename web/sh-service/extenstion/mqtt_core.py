"""
==============================================================
   - Author: NoName
   - Version: 1.0
   - Since: 4/23/2019
   - Copy right @SmartHome
==============================================================
"""
import logging

from flask_mqtt import Mqtt, MQTT_LOG_ERR

from application import app, db

mqtt = Mqtt()

try:
    mqtt.init_app(app)
except Exception as ex:
    logging.error(f"Init MQTT Error: {ex}")


@mqtt.on_connect()
def handle_connect(client, userdata, flags, rc):
    pass


@mqtt.on_disconnect()
def handle_disconnect(client, userdata, flas, rc):
    pass

@mqtt.on_log()
def handle_logging(self, client, userdata, level, buf):
    if level == MQTT_LOG_ERR:
        logging.info('MQTT-Error: {}'.format(buf))
