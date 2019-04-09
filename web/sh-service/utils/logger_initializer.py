"""
==============================================================
   - Author: NoName
   - Version: 1.0
   - Since: 3/29/2019
   - Copy right @SmartHome
==============================================================
"""

import logging
import os.path
import datetime as dt

from utils import constants


def initialize_logger(dir_path):
    version = get_date_version()
    logging_file_path = constants.Logger.LOGGING_FOLDER_FORMAT.format(dir_path)
    log_file = constants.Logger.LOGGING_FILE_NAME_FORMAT.format(logging_file_path, version)

    # Check folder exits
    if not os.path.exists(logging_file_path):
        os.makedirs(logging_file_path)

    # Check file exits
    if not os.path.isfile(log_file):
        with open(log_file, "w+") as file:
            file.write(version + "\n")
            file.close()

    logger = logging.getLogger()
    logger.setLevel(logging.DEBUG)

    log_format = constants.Logger.LOGGING_CONTENT_FORMAT
    date_format = constants.Logger.LOGGING_DATE_FORMAT

    logger.addHandler(handler_log_console(log_format, date_format))
    logger.addHandler(handler_log_file(log_format, log_file))


def handler_log_console(log_format, date_format):
    formatter = logging.Formatter(log_format, date_format)

    handler = logging.StreamHandler()

    handler.setLevel(logging.INFO)
    handler.setFormatter(formatter)

    return handler


def handler_log_file(log_format, file):
    formatter = logging.Formatter(log_format)

    handler = logging.FileHandler(file, "a")

    handler.setLevel(logging.DEBUG)
    handler.setFormatter(formatter)

    return handler


def get_date_version():
    # Get date
    date = dt.datetime.now()

    # Mapping date to date format
    day = "{}{}".format(date.day // 10, date.day % 10)
    month = "{}{}".format(date.month // 10, date.month % 10)
    year = str(date.year)

    return "-".join([day, month, year])
