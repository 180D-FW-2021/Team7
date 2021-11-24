import os
import sys 
import webbrowser
from Pose_Determination.Pose_Basics import controlVolume

def main():

    #button press to open this 
    filename = "Visualization/index.html"
    webbrowser.open('file://' + os.path.realpath(filename))

    #if voice command to turn up volume?
    controlVolume()

if __name__ == "__main__":
    main()