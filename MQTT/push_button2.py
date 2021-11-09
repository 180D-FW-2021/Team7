from gpiozero import Button
import os

button = Button(22)
print("Waiting for button")
button.wait_for_press()
print("Button was pressed. Running publisher.py")
os.system("sudo python3 ./publisherTest.py")
print("Done.")
