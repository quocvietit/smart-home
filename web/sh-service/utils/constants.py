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
    LOGGING_FOLDER_FORMAT = '{}\\logs'
    LOGGING_CONTENT_FORMAT = "%(asctime)s [%(threadName)s] [%(levelname)s] - %(message)s"
    LOGGING_DATE_FORMAT = "%d/%m/%Y %I:%M:%S %p"
    LOGGING_FILE_NAME_FORMAT = "{}\\log-{}.txt"





SECRET_KEY_LENGTH = 12

# Device
TEMPERATURE = 'TEMPERATURE'
LIGHT = 'LIGHT'
GAS = 'GAS'
FLASH_LIGHT = 'FLASH_LIGHT'

