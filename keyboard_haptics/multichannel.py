import pyaudio
import wave
import sys
import serial
import time

CHUNK = 1024
wf = wave.open('100hz_5sec.wav', 'rb')
# instantiate PyAudio
p = pyaudio.PyAudio()
# open stream
stream = p.open(format=p.get_format_from_width(wf.getsampwidth()),
                channels=10,
                rate=wf.getframerate(),
                output_device_index=14,
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
