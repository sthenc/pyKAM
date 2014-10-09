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

import sys
import numpy as np

#sys.path.insert(0, '..\\')

#print(sys.path)

from Signal import Signal

import unittest

class TestSignal(unittest.TestCase):

    def setUp(self):
        self.sig = Signal('./data/britney-short0.wav')

    def test_precision(self):
        self.sig.precision = 32
        
        self.assertEqual(type(self.sig.s[0][0]), type(np.complex64(1.0)));
        
		
        self.sig.precision = 64
        self.assertEqual(type(self.sig.S[0][0][0]), type(np.complex128(1.0)));

if __name__ == "__main__":
    unittest.main()

