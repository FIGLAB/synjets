
import pyaudio
import wave
import sys

chunk = 4096

PyAudio = pyaudio.PyAudio

wf = wave.open(sys.argv[1], 'rb')

p = PyAudio()

# standard L-R stereo
# channel_map = (0, 1)

# reverse: R-L stereo
# channel_map = (1, 0)

# no audio
# channel_map = (-1, -1)

# left channel audio --> left speaker; no right channel
# channel_map = (0, -1)

# right channel audio --> right speaker; no left channel
# channel_map = (-1, 1)

# left channel audio --> right speaker
# channel_map = (-1, 0)

# right channel audio --> left speaker
channel_map = (0, -1, -1, -1, -1, -1, -1, -1)
# etc...

try:
    stream_info = pyaudio.PaMacCoreStreamInfo(
        flags=pyaudio.PaMacCoreStreamInfo.paMacCorePlayNice, # default
        channel_map=channel_map)
except AttributeError:
    print("Sorry, couldn't find PaMacCoreStreamInfo. Make sure that "
          "you're running on Mac OS X.")
    sys.exit(-1)

print("Stream Info Flags:", stream_info.get_flags())
print("Stream Info Channel Map:", stream_info.get_channel_map())
print("channels",wf.getnchannels())
#wf.setnchannels(2)
print('sample width',wf.getsampwidth())
# open stream
stream = p.open(
    format=p.get_format_from_width(wf.getsampwidth()),
    channels=wf.getnchannels(),
    rate=wf.getframerate(),
    output=True,
    output_host_api_specific_stream_info=stream_info)

# read data
data = wf.readframes(chunk)

# play stream
while data != '':
    stream.write(data)
    data = wf.readframes(chunk)

stream.stop_stream()
stream.close()

p.terminate()
