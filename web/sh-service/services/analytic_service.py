"""
==============================================================
   - Author: NoName
   - Version: 1.0
   - Since: 5/11/2019
   - Copy right @SmartHome
==============================================================
"""

import statistics
from decimal import Decimal as D

class AnalyticService:
    def __init__(self):
        pass

    @staticmethod
    def analytic(data):
        res = [
            statistics.mean(data),
            min(data),
            max(data),
            statistics.mode(data)
        ]
        print (res)

        return res

    @staticmethod
    def analytic_2(data):
        res = [
            sum(data),
            sum(data)/len(data)
        ]

        return res
