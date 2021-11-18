#!/usr/bin/python3
from gpiozero import Button
import os

button = Button(22)
while True:
	print("Waiting for button")
	button.wait_for_press()
	print("Button was pressed. Running publisher.py")
	#os.system("python3 publisherTest.py")
	exec(open("publisherTest.py").read())
	print("Done.")
