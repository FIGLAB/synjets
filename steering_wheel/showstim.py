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


def rightswipe(p, ser):
    wf = wave.open('41hz_1.5sec.wav', 'rb')
    stream = p.open(format=p.get_format_from_width(wf.getsampwidth()),
                    channels=wf.getnchannels(),
                    rate=wf.getframerate(),
                    output=True)
    ser.write(bytes("right", 'utf-8'))
    ser.flush()
    time.sleep(0.5)
    ser.write(bytes("ls", 'utf-8'))
    ser.flush()
    time.sleep(0.05)
    playaudio(wf, stream)
    stream.stop_stream()
    stream.close()


def leftswipe(p, ser):
    wf = wave.open('41hz_1.5sec.wav', 'rb')
    stream = p.open(format=p.get_format_from_width(wf.getsampwidth()),
                    channels=wf.getnchannels(),
                    rate=wf.getframerate(),
                    output=True)
    ser.write(bytes("left", 'utf-8'))
    ser.flush()
    time.sleep(0.5)
    ser.write(bytes("rs", 'utf-8'))
    ser.flush()
    time.sleep(0.05)
    playaudio(wf, stream)
    stream.stop_stream()
    stream.close()

def upswipe(p, ser):
    wf = wave.open('41hz_1.5sec.wav', 'rb')
    stream = p.open(format=p.get_format_from_width(wf.getsampwidth()),
                    channels=wf.getnchannels(),
                    rate=wf.getframerate(),
                    output=True)
    ser.write(bytes("bot", 'utf-8'))
    ser.flush()
    time.sleep(0.5)
    ser.write(bytes("us", 'utf-8'))
    ser.flush()
    time.sleep(0.05)
    playaudio(wf, stream)
    stream.stop_stream()
    stream.close()

def downswipe(p, ser):
    wf = wave.open('41hz_1.5sec.wav', 'rb')
    stream = p.open(format=p.get_format_from_width(wf.getsampwidth()),
                    channels=wf.getnchannels(),
                    rate=wf.getframerate(),
                    output=True)
    ser.write(bytes("top", 'utf-8'))
    ser.flush()
    time.sleep(0.5)
    ser.write(bytes("ds", 'utf-8'))
    ser.flush()
    time.sleep(0.05)
    playaudio(wf, stream)
    stream.stop_stream()
    stream.close()

def left(p, ser):
    wf = wave.open('41hz_1.5sec.wav', 'rb')
    stream = p.open(format=p.get_format_from_width(wf.getsampwidth()),
                    channels=wf.getnchannels(),
                    rate=wf.getframerate(),
                    output=True)
    ser.write(bytes("left", 'utf-8'))
    ser.flush()
    time.sleep(0.5)
    playaudio(wf, stream)
    stream.stop_stream()
    stream.close()

def right(p, ser):
    wf = wave.open('41hz_1.5sec.wav', 'rb')
    stream = p.open(format=p.get_format_from_width(wf.getsampwidth()),
                    channels=wf.getnchannels(),
                    rate=wf.getframerate(),
                    output=True)
    ser.write(bytes("right", 'utf-8'))
    ser.flush()
    time.sleep(0.5)
    playaudio(wf, stream)
    stream.stop_stream()
    stream.close()

def bot(p, ser):
    wf = wave.open('41hz_1.5sec.wav', 'rb')
    stream = p.open(format=p.get_format_from_width(wf.getsampwidth()),
                    channels=wf.getnchannels(),
                    rate=wf.getframerate(),
                    output=True)
    ser.write(bytes("bot", 'utf-8'))
    ser.flush()
    time.sleep(0.5)
    playaudio(wf, stream)
    stream.stop_stream()
    stream.close()

def mid(p, ser):
    wf = wave.open('41hz_1.5sec.wav', 'rb')
    stream = p.open(format=p.get_format_from_width(wf.getsampwidth()),
                    channels=wf.getnchannels(),
                    rate=wf.getframerate(),
                    output=True)
    ser.write(bytes("mid", 'utf-8'))
    ser.flush()
    time.sleep(0.5)
    playaudio(wf, stream)
    stream.stop_stream()
    stream.close()

def circle(p, ser):
    wf = wave.open('41hz_1.5sec.wav', 'rb')
    stream = p.open(format=p.get_format_from_width(wf.getsampwidth()),
                    channels=wf.getnchannels(),
                    rate=wf.getframerate(),
                    output=True)
    ser.write(bytes("left", 'utf-8'))
    ser.flush()
    time.sleep(0.5)
    ser.write(bytes("circle", 'utf-8'))
    ser.flush()
    time.sleep(0.05)
    playaudio(wf, stream)
    stream.stop_stream()
    stream.close()

if __name__ == "__main__":
    # instantiate PyAudio
    p = pyaudio.PyAudio()
    # instantiate Serial
    ser = serial.Serial('COM11', baud, timeout=1)
    time.sleep(3)

    # Run through all the stimuli randomly
    while True:
        stim = input("Which stimulus to play: ")
        if stim == "break": break
        elif stim == "mid": mid(p, ser)
        elif stim == "bot": bot(p, ser)
        elif stim == "top": top(p, ser)
        elif stim == "left": left(p, ser)
        elif stim == "right": right(p, ser)
        elif stim == "leftswipe": leftswipe(p, ser)
        elif stim == "rightswipe": rightswipe(p, ser)
        elif stim == "upswipe": upswipe(p, ser)
        elif stim == "downswipe": downswipe(p, ser)

    # close everything
    ser.close()
    # close PyAudio
    p.terminate()
