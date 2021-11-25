#!/usr/bin/python3
import os
import sys 
import webbrowser
from multiprocessing import Process
from Pose_Determination.Pose_Basics import controlVolume
from MQTT.button_control import button_MQTT, zoom_in, zoom_out

#Function below used to test parallel function behavior
def parallel_test():
    for i in range(100):
        if i is 75:
            print("75")

def main():

    #button press to open this 
    filename = "Visualization/index.html"
    webbrowser.open('file://' + os.path.realpath(filename))

    #if voice command to turn up volume?
    controlVolume()
    
    #Zoom in/out buttons
    #This is the general format for calling all our functions at the same time
    p1 = Process(target=button_MQTT)
    p1.start()
    p2 = Process(target=parallel_test)
    p2.start()
    p1.join()
    p2.join()

if __name__ == "__main__":
    main()
