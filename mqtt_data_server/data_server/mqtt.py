import paho.mqtt.client as mqtt
import json

# The callback for when the client receives a CONNACK response from the broker.
def on_connect(client, userdata, flags, rc):
    print("Connected with result code " + str(rc))
    client.subscribe("test")

def on_subscribe(client, userdata, mid, granted_qos):
    print("Subscribed: " + str(mid) + " "+str(granted_qos))

# The callback for when a PUBLISH message is received from the broker.
def on_message(client, userdata, msg):
    print("Message received")
    from .models import Data
    print(msg.topic + " " + str(msg.payload))
    message_dict = json.loads(msg.payload)

    if (message_dict.get("temperature") and message_dict.get("humidity")):
        data = Data(temperature=message_dict["temperature"], humidity=message_dict["humidity"])
        data.save()

#define Client
client = mqtt.Client(client_id="data_server")

#adding callbacks to client
client.on_connect = on_connect
client.on_subscribe = on_subscribe
client.on_message = on_message

# client.connect(host="192.168.0.11", port=1883)
print("hello django!")
