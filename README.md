# NoiseGhost
A tool which hides the messages in the audio using LSB method.

# Key Features
- It can hide messages in audio file.
- While giving output file name, it automatically add `.wav` at the end of the output file name.

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
