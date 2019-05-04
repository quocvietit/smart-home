"""
==============================================================
   - Author: NoName
   - Version: 1.0
   - Since: 4/27/2019
   - Copy right @SmartHome
==============================================================
"""

from flask_mail import Mail

from application import app

mail = Mail(app)
