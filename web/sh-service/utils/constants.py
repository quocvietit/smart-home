"""
==============================================================
   - Author: NoName
   - Version: 1.0
   - Since: 3/29/2019
   - Copy right @SmartHome
==============================================================
"""


class Logger:
    # Language
    LANGUAGE = "english"

    # Setup logging
    LOGGING_FOLDER_FORMAT = '{}/logs'
    LOGGING_CONTENT_FORMAT = "%(asctime)s [%(threadName)s] [%(levelname)s] - %(message)s"
    LOGGING_DATE_FORMAT = "%d/%m/%Y %I:%M:%S %p"
    LOGGING_FILE_NAME_FORMAT = "{}/log-{}.txt"


class MQTTParam:
    BROKER_URL = 'MQTT_BROKER_URL'
    BROKER_PORT = 'MQTT_BROKER_PORT'
    CLIENT_ID = 'MQTT_CLIENT_ID'
    USERNAME = 'MQTT_USERNAME'
    PASSWORD = 'MQTT_PASSWORD'
    KEEP_ALIVE = 'MQTT_KEEPALIVE'
    TLS_ENABLED = 'MQTT_TLS_ENABLED'


class SQLParams:
    DATABASE_URI = 'SQLALCHEMY_DATABASE_URI'
    TRACK_MODIFICATION = 'SQLALCHEMY_TRACK_MODIFICATIONS'
    ECHO = 'SQLALCHEMY_ECHO'


class MailParams:
    SERVER = "MAIL_SERVER"
    PORT = "MAIL_PORT"
    USE_SSL = "MAIL_USE_SSL"
    USERNAME = "MAIL_USERNAME"
    PASSWORD = "MAIL_PASSWORD"


class TableName:
    DEVICE = 'device'
    DEVICE_STATUS = 'device_status'
    DEVICE_TYPE = 'device_type'
    DEVICE_CONFIGURATION = 'device_configuration'
    DEVICE_LOCATION = 'device_location'
    CONFIGURATION = 'configuration'


SECRET_KEY_LENGTH = 12

# Device
TEMPERATURE = 'TEMPERATURE'
LIGHT = 'LIGHT'
GAS = 'GAS'
FLASH_LIGHT = 'FLASH_LIGHT'
