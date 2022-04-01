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

def high_click(p, ser):
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
    while time.time()-timezero < 5:
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

def low_click(p, ser):
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
    while time.time()-timezero < 5:
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
dists = [20, 40, 60, 80, 100, 120, 140, 160]
def closest(lst, K):
    return lst[min(range(len(lst)), key = lambda i: abs(lst[i]-K))]

def detents(p, ser):
    print("detents!")
    timestart = time.time()
    wf = wave.open('sharp_100hz.wav', 'rb')
    stream = p.open(format=p.get_format_from_width(wf.getsampwidth()),
                    channels=wf.getnchannels(),
                    rate=wf.getframerate(),
                    output=True)
    audio = threading.Thread(target=playaudio, args=(wf, stream,))
    dist = 0
    prevdist = 120
    timezero = time.time()
    while time.time()-timezero < 5:
        feedback = ser.readline().decode('utf-8')
        if "ERROR" in feedback.strip():
            dist = 0.0
            continue
        # print(feedback.strip())
        dist = float(feedback)
        if abs(prevdist-dist) > 20 and abs(time.time()-timestart)>0.1:
            audio.start()
            audio = threading.Thread(target=playaudio, args=(wf, stream,))
            timestart = time.time()
            prevdist = closest(dists, dist)

    # stop stream
    stream.stop_stream()
    stream.close()

numtimes = 4
stimnames = ["low_click", "high_click", "detents"]
stims = [low_click, high_click, detents]
guesses = []
counter = np.zeros(len(stims))
if __name__ == "__main__":
    f = open("data/" + str(round(time.time()))+".txt", "a")
    # instantiate PyAudio
    p = pyaudio.PyAudio()
    # instantiate Serial
    ser = serial.Serial('COM13', baud, timeout=1)
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
