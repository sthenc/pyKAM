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
        self.precision = 64
        self.s = np.array([], np.float64)
        self.fs = 44100
        self.sLength = 0
        self.nChans = 0
        self.weightingFunction = np.hamming
        
        #STFT properties
        self.S = np.array([], np.float64)
        self.windowLength = 60
        self.nfft = 0
        self.nfftUtil = 0
        self.overlapRatio = 0.5
        self.framesPositions = np.array([], np.float64)
        self.nFrames = 0
        self.weightingWindow = np.array([], np.float64)
        self.overlap = 0

        # Windowing properties
        self.sWin = np.array([], np.float64)
        self.sWeights = np.array([], np.float64)
        self.sWin = np.array([], np.float64)
        self.sWeights = np.array([], np.float64)
        
        
        if len(args) == 1:
            if type(args[0]) == type(''): # it's a filename
                self.LoadFromFile(args[0])
            elif type(args[0] == type(self)): # copy data from other signal
                self.__dict__ = copy.deepcopy(args[0].__dict__)
                    
        elif len(args) == 2: # args[0] is a signal, args[1] is sample freq.
            self.LoadWF(args(0), args(1))


# Properties and constraints definitions
        

    def set_precision(self, val):

        if not ('_precision' in self.__dict__):
            self._precision = val
    	
        if self._precision != val:
            self._precision = val
            if (val == 32):
                for k in self.__dict__:
                    if k != 'weightingFunction':
                        self.__dict__[k] = np.float32(self.__dict__[k])
            elif (val == 16):
                for k in self.__dict__:
                    if k != 'weightingFunction':
                        self.__dict__[k] = np.float16(self.__dict__[k])
            else:
                for k in self.__dict__:
                    if k != 'weightingFunction':
                        self.__dict__[k] = np.float64(self.__dict__[k])
	
    def get_precision(self):
	    return self._precision
		
    precision = property(get_precision, set_precision)
#s 

#fs

#windowLength

#nfft

#overlapRatio

    def set_S(self, value):
        self._S = value

    def get_S(self):
        return self._S
    
    S = property(get_S, set_S)
    
#weightingFunction - evaluate weightingWindow

# TODO something for handling windowfunctions that take both nfft and overlapRatio as input
