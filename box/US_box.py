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


numtimes = 4
stimnames = ["continuous", "modulated", "impulses"]
stims = [continuous, modulated, impulses]
guesses = []
counter = np.zeros(len(stims))
if __name__ == "__main__":
    f = open("data/" + str(round(time.time()))+".txt", "a")
    # instantiate PyAudio
    p = pyaudio.PyAudio()

    print("1: continuous. 2: modulated. 3:impulses")
    while True:
        if len(counter) == 0: break
        idx = random.randint(0, len(stims)-1)
        func = stims[idx]
        func(p)
        ans = input("What stimuli? ")
        if ans == "n": continue
        f.write(stimnames[idx] + " : " + ans + "\n")
        guesses.append((stimnames[idx], ans))
        counter[idx] += 1
        if counter[idx] == numtimes:
            counter = np.delete(counter, idx)
            del stimnames[idx]
            del stims[idx]

    print(guesses)
    # close everything
    f.close()
    # close PyAudio
    p.terminate()
