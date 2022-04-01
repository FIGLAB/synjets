import pyaudio
import wave
import sys
import serial
import time

def playaudio():
    # read data
    data = wf.readframes(CHUNK)
    # play stream
    while len(data) > 0:
        stream.write(data)
        data = wf.readframes(CHUNK)
    wf.rewind()

def rightswipe():
    ser.write(bytes("right", 'utf-8'))
    ser.flush()
    time.sleep(3)
    ser.write(bytes("ls", 'utf-8'))
    ser.flush()
    time.sleep(0.5)

def leftswipe():
    ser.write(bytes("left", 'utf-8'))
    ser.flush()
    time.sleep(3)
    ser.write(bytes("rs", 'utf-8'))
    ser.flush()
    time.sleep(0.5)

def upswipe():
    ser.write(bytes("bot", 'utf-8'))
    ser.flush()
    time.sleep(3)
    ser.write(bytes("us", 'utf-8'))
    ser.flush()
    time.sleep(0.5)

def downswipe():
    ser.write(bytes("top", 'utf-8'))
    ser.flush()
    time.sleep(3)
    ser.write(bytes("ds", 'utf-8'))
    ser.flush()
    time.sleep(0.5)

def left():
    ser.write(bytes("left", 'utf-8'))
    ser.flush()
    time.sleep(0.5)

def right():
    ser.write(bytes("right", 'utf-8'))
    ser.flush()
    time.sleep(0.5)

def bot():
    ser.write(bytes("bot", 'utf-8'))
    ser.flush()
    time.sleep(0.5)

def mid():
    ser.write(bytes("mid", 'utf-8'))
    ser.flush()
    time.sleep(0.5)

def circle():
    ser.write(bytes("circle", 'utf-8'))
    ser.flush()
    time.sleep(0.8)

CHUNK = 1024
baud = 115200
counter = []
if __name__ == "__main__":
    wf = wave.open('41hz_1.5sec.wav', 'rb')
    # instantiate PyAudio
    p = pyaudio.PyAudio()
    # instantiate Serial
    ser = serial.Serial('COM11', baud, timeout=1)
    time.sleep(3) # instantiate the serial!

    # open stream
    stream = p.open(format=p.get_format_from_width(wf.getsampwidth()),
                    channels=wf.getnchannels(),
                    rate=wf.getframerate(),
                    output=True)

    while True:
        word = input("enter action: ")
        ser.write(bytes(word, 'utf-8'))
        ser.flush()
        if word == "middle": time.sleep(0.5)
        playaudio()

    # stop stream
    stream.stop_stream()
    stream.close()
    ser.close()

    # close PyAudio
    p.terminate()
