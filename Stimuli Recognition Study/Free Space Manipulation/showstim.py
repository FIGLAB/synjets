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
    wf = wave.open('45hz_1.5sec_ramp.wav', 'rb')
    stream = p.open(format=p.get_format_from_width(wf.getsampwidth()),
                    channels=wf.getnchannels(),
                    rate=wf.getframerate(),
                    output=True)
    # ser.write(bytes("close", 'utf-8'))
    # ser.flush()
    # time.sleep(0.1)
    stat_close(p,ser)
    ser.write(bytes("mopen", 'utf-8'))
    ser.flush()
    time.sleep(0.05)
    playaudio(wf, stream)
    # stop stream
    stream.stop_stream()
    stream.close()
    stat_open(p,ser)

def move_close(p, ser):
    wf = wave.open('45hz_1.5sec_ramp.wav', 'rb')
    stream = p.open(format=p.get_format_from_width(wf.getsampwidth()),
                    channels=wf.getnchannels(),
                    rate=wf.getframerate(),
                    output=True)
    # ser.write(bytes("open", 'utf-8'))
    # ser.flush()
    # time.sleep(0.1)
    stat_open(p,ser)
    ser.write(bytes("mclose", 'utf-8'))
    ser.flush()
    time.sleep(0.05)
    playaudio(wf, stream)
    # stop stream
    stream.stop_stream()
    stream.close()
    stat_close(p,ser)

def move_open_close(p, ser):
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

if __name__ == "__main__":
    # instantiate PyAudio
    p = pyaudio.PyAudio()
    # instantiate Serial
    ser = serial.Serial('COM11', baud, timeout=1)
    time.sleep(3)

    # Run through all the stimuli randomly
    print("1: open. 2: close. or break")
    while True:
        stim = input("Which stimulus to play: ")
        if stim == "break": break
        elif stim == "1": stat_open(p, ser)
        elif stim == "2": stat_close(p, ser)
        elif stim == "3": move_open(p, ser)
        elif stim == "4": move_close(p, ser)
        elif stim == "5": move_open_close(p, ser)

    # close everything
    ser.close()
    # close PyAudio
    p.terminate()
