import pyaudio
import wave
import sys
import serial
import time

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
    # open stream
    stream = p.open(format=p.get_format_from_width(wf.getsampwidth()),
                    channels=wf.getnchannels(),
                    rate=wf.getframerate(),
                    output=True)
    ser.write(bytes("open", 'utf-8'))
    ser.flush()
    time.sleep(0.1)
    playaudio(wf, stream)
    # stop stream
    stream.stop_stream()
    stream.close()

def stat_close(p, ser):
    wf = wave.open('45hz_1.5sec.wav', 'rb')
    # open stream
    stream = p.open(format=p.get_format_from_width(wf.getsampwidth()),
                    channels=wf.getnchannels(),
                    rate=wf.getframerate(),
                    output=True)
    ser.write(bytes("close", 'utf-8'))
    ser.flush()
    time.sleep(0.1)
    playaudio(wf, stream)
    # stop stream
    stream.stop_stream()
    stream.close()

def move_open():
    ser.write(bytes("mopen", 'utf-8'))
    ser.flush()
    time.sleep(0.05)
def move_close():
    ser.write(bytes("mclose", 'utf-8'))
    ser.flush()
    time.sleep(0.05)
def move_open_close():
    ser.write(bytes("moc", 'utf-8'))
    ser.flush()
    time.sleep(0.05)

CHUNK = 1024
baud = 115200
counter = []
if __name__ == "__main__":
    # instantiate PyAudio
    p = pyaudio.PyAudio()
    # instantiate Serial
    ser = serial.Serial('COM11', baud, timeout=1)
    time.sleep(3) # instantiate the serial!


    while True:
        word = input("enter action: ")
        if word == "open": stat_open(p, ser)
        if word == "close": stat_close(p, ser)
        if word == "break": break

    ser.close()
    # close PyAudio
    p.terminate()
