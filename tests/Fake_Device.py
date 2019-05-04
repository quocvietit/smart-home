import time
import random

from flask import Flask
from flask_mqtt import Mqtt

app = Flask(__name__)

app.config['MQTT_BROKER_URL'] = 'localhost'
app.config['MQTT_BROKER_PORT'] = 1883
app.config['MQTT_CLIENT_ID'] = 'Raspberry-Server'
app.config['MQTT_USERNAME'] = 'pi'
app.config['MQTT_PASSWORD'] = '123'
app.config['MQTT_KEEPALIVE'] = 60
app.config['MQTT_TLS_ENABLED'] = False

mqtt = Mqtt(app)

topics = {
    "TEMPERATURE_HOME"
}
def pub():
    while True:
        for topic in topics:
            print(topic)
            mqtt.publish(topic, random.randrange(-20, 50))
        time.sleep(1)

if __name__ == '__main__':
    app.run(debug=True, host='localhost', port=8081)
    pub()
