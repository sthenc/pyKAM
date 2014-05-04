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



#import audioread
#indf = audioread.audio_open('../../data/trololo.mp4')
#ar = [x for x in indf];
#print(indf.channels, indf.samplerate, indf.duration)
#print(ar[0])
#indf.close()

import numpy as np
import scipy.io.wavfile as wav
from scipy.interpolate import interp1d


sr, y = wav.read("../../data/stereo-blauen1.wav")

ly = y.T[0]
ry = y.T[1]


x = np.linspace(0, 10000, len(y))
lf = interp1d(x, ly)
rf = interp1d(x, ry)

print("pocetak racunanja")
sr2 = 96000
ly2 = [lf(t) for t in np.linspace(0, 10000, len(y) * sr2/sr)]
ry2 = [rf(t) for t in np.linspace(0, 10000, len(y) * sr2/sr)]


y2 = array([ly2,ry2]).T

wav.write("./stereo-resampled.wav", sr2, y2)

