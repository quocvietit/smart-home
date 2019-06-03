"""
==============================================================
   - Author: NoName
   - Version: 1.0
   - Since: 4/20/2019
   - Copy right @SmartHome
==============================================================
"""

import os
from . import *

class Config:
    def __init__(self, app):
        app.secret_key = os.urandom(SECRET_KEY_LENGTH)
