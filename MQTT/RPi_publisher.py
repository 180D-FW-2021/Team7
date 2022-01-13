#!/usr/bin/python3
from gpiozero import Button
import paho.mqtt.client as mqtt
import argparse
import os

parser = argparse.ArgumentParser()
parser.add_argument("-i", "--ZoomIn", help="Zoom In", action="store_true")
parser.add_argument("-o", "--ZoomOut", help="Zoom Out", action="store_true")
args = parser.parse_args()

if (not args.ZoomIn) and (not args.ZoomOut):
  print("Zooming direction not specified")
  exit()

# 0. define callbacks - functions that run when events happen.
# The callback for when the client receives a CONNACK response from the server.
def on_connect(client, userdata, flags, rc):
  print("Connection returned result: "+str(rc))
  # Subscribing in on_connect() means that if we lose the connection and
  # reconnect then subscriptions will be renewed.
  # client.subscribe("ece180d/test")

# The callback of the client when it disconnects.
def on_disconnect(client, userdata, rc):
  if rc != 0:
    print('Unexpected Disconnect')
  else:
    print('Expected Disconnect')

# The default message callback.
# (won’t be used if only publishing, but can still exist)
def on_message(client, userdata, message):
  print('Received message: ' + str(message.payload) + ' on topic ' + message.topic + ' with QoS ' + str(message.qos))

#To Do add arguments to input:

# 1. create a client instance.
client = mqtt.Client()
# add additional client options (security, certifications, etc.)
# many default options should be good to start off.
# add callbacks to client.
client.on_connect = on_connect
client.on_disconnect = on_disconnect
client.on_message = on_message

# 2. connect to a broker using one of the connect*() functions.
#client.connect_async('mqtt.eclipseprojects.io')
#client.connect_async("mqtt.eclipse.org")
client.connect_async("test.mosquitto.org")

# 3. call one of the loop*() functions to maintain network traffic flow with the broker.
client.loop_start()

#------BUTTON PRESS----------
def zoom_in_publish():
  print("zoomIn button pressed. Publishing now.")
  client.publish('ece180d/team7', "Run CLIclick Zoom In", qos=1)

def zoom_out_publish():
  print("zoomOut button pressed. Publishing now.")
  client.publish('ece180d/team7', "Run CLIclick Zoom Out", qos=1)

zoomIn_button = Button(22)
zoomOut_button = Button(23)
print("Waiting for buttons")

try:
  while True:
    zoomIn_button.when_pressed = zoom_in_publish
    zoomOut_button.when_pressed = zoom_out_publish

# 4. use subscribe() to subscribe to a topic and receive messages.
# 5. use publish() to publish messages to the broker.
# payload must be a string, bytearray, int, float or None.

#if args.ZoomIn:
#  print("Publishing Zoom In")
#  client.publish('ece180d/team7', "Run CLIclick Zoom In", qos=1)
#elif args.ZoomOut:
#  print("Publishing Zoom Out")
#  client.publish('ece180d/team7', "Run CLIclick Zoom Out", qos=1)

# 6. use disconnect() to disconnect from the broker.
except KeyboardInterrupt:
  client.loop_stop()
  client.disconnect()
