"""
==============================================================
   - Author: NoName
   - Version: 1.0
   - Since: 3/29/2019
   - Copy right @SmartHome
==============================================================
"""

from . import *


class DatabaseConfig:
    def __init__(self, app):
        app.config[SQLParams.DATABASE_URI] = DatabaseConfiguration.URI
        app.config[SQLParams.TRACK_MODIFICATION] = DatabaseConfiguration.TRACK_MODIFICATION
        app.config[SQLParams.ECHO] = DatabaseConfiguration.ECHO
