import pyaudio
import wave
import sys
import serial
import time
from scipy.io import wavfile

CHUNK = 1024
wf = wave.open('45hz_1.5sec.wav', 'rb')
samplerate, data = wavfile.read('45hz_1.5sec.wav')
# instantiate PyAudio
p = pyaudio.PyAudio()
# open stream
stream = p.open(format=p.get_format_from_width(wf.getsampwidth()),
                channels=wf.getnchannels(),
                rate=wf.getframerate(),
                output=True)

for i in range(4):
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
