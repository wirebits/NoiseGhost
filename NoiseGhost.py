# NoiseGhost
# A tool which hides the messages in the audio using LSB method.
# Author - WireBits

import os
import wave
import argparse

def enc_msg(message, audio_file, output_file):
    wav_audio = wave.open(audio_file, mode='rb')
    frame_bytes = bytearray(list(wav_audio.readframes(wav_audio.getnframes())))
    message = message + int((len(frame_bytes)-(len(message)*8*8))/8) *'#'
    bits = list(map(int, ''.join([bin(ord(i)).lstrip('0b').rjust(8,'0') for i in message])))
    for i, bit in enumerate(bits):
        frame_bytes[i] = (frame_bytes[i] & 254) | bit
    frame_modified = bytes(frame_bytes)
    with wave.open(output_file, 'wb') as encFile:
        encFile.setparams(wav_audio.getparams())
        encFile.writeframes(frame_modified)
    wav_audio.close()

def dec_msg(audio_file):
    wav_audio = wave.open(audio_file, mode='rb')
    frame_bytes = bytearray(list(wav_audio.readframes(wav_audio.getnframes())))
    extracted = [frame_bytes[i] & 1 for i in range(len(frame_bytes))]
    string = "".join(chr(int("".join(map(str,extracted[i:i+8])),2)) for i in range(0,len(extracted),8))
    msg = string.split("###")[0]
    print("Hidden Message :", msg)
    wav_audio.close()

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Noise Ghost")
    parser.add_argument("-e", "--encode", action="store_true", help="Encode Message")
    parser.add_argument("-d", "--decode", action="store_true", help="Decode Message")
    parser.add_argument("-i", "--input", required=False, help="WAV File")
    parser.add_argument("-m", "--message", required=False, help="Message")
    parser.add_argument("-o", "--output", required=False, help="Output WAV File")
    args = parser.parse_args()

    if args.encode:
        if not (args.input and args.message):
            print("Error: Both input file and message are required for encoding.")
            exit(1)
        output_file = args.output if args.output else args.input
        if output_file.endswith('.wav'):
            print("Warning: Remove .wav from output file!")
            exit(1)
        output_file += '.wav'
        enc_msg(args.message, args.input, output_file)
        print(f"File has been encoded and saved as {output_file}!")
    elif args.decode:
        if not args.input:
            print("Error: Input file is required for decoding.")
            exit(1)
        dec_msg(args.input)