import pandas as nero
import math
import random
import numpy

dataset = nero.read_csv('DataTrain_Tugas3_AI.csv')
datatest = nero.read_csv('DataTest_Tugas3_AI.csv')

train = dataset.values.tolist()
testing = datatest.values.tolist()
data_hasil = numpy.zeros((800,2))
kelas = numpy.zeros(200)


nol = 0
satu = 0
dua = 0
tiga = 0

for i in range(0,len(testing)):
	for x in range(0,len(train)):
		data_hasil[x][0] = math.sqrt(pow((testing[i][1] - train[x][1]), 2) + pow((testing[i][2] - train[x][2]), 2) + pow((testing[i][3] - train[x][3]), 2) + pow((testing[i][4] - train[x][4]), 2) + pow((testing[i][5] - train[x][5]), 2))
		data_hasil[x][1] = train[x][6]

	numpy.sort(data_hasil)

	for z in range(0,12):
		if data_hasil[z][1] == 0:
			nol += 1
		elif data_hasil[z][1] == 1:
			satu += 1
		elif data_hasil[z][1] == 2:
			dua += 1
		else:
			tiga += 1

	if nol > satu and nol > dua and nol > tiga:
		kelas[i] = '0'
	elif satu > nol and satu > dua and satu > tiga:
		kelas[i] = '1'
	elif dua > nol and dua > satu and dua > tiga:
		kelas[i] = '2'
	elif tiga > nol and tiga > satu and tiga > dua:
		kelas[i] = '3'
	elif satu >= nol:
		kelas[i] = random(0,1)
	elif dua > nol and dua >= satu:
		kelas[i] = random(1,2)
	elif tiga > nol and tiga >= satu and tiga >= dua:
		kelas[i] = random(1,3)
	else:
		kelas[i] = random(0,3)

