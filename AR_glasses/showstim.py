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


def front_to_back(p):
    wf = wave.open('front_to_back.wav', 'rb')
    stream = p.open(format=p.get_format_from_width(wf.getsampwidth()),
                    channels=wf.getnchannels(),
                    rate=wf.getframerate(),
                    output=True)
    playaudio(wf, stream)
    stream.stop_stream()
    stream.close()


def back_to_front(p):
    wf = wave.open('back_to_front.wav', 'rb')
    stream = p.open(format=p.get_format_from_width(wf.getsampwidth()),
                    channels=wf.getnchannels(),
                    rate=wf.getframerate(),
                    output=True)
    playaudio(wf, stream)
    stream.stop_stream()
    stream.close()

def click_forward(p):
    wf = wave.open('click_forward.wav', 'rb')
    stream = p.open(format=p.get_format_from_width(wf.getsampwidth()),
                    channels=wf.getnchannels(),
                    rate=wf.getframerate(),
                    output=True)
    playaudio(wf, stream)
    stream.stop_stream()
    stream.close()

def click_backward(p):
    wf = wave.open('click_backward.wav', 'rb')
    stream = p.open(format=p.get_format_from_width(wf.getsampwidth()),
                    channels=wf.getnchannels(),
                    rate=wf.getframerate(),
                    output=True)
    playaudio(wf, stream)
    stream.stop_stream()
    stream.close()

def oppo_click(p):
    wf = wave.open('click_opposite.wav', 'rb')
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

    # Run through all the stimuli randomly
    print("Options: front, back, click forward, click backward, opposite click. or break")
    while True:
        stim = input("Which stimulus to play: ")
        if stim == "break": break
        elif stim == "front": front_to_back(p)
        elif stim == "back": back_to_front(p)
        elif stim == "click forward": click_forward(p)
        elif stim == "click backward": click_backward(p)
        elif stim == "opposite click": oppo_click(p)

    # close PyAudio
    p.terminate()
