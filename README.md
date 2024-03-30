# NoiseGhost
A tool which hides the messages in the audio using LSB method.

# Key Features
- It can hide messages in audio file.
- While giving output file name, it automatically add `.wav` at the end of the output file name.

# MP3 To WAV CLI Converter
- It is a small command-line tool so that it converts mp3 files into wav files.
- It can download from [here](https://github.com/wirebits/NoiseGhost/releases/download/v1.0.0/MP3ToWAVConverter.exe).
- It works only on windows.
- To use this tool, create a folder and put this tool and mp3 file in it.
- Open Terminal.
- Type the following command and press enter :
  
  ```
  MP3ToWAVConverter.exe INPUT.mp3 OUTPUT
  ```
- Replace `INPUT` with actual file name of the mp3 file and `OUTPUT` with actual file name of wav file.
 
# OS Support
- Windows 10

# Supported Audio Format
- WAV

# Setup
Make sure the latest python is installed on your system (Windows/Linux/MacOS).<br>

# Parameters
There are 5 parameters :
1. **-e** - Encode the message.
2. **-d** - Decode the message.
3. **-i** - WAV File.
4. **-m** - Message.
5. **-o** - Output WAV file.

# Install and Run
1. Download or Clone the Repository.
2. Open the folder.
3. Open CMD/Powershell (Windows) or Terminal (Linux) in that folder.
## Encode

```
python NoiseGhost.py -e -i INPUT.wav -m "MESSAGE" -o OUTPUT
```
## Decode

```
python NoiseGhost.py -d -i OUTPUT.wav
```
# Keep In Mind
- Larger the size of the WAV file, it takes more time to encode or decode.
- Large size WAV file encode long messages and less distortion which means the quality of the WAV file remains good.
