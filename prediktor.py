#!/usr/bin/python
#
# stjepan.henc@fer.hr
# 25.11.2013
#
import wave, struct, math, sys, time

import matplotlib.pylab as pl

import scipy
import scipy.fftpack
import pylab
import scipy.stats
import numpy



#audio = wave.open("ispitivanje.wav", mode="r")
audio = wave.open("smallest.wav", mode="r")

length = audio.getnframes()

sample_rate = audio.getframerate()


desni = [0] * length
proba = [0] * length



# read & preprocess the data from the file
for i in range(0, length):
	
	data = audio.readframes(1)
	tmp = struct.unpack("<hh", data)
	#ljevi[i] = tmp[0]
	desni[i] = tmp[1]


stanje = False # je li zvucno ili tiho
brojaci = []

tisina_int = []
zvuk_int = []


last = 0
#for k in range (5, 20):
treshold = 20
frame = 50	 	# dobiveni brute-force optimizacijom
		
brojac = 0

for i in range(frame, length):

	bul = True

	for j in range(0, frame - 1):

		if abs(desni[i - j]) > treshold: 
			bul = False
	

	if bul == True and stanje == False: # onda treba promijeniti stanje
		stanje = True
		proba[i - frame] = 32000
		brojac = brojac + 1
		tisina_int.append(1.0 * (i - frame - last) / sample_rate)
		last = i - frame

	if bul == False and stanje == True: # onda treba promijeniti stanje
		stanje = False
		proba[i] = -32000
		brojac = brojac + 1
		zvuk_int.append(1.0 * (i - last) / sample_rate)
		last = i

brojaci.append(brojac)
		
audio.close()

print(brojac)

#arr = numpy.array([tisina_int, zvuk_int])

tisina_sred = numpy.mean(tisina_int)
print(tisina_sred)

tisina_dev = numpy.std(tisina_int)
print(tisina_dev)


zvuk_sred = numpy.mean(zvuk_int)
print(zvuk_sred)

zvuk_dev = numpy.std(zvuk_int)
print(zvuk_dev)


brojevi = pl.linspace(5, 19, 15) 
time = pl.linspace(1, length, length)

pl.subplot(211)
pl.plot(time, desni)
pl.subplot(212)
pl.plot(time, proba)

pl.show()

#TODO
# odvajanje intervala
# aproksimacija sinusoide


