import pyaudio
import wave
import sys
import serial
import time

CHUNK = 1024
wf = wave.open('volume_display/45hz_2sec.wav', 'rb')
# instantiate PyAudio
p = pyaudio.PyAudio()
# open stream
stream = p.open(format=p.get_format_from_width(wf.getsampwidth()),
                channels=wf.getnchannels(),
                rate=wf.getframerate(),
                output=True)

# read data
data = wf.readframes(CHUNK)
# play stream
while len(data) > 0:
    stream.write(data)
    data = wf.readframes(CHUNK)
# stop stream
stream.stop_stream()
stream.close()

# close PyAudio
p.terminate()
