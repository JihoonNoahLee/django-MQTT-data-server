import paho.mqtt.client as mqtt
from threading import Thread
import json

class MqttThread(Thread):
    def __init__(self, broker_ip, broker_port, timeout, topics):
        super(MqttThread, self).__init__()
        self.client = mqtt.Client(client_id="data_server")
        self.broker_ip = broker_ip
        self.broker_port = broker_port
        self.timeout = timeout
        self.topics = topics

    # run method override from Thread class
    def run(self):
        self.connect_to_broker()

    def connect_to_broker(self):
        self.client.on_connect = self.on_connect
        self.client.on_subscribe = self.on_subscribe
        self.client.on_message = self.on_message
        while True:
            try:
                self.client.connect(self.broker_ip, self.broker_port, self.timeout)
                self.client.loop_forever()
            except Exception as e:
                print("Connection to broker failed: " + str(e))
                continue

    def on_connect(self, client, userdata, flags, rc):
        print("Connected with result code " + str(rc))
        for topic in self.topics:
            client.subscribe(topic)

    def on_subscribe(self, client, userdata, mid, granted_qos):
        print("Subscribed: " + str(mid) + " "+str(granted_qos))

    def on_message(self, client, userdata, msg):
        print("Message received")
        from .models import Data
        print(msg.topic + " " + str(msg.payload))
        message_dict = json.loads(msg.payload)

        if (message_dict.get("temperature") and message_dict.get("humidity")):
            data = Data(temperature=message_dict["temperature"], humidity=message_dict["humidity"])
            data.save()
