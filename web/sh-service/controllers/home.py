"""
==============================================================
   - Author: NoName
   - Version: 1.0
   - Since: 3/29/2019
   - Copy right @SmartHome
==============================================================
"""

import logging
from flask import Blueprint, jsonify

from models.device_type import DeviceType


home = Blueprint(__name__, __name__, template_folder='templates')


@home.route('/')
@home.route('/index')
@home.route('/home')
def home_view():
    return "ok"

@home.route('/h')
def test():
    return DeviceType.get_all()

from services.mail_service import  MailService
@home.route('/unsub')
def unsub():
    MailService.send_mail("a","a")
    return "ok"
