"""
==============================================================
   - Author: NoName
   - Version: 1.0
   - Since: 5/11/2019
   - Copy right @SmartHome
==============================================================
"""

import socket


class ip:

    def __init__(self):
        self.__ip = socket.gethostbyname(socket.gethostname())

    def getIP(self):
        return 'localhost'
        #return self.__ip

    def toString(self):
        return "IP: {}".format(self.getIP())
