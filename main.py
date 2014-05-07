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

import math as m
import numpy as np
import scipy.io.wavfile as wav
from scipy.interpolate import interp1d


sr, y = wav.read("../../data/stereo-blauen1.wav")


sz = len(y)

ly = y.T[0][0:sz]
ry = y.T[1][0:sz]


x = np.linspace(0, 10000, sz)

print(len(x), len(ly))

lf = interp1d(x, ly)
rf = interp1d(x, ry)



sr2 = 96000
sy2 = m.floor(sz * sr2/sr)
print(len(y), sy2)
ly2 = np.empty(sz * sr2/sr, np.int16)
print(ly2)
ry2 = np.empty(sz * sr2/sr, np.int16)
print(ry2)
#ly2 = [lf(t) for t in np.linspace(0, 10000, sz * sr2/sr)]
#ry2 = [rf(t) for t in np.linspace(0, 10000, sz * sr2/sr)]

#for i in range(0, len(ly2)):
#	ly2[i] = int(round(float(ly2[i])));
#	ry2[i] = int(round(float(ry2[i])));

domena = np.linspace(0, 10000, sy2)
print(domena)
for i in range(0, sy2):
	ly2[i] = np.int16(round(float(lf(domena[i]))))
	ry2[i] = np.int16(round(float(rf(domena[i]))))
	if (i % 10000 == 0):
		print (i/10000, '/', sy2/10000)

y2 = np.array([ly2,ry2]).T

print(y)

print(y2)

wav.write("./stereo-resampled.wav", sr2, y2)

