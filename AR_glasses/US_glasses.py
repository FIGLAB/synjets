import pyaudio
import wave
import sys
import serial
import time
import threading
import numpy as np
import random

CHUNK = 1024
baud = 115200

def playaudio(wf, stream):
    # read data
    data = wf.readframes(CHUNK)
    # play stream
    while len(data) > 0:
        stream.write(data)
        data = wf.readframes(CHUNK)
    wf.rewind()


def front_to_back(p):
    print("Front to back")
    wf = wave.open('front_to_back.wav', 'rb')
    stream = p.open(format=p.get_format_from_width(wf.getsampwidth()),
                    channels=wf.getnchannels(),
                    rate=wf.getframerate(),
                    output=True)
    playaudio(wf, stream)
    stream.stop_stream()
    stream.close()


def back_to_front(p):
    print("Back to front")
    wf = wave.open('back_to_front.wav', 'rb')
    stream = p.open(format=p.get_format_from_width(wf.getsampwidth()),
                    channels=wf.getnchannels(),
                    rate=wf.getframerate(),
                    output=True)
    playaudio(wf, stream)
    stream.stop_stream()
    stream.close()

def click_forward(p):
    print("Click forward")
    wf = wave.open('click_forward.wav', 'rb')
    stream = p.open(format=p.get_format_from_width(wf.getsampwidth()),
                    channels=wf.getnchannels(),
                    rate=wf.getframerate(),
                    output=True)
    playaudio(wf, stream)
    stream.stop_stream()
    stream.close()

def click_backward(p):
    print("Click backward")
    wf = wave.open('click_backward.wav', 'rb')
    stream = p.open(format=p.get_format_from_width(wf.getsampwidth()),
                    channels=wf.getnchannels(),
                    rate=wf.getframerate(),
                    output=True)
    playaudio(wf, stream)
    stream.stop_stream()
    stream.close()

def oppo_click(p):
    print("opposite click")
    wf = wave.open('click_opposite.wav', 'rb')
    stream = p.open(format=p.get_format_from_width(wf.getsampwidth()),
                    channels=wf.getnchannels(),
                    rate=wf.getframerate(),
                    output=True)
    playaudio(wf, stream)
    stream.stop_stream()
    stream.close()

numtimes = 4
stimnames = ["front", "back", "click_for", "click_back", "oppose"]
stims = [front_to_back, back_to_front, click_forward, click_backward, oppo_click]
guesses = []
counter = np.zeros(len(stims))
if __name__ == "__main__":
    f = open("../data/ARglasses_" + str(round(time.time()))+".txt", "a")
    # instantiate PyAudio
    p = pyaudio.PyAudio()

    # Run through all the stimuli randomly
    while True:
        if len(counter) == 0: break
        idx = random.randint(0, len(stims)-1)
        func = stims[idx]
        while True:
            func(p)
            ans = input("What stimuli? ")
            if ans != "n": break
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
