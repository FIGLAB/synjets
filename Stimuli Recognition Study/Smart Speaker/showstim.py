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
timestart = time.time()

def playaudio(wf, stream):
    # read data
    data = wf.readframes(CHUNK)
    # play stream
    while len(data) > 0:
        stream.write(data)
        data = wf.readframes(CHUNK)
    wf.rewind()

def high_click(p, ser, sec=5):
    print("high click!")
    timestart = time.time()
    wf = wave.open('doubleclick.wav', 'rb')
    stream = p.open(format=p.get_format_from_width(wf.getsampwidth()),
                    channels=wf.getnchannels(),
                    rate=wf.getframerate(),
                    output=True)
    audio = threading.Thread(target=playaudio, args=(wf, stream,))
    dist = 0
    timezero = time.time()
    while time.time()-timezero < sec:
        feedback = ser.readline().decode('utf-8')
        if "ERROR" in feedback.strip():
            dist = 0.0
            continue
        # print(feedback.strip())
        dist = float(feedback)
        if dist > 80 and dist < 120 and abs(time.time()-timestart)>0.5:
            audio.start()
            audio = threading.Thread(target=playaudio, args=(wf, stream,))
            timestart = time.time()

    # stop stream
    stream.stop_stream()
    stream.close()

def low_click(p, ser, sec=5):
    print("low click!")
    timestart = time.time()
    wf = wave.open('doubleclick.wav', 'rb')
    stream = p.open(format=p.get_format_from_width(wf.getsampwidth()),
                    channels=wf.getnchannels(),
                    rate=wf.getframerate(),
                    output=True)
    audio = threading.Thread(target=playaudio, args=(wf, stream,))
    dist = 0
    timezero = time.time()
    while time.time()-timezero < sec:
        feedback = ser.readline().decode('utf-8')
        if "ERROR" in feedback.strip():
            dist = 0.0
            continue
        # print(feedback.strip())
        dist = float(feedback)
        if dist < 40 and abs(time.time()-timestart)>0.5:
            audio.start()
            audio = threading.Thread(target=playaudio, args=(wf, stream,))
            timestart = time.time()

    # stop stream
    stream.stop_stream()
    stream.close()

prevdist = 120
dists = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110, 120, 130, 140, 150, 160]
def closest(lst, K):
    return lst[min(range(len(lst)), key = lambda i: abs(lst[i]-K))]

def detents(p, ser, sec=5):
    print("detents!")
    timestart = time.time()
    wf = wave.open('sharp_100hz_short.wav', 'rb')
    stream = p.open(format=p.get_format_from_width(wf.getsampwidth()),
                    channels=wf.getnchannels(),
                    rate=wf.getframerate(),
                    output=True)
    audio = threading.Thread(target=playaudio, args=(wf, stream,))
    dist = 0
    prevdist = 120
    timezero = time.time()
    while time.time()-timezero < sec:
        feedback = ser.readline().decode('utf-8')
        if "ERROR" in feedback.strip():
            dist = 0.0
            continue
        # print(feedback.strip())
        dist = float(feedback)
        if abs(prevdist-dist) > 10:
            audio.start()
            audio = threading.Thread(target=playaudio, args=(wf, stream,))
            timestart = time.time()
            prevdist = closest(dists, dist)

    # stop stream
    stream.stop_stream()
    stream.close()

if __name__ == "__main__":
    # instantiate PyAudio
    p = pyaudio.PyAudio()
    # instantiate Serial
    ser = serial.Serial('COM13', baud, timeout=1)
    time.sleep(3)

    # Run through all the stimuli randomly
    print("1: low_click. 2: high_click. 3: detents. 0: break.")
    print("Second number (x,x) is # of seconds.")
    while True:
        inp = input("Which stimulus to play: ")
        if inp == "0" or inp == "break": break
        stimnum, sec = inp.split(",")
        if int(stimnum) == 1: low_click(p, ser, int(sec))
        elif int(stimnum) == 2: high_click(p, ser, int(sec))
        elif int(stimnum) == 3: detents(p, ser, int(sec))

    # close everything
    ser.close()
    # close PyAudio
    p.terminate()
