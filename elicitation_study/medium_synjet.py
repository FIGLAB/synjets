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

 # peak voltage little over 2v
def continuous(p):
    wf = wave.open('med_cont.wav', 'rb')
    stream = p.open(format=p.get_format_from_width(wf.getsampwidth()),
                    channels=wf.getnchannels(),
                    rate=wf.getframerate(),
                    output=True)
    playaudio(wf, stream)
    stream.stop_stream()
    stream.close()

# nyquist prompt decay: (mult *track* (hzosc 3))
def modulated(p):
    wf = wave.open('med_mod_5hz.wav', 'rb')
    stream = p.open(format=p.get_format_from_width(wf.getsampwidth()),
                    channels=wf.getnchannels(),
                    rate=wf.getframerate(),
                    output=True)
    playaudio(wf, stream)
    stream.stop_stream()
    stream.close()

def impulse(p):
    wf = wave.open('med_impulse.wav', 'rb')
    stream = p.open(format=p.get_format_from_width(wf.getsampwidth()),
                    channels=wf.getnchannels(),
                    rate=wf.getframerate(),
                    output=True)
    playaudio(wf, stream)
    stream.stop_stream()
    stream.close()

def single(p):
    wf = wave.open('med_single.wav', 'rb')
    stream = p.open(format=p.get_format_from_width(wf.getsampwidth()),
                    channels=wf.getnchannels(),
                    rate=wf.getframerate(),
                    output=True)
    playaudio(wf, stream)
    stream.stop_stream()
    stream.close()

def focus(p):
    wf = wave.open('med_cont.wav', 'rb')
    stream = p.open(format=p.get_format_from_width(wf.getsampwidth()),
                    channels=wf.getnchannels(),
                    rate=wf.getframerate(),
                    output=True)
    playaudio(wf, stream)
    stream.stop_stream()
    stream.close()
    time.sleep(1)

    wf = wave.open('med_cont.wav', 'rb')
    stream = p.open(format=p.get_format_from_width(wf.getsampwidth()),
                    channels=wf.getnchannels(),
                    rate=wf.getframerate(),
                    output=True)
    playaudio(wf, stream)
    stream.stop_stream()
    stream.close()

def direction(p):
    wf = wave.open('med_direction.wav', 'rb')
    stream = p.open(format=p.get_format_from_width(wf.getsampwidth()),
                    channels=wf.getnchannels(),
                    rate=wf.getframerate(),
                    output=True)
    playaudio(wf, stream)
    stream.stop_stream()
    stream.close()

stimnames = ["continuous", "modulated", "impulse", "single", "focus", "swipe", "direction"]
stims = [continuous, modulated, impulse, single, focus, direction, continuous]
if __name__ == "__main__":
    f = open("../data/med_" + str(round(time.time()))+".txt", "a")
    # instantiate PyAudio
    p = pyaudio.PyAudio()

    for idx in range(len(stims)):
        func = stims[idx]
        replaycount = 1
        while True:
            print("Playing stimuli: " + stimnames[idx])
            time.sleep(0.5)
            func(p)
            ans = input("replay? ")
            if ans == "no": break
            replaycount += 1
        f.write(stimnames[idx] + ":" + str(replaycount) + "\n")

    # close everything
    f.close()
    # close PyAudio
    p.terminate()
