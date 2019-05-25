"""
==============================================================
   - Author: NoName
   - Version: 1.0
   - Since: 4/20/2019
   - Copy right @SmartHome
==============================================================
"""

from . import *


class MQTTConfig:
    def __init__(self, app):
        app.config[MQTTParam.BROKER_URL] = MQTTConfiguration.SERVER
        app.config[MQTTParam.BROKER_PORT] = MQTTConfiguration.PORT
        app.config[MQTTParam.CLIENT_ID] = MQTTConfiguration.CLIENT_NAME
        app.config[MQTTParam.USERNAME] = MQTTConfiguration.USER_NAME
        app.config[MQTTParam.PASSWORD] = MQTTConfiguration.PASSWORD
        app.config[MQTTParam.KEEP_ALIVE] = MQTTConfiguration.KEEP_ALIVE
        app.config[MQTTParam.TLS_ENABLED] = MQTTConfiguration.TLS_ENABLED
