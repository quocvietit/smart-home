from extenstion.app_core import *
from flask_sqlalchemy import SQLAlchemy
from flask_socketio import SocketIO

app = init_app()
db = SQLAlchemy()
db.init_app(app)

socketio = SocketIO()
socketio.init_app(app)


@socketio.on('connect')
def handle_connect():
    pass


@socketio.on('disconnect')
def handle_disconnect():
    pass


if __name__ == '__main__':
    init_log(os.path.realpath(__file__))
    register_bluesprint(app)
    register_topic()

    from extenstion.mqtt_handle import *

    app.run(debug=True, host=os.getenv('IP', '0.0.0.0'), port=int(os.getenv('PORT', 80)))
    # socketio.run(app)
