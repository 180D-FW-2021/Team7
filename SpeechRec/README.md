### Overview

The speech recognition utilizes Google Cloud Speech-to-Text API as well as CLIclick to execute specified speech commands.
This process involves developing a transcript from the computers microphone and then checking the transcript for various
key phrases such as "increase brightness". Speech recognition is integrated with Pose Determination so that when the transcript
detects the phrase "increase volume", it will launch the camera and use gesture control.

### Prerequisites 

- Install [Google Cloud](https://cloud.google.com/sdk/docs/install) 
- Download [PyAudio](https://pypi.org/project/PyAudio/) package using pip or homebrew
- [CliClick Source code](https://github.com/BlueM/cliclick)
  
### Code 

Imports
- Speech from Google cloud to configure the streaming recognition
- Webbbrowser estalishes a connection from the python scripts to the internet to launch browsers
- PyAudio integrates the audio stream from the microphone 
- controlVolume from Pose_Determination to launch the function

class Mircophone Stream
- This class opens a recording stream wiith a generator
- Defines basic funcitons such as init, enter, and exit

listen_print_loop function
- This is where the transcript gets processed and we search for key words
- Computer commands are processed with CliClick
- Print out speech-to-text transcript 

run_speech_rec()
- Main function
- Launches Google Cloud Speech API functions
- Gathers transcript with Microphone Stream class

### More
- Base code from [Google Cloud example resources](https://cloud.google.com/speech-to-text/docs/samples/speech-transcribe-streaming-mic#speech_transcribe_streaming_mic-python)
- Author: Neha Adhlakha 
- Last Modified: 12/12/21
