"""
==============================================================
   - Author: NoName
   - Version: 1.0
   - Since: 4/23/2019
   - Copy right @SmartHome
==============================================================
"""

import logging

from flask_socketio import SocketIO
from flask import request

from application import app

socketio = SocketIO()

try:
    socketio.init_app(app)
except Exception as ex:
    logging.error(f"Init SocketIO Error: {ex}")


@socketio.on('connect')
def handle_connect():
    logging.info(f'Client connected: {request.sid}')


@socketio.on('disconnect')
def handle_disconnect():
    logging.info(f'Client disconnected: {request.sid}')
