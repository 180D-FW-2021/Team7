GETTING STARTED:

The purpose of this code is to complete pose recognition for the Mr. Remote system. The pose recognition system controls the volume on your computer with detecting the thumbs up and down pose, and the stop pose to stop volume control. 

Prerequisites:
- OpenCV - library of programming functions mainly aimed at real-time computer vision
   - In a virtual environment (instructions here: https://docs.conda.io/projects/conda/en/latest/user-guide/tasks/manage-environments.html)
   - Run 'pip install opencv-python' for the built-in python extensions
   - Download instructions can be found here: https://pypi.org/project/opencv-python/ 
- MediaPipe (https://google.github.io/mediapipe/) 
  - This script runs using MediaPipe, which is machine-learning based solution for pose recognition and tracking
  - Install where OpenCV is installed (in virtual environment for example)
  - run 'pip install mediapipe'
  - Note: in Mac (which is where system is compatible) MacOS version must be 10.15 or higher
  - Other installation instructions and trouble shooting can be found here: https://google.github.io/mediapipe/getting_started/install.html#installing-on-macos
- CliClick 
   - Source code: https://github.com/BlueM/cliclick
   - Download package from the following: https://www.bluem.net/en 
   - Move download folder to usr/local/bin folder on personal computer


CODE EXPLAINED:

controlVolume() function:
   - Main function called when the user says 'controlVolume'
   - Import video using cv2 (opencv) and call mediapipe hands
   - To bring the camera video screen to the front after the website is launched, we include a white window for 1 second
   - Track the hands until the user indicates to stop
   - To stop, track the tips of all the fingers and if they are all open, then the stop position is in place
   - Thumbs up tracking is done with hand position 4
   - Thumbs down tracking is done with hand position 20
   - Use CliClick to Control volume up and volume down 
