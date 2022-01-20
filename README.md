# Team7

Mr. Remote Source code

MQTT
- Uses MQTT communication to zoom in and zoom out

MOUSE
- Uses Arduino 33 BLE's IMU to create a computer mouse that is controlled by IMU movement

Pose_Determination
- Uses Mediapipe to control volume using hand pose determination 

SpeechRec
- Google Cloud Speech API to detect certain commands such as click/increase brightness

Visualization
- HTML file that creates our main website with certain shortcuts


START UP:
1. Launch PC_subscriber script for MQTT: "python3 PC_subscriber.py"
2. Connect Rasperry Pi and launch button_control script on RPi terminal: "./RPi_publisher.py"
3. Connect Arduino to power
4. Run main script on laptop to launch visualization, pose determination, and speech recognition

