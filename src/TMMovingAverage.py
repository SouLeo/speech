#!/usr/bin/env python
import numpy as np
import soundfile as sf
from scipy import signal 
from scipy.signal import butter, lfilter, freqz
import matplotlib.pyplot as plt

def plot(data):
    plt.plot(data, color='steelblue')
    plt.show()

# I most certainly require a main

if __name__ == '__main__': 
    print "begin"
    data, sampleRate = sf.read('/home/selma/throatfiles/throattest_earphonein_uppedgain_fingersupport.wav')
    ts = 1 / sampleRate
    sizeOfSample = np.size(data)
    # Parks McClellan Algorithm for FIR Filter Design
    numtaps = 5
    bands = np.array([0, .03, .06, .33, .34, .399])
    desired = np.array([0, 1, 0])
    h = signal.remez(numtaps, bands, desired)
    plot(data)
    #magFFT = np.abs(np.fft.fft(data))
    #plot(magFFT)
    print "AAAAAAHHH"
