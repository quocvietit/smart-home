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
    logging.error('Init SocketIO Error: {}'.format( ex))


@socketio.on('connect')
def handle_connect():
    logging.info('Client connected: {}'.format(request.sid))


@socketio.on('disconnect')
def handle_disconnect():
    logging.info('Client disconnected: {}'.format(request.sid))
