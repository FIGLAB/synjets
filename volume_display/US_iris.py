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

def stat_open(p, ser):
    print("static open")
    wf = wave.open('45hz_1.5sec.wav', 'rb')
    stream = p.open(format=p.get_format_from_width(wf.getsampwidth()),
                    channels=wf.getnchannels(),
                    rate=wf.getframerate(),
                    output=True)
    ser.write(bytes("open", 'utf-8'))
    ser.flush()
    time.sleep(0.2)
    playaudio(wf, stream)
    # stop stream
    stream.stop_stream()
    stream.close()

def stat_close(p, ser):
    print("static close")
    wf = wave.open('45hz_1.5sec.wav', 'rb')
    stream = p.open(format=p.get_format_from_width(wf.getsampwidth()),
                    channels=wf.getnchannels(),
                    rate=wf.getframerate(),
                    output=True)
    ser.write(bytes("close", 'utf-8'))
    ser.flush()
    time.sleep(0.2)
    playaudio(wf, stream)
    # stop stream
    stream.stop_stream()
    stream.close()

def move_open(p, ser):
    print("move open")
    wf = wave.open('45hz_1.5sec.wav', 'rb')
    stream = p.open(format=p.get_format_from_width(wf.getsampwidth()),
                    channels=wf.getnchannels(),
                    rate=wf.getframerate(),
                    output=True)
    ser.write(bytes("close", 'utf-8'))
    ser.flush()
    time.sleep(0.1)
    ser.write(bytes("mopen", 'utf-8'))
    ser.flush()
    time.sleep(0.05)
    playaudio(wf, stream)
    # stop stream
    stream.stop_stream()
    stream.close()

def move_close(p, ser):
    print("move close")
    wf = wave.open('45hz_1.5sec.wav', 'rb')
    stream = p.open(format=p.get_format_from_width(wf.getsampwidth()),
                    channels=wf.getnchannels(),
                    rate=wf.getframerate(),
                    output=True)
    ser.write(bytes("open", 'utf-8'))
    ser.flush()
    time.sleep(0.1)
    ser.write(bytes("mclose", 'utf-8'))
    ser.flush()
    time.sleep(0.05)
    playaudio(wf, stream)
    # stop stream
    stream.stop_stream()
    stream.close()

def move_open_close(p, ser):
    print("move open close")
    wf = wave.open('45hz_2.5sec.wav', 'rb')
    stream = p.open(format=p.get_format_from_width(wf.getsampwidth()),
                    channels=wf.getnchannels(),
                    rate=wf.getframerate(),
                    output=True)
    ser.write(bytes("open", 'utf-8'))
    ser.flush()
    time.sleep(0.1)
    ser.write(bytes("moc", 'utf-8'))
    ser.flush()
    time.sleep(0.05)
    playaudio(wf, stream)
    # stop stream
    stream.stop_stream()
    stream.close()

numtimes = 4
stimnames = ["sopen", "sclose"]
stims = [stat_open, stat_close]
guesses = []
counter = np.zeros(len(stims))
if __name__ == "__main__":
    f = open("../data/iris_" + str(round(time.time()))+".txt", "a")
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
        while True:
            func(p, ser)
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
    ser.close()
    # close PyAudio
    p.terminate()
