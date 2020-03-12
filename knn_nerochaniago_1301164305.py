from random import random
import pandas as nero
import math

dataset = nero.read_csv('DataTrain_Tugas3_AI.csv')
datatest = nero.read_csv('DataTest_Tugas3_AI.csv')

train = dataset.values.tolist()
testing = datatest.values.tolist()
data_hasil = []
kelas = []
hasil = []

nol = 0
satu = 0
dua = 0
tiga = 0

for i in range(1,200):
    for x in range(1,800):
        hasil.append(math.sqrt(pow((testing[i][1] - train[x][1]), 2) + pow((testing[i][2] - train[x][2]), 2) + pow((testing[i][3] - train[x][3]), 2) + pow((testing[i][4] - train[x][4]), 2) + pow((testing[i][5] - train[x][5]), 2)))
        hasil.append(train[x][6])
        data_hasil.append(hasil)
        data_hasil.append(hasil)

    for z in range(0,11):
        if data_hasil[z][0] == 0:
            nol += 1
        elif data_hasil[z][0] == 1:
            satu += 1
        elif data_hasil[z][0] == 2:
            dua += 1
        elif data_hasil[z][0] == 3:
            tiga += 1

    if nol > satu and nol > dua and nol > tiga:
        kelas.append(int(0))
    elif satu > nol and satu > dua and satu > tiga:
        kelas.append(int(1))
    elif dua > nol and dua > satu and dua > tiga:
        kelas.append(int(2))
    elif tiga > nol and tiga > satu and tiga > dua:
        kelas.append(int(3))
    elif satu >= nol :
        kelas.append(random.randint(0, 1))
    elif dua > nol and dua >= satu:
        kelas.append(random.randint(1, 2))
    elif tiga > nol and tiga >= satu and tiga >= dua:
        kelas.append(random.randint(1, 3))
    else:
        kelas.append(random.randint(0, 3))
    print(kelas)
