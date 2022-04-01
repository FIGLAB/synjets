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
    print("right swipe")
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
    print("left swipe")
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
    print("up swipe")
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
    print("down swipe")
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
    print("left")
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
    print("right")
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
    print("bot")
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

def top(p, ser):
    print("top")
    wf = wave.open('41hz_1.5sec.wav', 'rb')
    stream = p.open(format=p.get_format_from_width(wf.getsampwidth()),
                    channels=wf.getnchannels(),
                    rate=wf.getframerate(),
                    output=True)
    ser.write(bytes("top", 'utf-8'))
    ser.flush()
    time.sleep(0.5)
    playaudio(wf, stream)
    stream.stop_stream()
    stream.close()

def mid(p, ser):
    print("mid")
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
    print("circle")
    wf = wave.open('41hz_2sec.wav', 'rb')
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

numtimes = 3
stimnames = ["top", "bot", "mid", "leftswipe", "rightswipe", "upswipe", "downswipe", "circle"]
stims = [top, bot, mid, leftswipe, rightswipe, upswipe, downswipe, circle]
guesses = []
counter = np.zeros(len(stims))
if __name__ == "__main__":
    f = open("data/" + str(round(time.time()))+".txt", "a")
    # instantiate PyAudio
    p = pyaudio.PyAudio()
    # instantiate Serial
    ser = serial.Serial('COM11', baud, timeout=1)
    time.sleep(3)

    # Run through all the stimuli randomly
    while True:
        if len(counter) == 0: break
        idx = random.randint(0, len(stims)-1)
        func = stims[idx]
        func(p, ser)
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
    ser.close()
    # close PyAudio
    p.terminate()
