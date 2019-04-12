"""
==============================================================
   - Author: NoName
   - Version: 1.0
   - Since: 3/29/2019
   - Copy right @SmartHome
==============================================================
"""
import os

class MQTTConfig:
    CLIENT_NAME = "Raspberry-Server-1"
    SERVER = 'localhost'
    PORT = 1883
    USER_NAME = 'pi'
    PASSWORD = '123'
    KEEP_ALIVE = 60
    TLS_ENABLED = False
    TOPIC_TEMPERATURE = "home/room/temperature"
    TOPIC_HUMIDITY = "home/room/humidity"
    TOPIC_LIGHT = "home/room/light"
    TOPIC_GAS = "home/room/gas"
    TOPIC_FLASH_LIGHT = "home/room/flash_light"

class DatabaseConfig:
    USER_NAME = 'postgres'
    PASSWORD = 'admin'
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



