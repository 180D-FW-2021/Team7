#!/usr/bin/python3
from gpiozero import Button
import os
def zoom_in():
	print("zoomIn_button was pressed. Running RPi_publisher.py")
	os.system("python3 RPi_publisher.py -i")

def zoom_out():
        print("zoomOut_button was pressed. Running RPi_publisher.py")
        os.system("python3 RPi_publisher.py -o")

def button_MQTT():
	zoomIn_button = Button(22) 
	zoomOut_button = Button(23)
	print("Waiting for buttons")
	#To Do: Add another button for Zoom out
	while True:
		#Could add an on/off signal perhaps with double click
	#print("Waiting for button")
		zoomIn_button.when_pressed = zoom_in
		zoomOut_button.when_pressed = zoom_out
		#print("zoomIn_button was pressed. Running RPi_publisher.py")
		#os.system("python3 publisherTest.py")
		#exec(open("RPi_publisher.py").read())
	print("Done.")

button_MQTT()
