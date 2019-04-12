"""
==============================================================
   - Author: NoName
   - Version: 1.0
   - Since: 3/30/2019
   - Copy right @SmartHome
==============================================================
"""

import datetime

from models.history_model import HistoryModel

class HistoryService:
    def __init__(self):
        pass

    @staticmethod
    def save(value, id):
        history_model = HistoryModel(value, datetime.datetime.now(), id)
        history_model.save()