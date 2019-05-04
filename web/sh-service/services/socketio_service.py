"""
==============================================================
   - Author: NoName
   - Version: 1.0
   - Since: 4/23/2019
   - Copy right @SmartHome
==============================================================
"""
from extenstion.socketio_core import socketio


class SocketIoService:
    def __init__(self):
        pass

    @staticmethod
    def send_message(topic, message):
        print("Send")
        try:
            socketio.emit(topic, message)
        except Exception as ex:
            print (ex)
