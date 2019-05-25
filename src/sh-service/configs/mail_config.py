"""
==============================================================
   - Author: NoName
   - Version: 1.0
   - Since: 4/27/2019
   - Copy right @SmartHome
==============================================================
"""
from . import *


class MailConfig:
    def __init__(self, app):
        app.config[MailParams.SERVER] = "smtp.gmail.com"
        app.config[MailParams.PORT] = 465
        app.config[MailParams.USE_SSL] = True
        app.config[MailParams.USERNAME] = 'smarthome.iuh2019@gmail.com'
        app.config[MailParams.PASSWORD] = 'Smarthome@2019'
