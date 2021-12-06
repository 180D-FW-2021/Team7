MQTT Communication for Zoom In/Out Feature

Overview:
Using an MQTT connection, the raspberry pi communicates with the desktop when either the Zoom In or Zoom Out button is pressed on the remote.
When pressed the RPi sends a message to the laptop which then launches the Zoom command using CLIclick.

Bugs:
There is a significant lag between the time when the button is pressed to when the command is executed on the laptop display.
The MQTT connection cannot be made when the devices are connected to UCLA wifi, instead they must be connected to a personal hotspot.

Files:
1. PC_subscriber.py:
  - SETUP: Run on laptop with command "python3 PC_subscriber.py"
  - This is the subscriber script developed from Lab 3 that waits for a message from the publisher
  - Once the message is received, the corresponding CLIclick command is run to zoom in/out
  - CLIclick:
    - Emulate mouse and keyboard events such as cmd, + keys (which we use to Zoom in)
2. RPi_publisher.py:
  - Run from button_control.py
  - This is the publisher script developed from Lab 3
  - Once a button is pressed, this script is run to send the message to the client (laptop)
3. button_control.py:
  - SETUP: Run with "./button_control.py"
  - Waits for button press and runs publisher script accordingly
  - Uses GPIPOzero

Future Improvements:
Reducing latency in the MQTT communication by reworking the script calls.

Sources:
1. GPIOzero: 
https://gpiozero.readthedocs.io/en/stable/installing.html
https://pinout.xyz/pinout/io_pi_zero
https://www.youtube.com/watch?v=AlcF1_rs9e0
https://gpiozero.readthedocs.io/en/stable/recipes.html
2. CLIclick: 
https://github.com/BlueM/cliclick
3. MQTT:
https://bruinlearn.ucla.edu/courses/1647/files/5937309?wrap=1

