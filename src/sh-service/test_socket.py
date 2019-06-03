"""
==============================================================
   - Author: NoName
   - Version: 1.0
   - Since: 5/4/2019
   - Copy right @SmartHome
==============================================================
"""
import os
import random
from flask_socketio import SocketIO
from flask import Flask
import time

app = Flask(__name__)
socketio = SocketIO(app)

if __name__ == '__main__':
    app.run(debug=True, host=os.getenv('IP', '0.0.0.0'), port=int(os.getenv('PORT', 80)))
    #socketio.run(app)
    while True:
        value = random.randrange(-20, 50)
        print("Send ", value)
        socketio.emit('temperature', value)
        socketio.emit('humidity', value-5)
        socketio.emit('light', random.randrange(0, 2))
        socketio.emit('gas', random.randrange(0, 2))
        socketio.emit('flashLight', random.randrange(0, 2))
        time.sleep(5)
