import pyaudio
import wave
import sys
import serial
import time

# TURN VOLUME 100!
CHUNK = 1024
wf = wave.open('30hz_1sec.wav', 'rb')
# instantiate PyAudio
p = pyaudio.PyAudio()
# open stream
stream = p.open(format=p.get_format_from_width(wf.getsampwidth()),
                channels=wf.getnchannels(),
                rate=wf.getframerate(),
                output=True)

for i in range(6):
    # read data
    data = wf.readframes(CHUNK)
    # play stream
    while len(data) > 0:
        stream.write(data)
        data = wf.readframes(CHUNK)
    wf.rewind()
# stop stream
stream.stop_stream()
stream.close()

# close PyAudio
p.terminate()
