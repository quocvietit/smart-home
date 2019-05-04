"""
==============================================================
   - Author: NoName
   - Version: 1.0
   - Since: 4/20/2019
   - Copy right @SmartHome
==============================================================
"""
from flask_mail import Message

from extenstion.mail_core import mail

# Init message service
#msg = Message()


class MailService:

    def __init__(self):
        pass

    @staticmethod
    def send_mail(mail_address, message):
        msg = Message("Hello",
                      sender="smarthome.iuh2019@gmail.com",
                      recipients=["vuongquocviet1996@gmail.com"])
        mail.send(msg)
