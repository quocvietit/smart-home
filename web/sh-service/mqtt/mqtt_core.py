"""
==============================================================
   - Author: NoName
   - Version: 1.0
   - Since: 4/6/2019
   - Copy right @SmartHome
==============================================================
"""
import paho.mqtt.client as mqtt
import datetime
import threading as th
import time


def on_message_temperature(self, client, userdata, message):
    value = message.payload.decode()
    device_id = 1
    save_device(value, device_id)


def on_message_humidity(self, client, userdata, message):
    value = message.payload.decode()
    device_id = 5
    save_device(value, device_id)


def on_message_light(client, userdata, message):
    print("AHihi")
    value = message.payload.decode()
    device_id = 2
    save_device(value, device_id)


def on_message_gas(client, userdata, message):
    value = message.payload.decode()
    device_id = 3
    save_device(value, device_id)


def on_message_flash_light(client, userdata, message):
    value = message.payload.decode()
    device_id = 4
    save_device(value, device_id)


def save_device(value, device_id):
    time = datetime.datetime.now()
    print (time)
    #record = HistoryModel(value, time, device_id)
    #record.save()
myGlobalMessagePayload = '' 
def on_message(client, userdata, msg):
    global myGlobalMessagePayload
    if msg.topic == 'home/room/light':
        myGlobalMessagePayload  = msg.payload   #HERE!
        print(msg.topic+" "+str(msg.payload))


#user_name = MQTT.USER_NAME_DEFAULT
#server_address = MQTT.SERVER_ADDRESS_DEFAULT
#port = MQTT.PORT_DEFAULT
client = mqtt.Client()
client.on_message = on_message
client.username_pw_set("pi", "123")
#client.message_callback_add(MQTT.TOPIC_TEMPERATURE, on_message_temperature)
#client.message_callback_add(MQTT.TOPIC_HUMIDITY, on_message_humidity)
#client.message_callback_add("home/room/light", on_message_light)
#client.message_callback_add(MQTT.TOPIC_GAS, on_message_gas)
#client.message_callback_add(MQTT.TOPIC_FLASH_LIGHT, on_message_flash_light)
client.connect('192.168.43.221', 1883)
client.loop_start()

#client.subscribe(MQTT.TOPIC_TEMPERATURE)
#client.subscribe(MQTT.TOPIC_HUMIDITY)
client.subscribe("home/room/light")
#client.subscribe(MQTT.TOPIC_GAS)
#client.subscribe(MQTT.TOPIC_FLASH_LIGHT)



def start(self):
    thread = th.Thread(target=self.update, args=())
    thread.start()


def update(self):
    pass

