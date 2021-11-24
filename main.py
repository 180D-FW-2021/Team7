import os
import sys 
import webbrowser
from Pose_Determination.Pose_Basics import controlVolume
from MQTT.button_control import button_MQTT, zoom_in, zoom_out
def main():

    #button press to open this 
    filename = "Visualization/index.html"
    webbrowser.open('file://' + os.path.realpath(filename))

    #if voice command to turn up volume?
    controlVolume()
    
    #Zoom in/out buttons
    button_MQTT()
if __name__ == "__main__":
    main()
