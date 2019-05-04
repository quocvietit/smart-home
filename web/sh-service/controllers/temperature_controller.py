"""
==============================================================
   - Author: NoName
   - Version: 1.0
   - Since: 3/30/2019
   - Copy right @SmartHome
==============================================================
"""

from flask import Blueprint


temperature = Blueprint(__name__, 'temperature', template_folder='templates')

@temperature.route('/current')
def get_temperature_current():
    pass




