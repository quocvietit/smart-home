from extenstion.app_core import *
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS

app = init_app()
db = SQLAlchemy()
db.init_app(app)
cors = CORS(app)

from extenstion.mqtt_handle import *

if __name__ == '__main__':
    init_log(os.path.realpath(__file__))
    register_bluesprint(app)
    register_topic()
    from extenstion.socketio_core import socketio
    #app.run(debug=True, host=os.getenv('IP', '0.0.0.0'), port=int(os.getenv('PORT', 80)))
    socketio.run(app, debug=True, host=os.getenv('IP', '0.0.0.0'), port=int(os.getenv('PORT', 8888)))
