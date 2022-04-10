import pyaudio
import wave
import sys
import serial
import time
import threading

CHUNK = 1024
baud = 115200
timestart = time.time()

def playaudio():
    # read data
    data = wf.readframes(CHUNK)
    # play stream
    while len(data) > 0:
        stream.write(data)
        data = wf.readframes(CHUNK)
    wf.rewind()


audio = threading.Thread(target=playaudio)
def high_click(dist):
    global timestart, audio
    if dist > 80 and dist < 120 and abs(time.time()-timestart)>1:
        print("high click!")
        audio.start()
        audio = threading.Thread(target=playaudio)
        timestart = time.time()

def low_click(dist):
    global timestart, audio
    if dist < 40 and abs(time.time()-timestart)>1:
        print("low click!")
        audio.start()
        audio = threading.Thread(target=playaudio)
        timestart = time.time()

prevdist = 120
dists = [20, 40, 60, 80, 100, 120, 140, 160]
def closest(lst, K):
    return lst[min(range(len(lst)), key = lambda i: abs(lst[i]-K))]

def detents(dist):
    global timestart, audio, prevdist
    if abs(prevdist-dist) > 20 and abs(time.time()-timestart)>0.1:
        print("click!")
        audio.start()
        audio = threading.Thread(target=playaudio)
        timestart = time.time()
        prevdist = closest(dists, dist)

counter = []
if __name__ == "__main__":
    wf = wave.open('doubleclick.wav', 'rb')
    # instantiate PyAudio
    p = pyaudio.PyAudio()
    # instantiate Serial
    ser = serial.Serial('COM13', baud, timeout=1)
    time.sleep(3)

    # open stream
    stream = p.open(format=p.get_format_from_width(wf.getsampwidth()),
                    channels=wf.getnchannels(),
                    rate=wf.getframerate(),
                    output=True)
    dist = 0
    while True:
        feedback = ser.readline().decode('utf-8')
        print(feedback.strip())
        if "ERROR" in feedback.strip():
            dist = 0.0
            continue
        dist = float(feedback)
        low_click(dist)

    # stop stream
    stream.stop_stream()
    stream.close()
    ser.close()

    # close PyAudio
    p.terminate()
