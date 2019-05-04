"""
==============================================================
   - Author: NoName
   - Version: 1.0
   - Since: 3/29/2019
   - Copy right @SmartHome
==============================================================
"""


class MQTTConfiguration:
    CLIENT_NAME = "Raspberry-Server-1"
    SERVER = 'localhost'
    PORT = 1883
    USER_NAME = 'pi'
    PASSWORD = '123'
    KEEP_ALIVE = 60
    TLS_ENABLED = False
    TOPIC_TEMPERATURE = "LIVINGROOM/TEMPERATURE"
    TOPIC_HUMIDITY = "LIVINGROOM/HUMIDITY"
    TOPIC_LIGHT = "LIVINGROOM/LIGHT"
    TOPIC_GAS = "LIVINGROOM/GAS"
    TOPIC_FLASH_LIGHT = "LIVINGROOM/FLASH_LIGHT"


class DatabaseConfiguration:
    USER_NAME = 'postgres'
    PASSWORD = 'smarthome@2019'
    NAME = 'smarthome'
    HOST = 'localhost'
    PORT = 5432
    POSTGRES = {
        'user': USER_NAME,
        'pw': PASSWORD,
        'db': NAME,
        'host': HOST,
        'port': PORT,
    }
    URI = 'postgresql://%(user)s:%(pw)s@%(host)s:%(port)s/%(db)s' % POSTGRES
    TRACK_MODIFICATION = False
    ECHO = False
