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


def wind(p):
    wf = wave.open('wind.wav', 'rb')
    stream = p.open(format=p.get_format_from_width(wf.getsampwidth()),
                    channels=wf.getnchannels(),
                    rate=wf.getframerate(),
                    output=True)
    playaudio(wf, stream)
    stream.stop_stream()
    stream.close()

def fast_vibration(p):
    wf = wave.open('fast_modulation.wav', 'rb')
    stream = p.open(format=p.get_format_from_width(wf.getsampwidth()),
                    channels=wf.getnchannels(),
                    rate=wf.getframerate(),
                    output=True)
    playaudio(wf, stream)
    stream.stop_stream()
    stream.close()

def slow_vibration(p):
    wf = wave.open('slow_modulation.wav', 'rb')
    stream = p.open(format=p.get_format_from_width(wf.getsampwidth()),
                    channels=wf.getnchannels(),
                    rate=wf.getframerate(),
                    output=True)
    playaudio(wf, stream)
    stream.stop_stream()
    stream.close()

def pulses(p):
    wf = wave.open('impulses.wav', 'rb')
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

    print("1: wind. 2: vibration. 3:pulses")
    while True:
        stim = input("Which stimulus to play: ")
        if stim == "break": break
        elif stim == "1": wind(p)
        elif stim == "2": fast_vibration(p)
        elif stim == "3": pulses(p)

    # close PyAudio
    p.terminate()
