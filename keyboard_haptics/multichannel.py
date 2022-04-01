import pyaudio
import wave
import sys
import serial
import time

CHUNK = 1024
wf = wave.open('100hz_1sec.wav', 'rb')
# instantiate PyAudio
p = pyaudio.PyAudio()
print(p.get_device_count())
print(p.get_default_output_device_info())
for i in range(20):
    print(p.get_device_info_by_index(i))
# open stream
channel_map = (0, 1, -1, -1, -1, -1, -1, -1)
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
