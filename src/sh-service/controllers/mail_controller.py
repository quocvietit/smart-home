"""
==============================================================
   - Author: NoName
   - Version: 1.0
   - Since: 5/11/2019
   - Copy right @SmartHome
==============================================================
"""
from datetime import datetime
from flask import Blueprint, jsonify
from services.mail_service import MailService

mail_controller = Blueprint(__name__, __name__, template_folder='templates')


@mail_controller.route('/mail/send/<device_id>')
def send(device_id):
    time_detection = datetime.now().strftime("%Y-%m-%d %H:%M")
    message = "Anomaly detection: {} \n Time detection: " + str(time_detection)
    if int(device_id) == 1:
        message = message.format("Temperature")

    elif int(device_id) == 2:
        message = message.format("Humidity")

    elif int(device_id) == 4:
        message = message.format("GAS")

    MailService.send_mail(message)
    return "ok"
