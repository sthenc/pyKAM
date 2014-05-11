#!/usr/bin/python3
################################################################################
#
#	Copyright 2014 Stjepan Henc <sthenc@gmail.com>
#
#	Licensed under the Apache License, Version 2.0 (the "License");
#	you may not use this file except in compliance with the License.
#	You may obtain a copy of the License at
#
#		http://www.apache.org/licenses/LICENSE-2.0
#
#	Unless required by applicable law or agreed to in writing, software
#	distributed under the License is distributed on an "AS IS" BASIS,
#	WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#	See the License for the specific language governing permissions and
#	limitations under the License.
#
################################################################################

import scipy.io.wavfile as wav
import numpy as np
import copy

class Signal:

    # Data loaders
    def LoadFromFile(self, file):
        self.fs, self.s = wav.read(file)
        self.sLength, self.nChans = self.s.shape

    def LoadWF(self, waveform, fs):
        self.s = waveform
        self.fs = fs
        self.sLength, self.nChans = self.s.shape
    
    def __init__(self, *args):
        
        #signal properties
        self.singlePrecision = 0
        self.s = np.array([])
        self.fs = 44100
        self.sLength = 0
        self.nChans = 0
        self.weightingFunction = np.hamming #FIXME
        
        #STFT properties
        self.S = np.array([])
        self.windowLength = 60
        self.nfft = 0
        self.nfftUtil = 0
        self.overlapRatio = 0.5
        self.framesPositions = np.array([])
        self.nFrames = 0
        self.weightingWindow = np.array([])
        self.overlap = 0
        

        # Windowing properties
        self.sWin = np.array([])
        self.sWeights = np.array([])
        self.sWin = np.array([])
        self.sWeights = np.array([])
        
        
        if len(args) == 1:
            if type(args[0]) == type(''): # it's a filename
                self.LoadFromFile(args[0])
            elif type(args[0] == type(self)): # copy data from other signal
                self.__dict__ = copy.deepcopy(args[0].__dict__)
                    
        elif len(args) == 2: # args[0] is a signal, args[1] is sample freq.
            self.LoadWF(args(0), args(1))


