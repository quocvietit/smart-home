"""
==============================================================
   - Author: NoName
   - Version: 1.0
   - Since: 5/11/2019
   - Copy right @SmartHome
==============================================================
"""
from flask import Blueprint, jsonify
from services.mail_service import MailService

mail_controller = Blueprint(__name__, __name__, template_folder='templates')


@mail_controller.route('/mail/send/<device_id>')
def send(device_id):
    message = "Anomaly detection: {}"
    if int(device_id) == 4:
        message = message.format("GAS")

    MailService.send_mail(message)
    return "ok"
