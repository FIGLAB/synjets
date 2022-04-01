import pyaudio
import wave
import sys
import serial
import time
import threading
import numpy as np
import random

CHUNK = 1024

def playaudio(wf, stream):
    # read data
    data = wf.readframes(CHUNK)
    # play stream
    while len(data) > 0:
        stream.write(data)
        data = wf.readframes(CHUNK)
    wf.rewind()


def continuous(p):
    wf = wave.open('41hz_2sec.wav', 'rb')
    stream = p.open(format=p.get_format_from_width(wf.getsampwidth()),
                    channels=wf.getnchannels(),
                    rate=wf.getframerate(),
                    output=True)
    playaudio(wf, stream)
    stream.stop_stream()
    stream.close()

def modulated(p):
    wf = wave.open('41hzMOD_2sec.wav', 'rb')
    stream = p.open(format=p.get_format_from_width(wf.getsampwidth()),
                    channels=wf.getnchannels(),
                    rate=wf.getframerate(),
                    output=True)
    playaudio(wf, stream)
    stream.stop_stream()
    stream.close()

def impulses(p):
    wf = wave.open('41hz_impulses.wav', 'rb')
    stream = p.open(format=p.get_format_from_width(wf.getsampwidth()),
                    channels=wf.getnchannels(),
                    rate=wf.getframerate(),
                    output=True)
    playaudio(wf, stream)
    stream.stop_stream()
    stream.close()


if __name__ == "__main__":
    # instantiate PyAudio
    p = pyaudio.PyAudio()

    print("1: continuous. 2: modulated. 3:impulses")
    while True:
        stim = input("Which stimulus to play: ")
        if stim == "break": break
        elif stim == "1": continuous(p)
        elif stim == "2": modulated(p)
        elif stim == "3": impulses(p)

    # close PyAudio
    p.terminate()
