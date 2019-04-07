"""
==============================================================
   - Author: NoName
   - Version: 1.0
   - Since: 3/29/2019
   - Copy right @SmartHome
==============================================================
"""
import os

class MQTT:
    USER_NAME_DEFAULT = "Raspberry-Server-1"
    SERVER_ADDRESS_DEFAULT = '192.168.43.221' #os.getenv("IP")
    PORT_DEFAULT = 1883 #os.getenv("PORT")
    TOPIC_TEMPERATURE = "home/room/temperature"
    TOPIC_HUMIDITY = "home/room/humidity"
    TOPIC_LIGHT = "home/room/light"
    TOPIC_GAS = "home/room/gas"
    TOPIC_FLASH_LIGHT = "home/room/flash_light"



