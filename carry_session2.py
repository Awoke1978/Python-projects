import paho.mqtt.client as mqtt
import time

broker_address = "localhost"
port = 1883
topic = "sensor_data"
client = mqtt.Client()
client.connect(broker_address, port)

while True:
    message = "Hello"
    client.publish(topic, message)
    print("Published message:", message)
    time.sleep(1)


import paho.mqtt.client as mqtt
import time

broker_address = "localhost"
port = 1883
topic = "sensor_data"
client = mqtt.Client()
client.connect(broker_address, port)

while True:
    message = "Hello"
    client.publish(topic, message)
    print("Published message:", message)
    time.sleep(1)