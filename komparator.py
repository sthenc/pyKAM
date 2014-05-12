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

import numpy as np
import scipy.io as so

def compute_stats(matx, name):
    print (name, ' statistics: ')
    print ('mean = ', matx.mean())
    print ('min = ', matx.min())
    print ('max = ', matx.max())
    print ('std = ', matx.std())
    
    

orig = so.loadmat("D:\\Fer\\diplomski\\spektar\\KAM\\matKAM\\test-orig\\britney-short0-stft.mat")

revs = so.loadmat("D:\\Fer\\diplomski\\spektar\\KAM\\pyKAM\\test-revs\\britney-short0-stft.mat")

# first check dimensions
if orig['stft'].shape != revs['stft'].shape:
    print ('matrix has wrong dimensions')
    print (' original> ', orig['stft'].shape)
    print (' reversed> ', revs['stft'].shape)
    exit()

# compute the matrix with errors
diff = dict()
diff['stft'] = orig['stft'] - revs['stft']

compute_stats(orig['stft'], 'orig')
compute_stats(revs['stft'], 'revs')
compute_stats(diff['stft'], 'diff')
