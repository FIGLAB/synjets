import pyaudio
import wave
import sys
import serial
import time
import threading
import numpy as np
import random

numtimes = 4
stims = ["leftswipe", "rightswipe", "left", "middle", "right", "circle"]
guesses = []
counter = np.zeros(len(stims))
if __name__ == "__main__":
    f = open("../data/HMD" + str(round(time.time()))+".txt", "a")

    while True:
        if len(counter) == 0: break
        idx = random.randint(0, len(stims)-1)
        print("PLAY: " + stims[idx])
        ans = input("What stimuli? ")
        f.write(stims[idx] + " : " + ans + "\n")
        guesses.append((stims[idx], ans))
        counter[idx] += 1
        if counter[idx] == numtimes:
            counter = np.delete(counter, idx)
            del stims[idx]

    print(guesses)
    # close everything
    f.close()
