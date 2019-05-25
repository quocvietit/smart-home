"""
==============================================================
   - Author: NoName
   - Version: 1.0
   - Since: 4/20/2019
   - Copy right @SmartHome
==============================================================
"""
import logging
from flask_mail import Message
from datetime import datetime

from extenstion.mail_core import mail

# Init message service
#msg = Message()

MESSAGE_GAS = "SMART HOME - Warning "

class MailService:

    def __init__(self):
        pass

    @staticmethod
    def send_mail(message):
        print("send mail")
        time_detection = str(datetime.now().strftime("%Y-%m-%d %H:%M"))
        message = message + time_detection
        date_detection = str(datetime.now().strftime("%Y-%m-%d"))
        title = MESSAGE_GAS + date_detection
        try:
            msg = Message(body=message,
                          subject=title,
                          sender="smarthome.iuh2019@gmail.com",
                          recipients=["vuongquocviet1996@gmail.com"])
            mail.send(msg)
        except Exception as ex:
            logging.info("Send mail error: {}".format(ex))


