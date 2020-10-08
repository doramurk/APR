import numpy as np

t0 = 0.01
tf = 10
T = 0.01
n = int((tf - t0) / T)


def citaj_iz_datoteke():
    file = open("ulazA", "r")
    lines = file.readlines()
    arrayA = []
    for i, line in enumerate(lines):
        array = []
        array.append(int(line.split()[0]))
        array.append(int(line.split()[1]))
        arrayA.append(array)
    file.close()
    file = open("ulazB", "r")
    lines = file.readlines()
    arrayB = []
    for i, line in enumerate(lines):
        array = []
        array.append(int(line.split()[0]))
        array.append(int(line.split()[1]))
        arrayB.append(array)
    file.close()
    file = open("ulaz_pocetni", "r")
    lines = file.readlines()
    array_pocetni = []
    for i, line in enumerate(lines):
        array_pocetni.append(int(line))
    file.close()
    return arrayA, arrayB, array_pocetni


def PECE(t0, tf, T, n, xt0, A, B, prediktor, korektor, broj_it, citaj=False, r=None):
    if citaj:
        A, B, xt0 = citaj_iz_datoteke()
    x = []
    x.append(xt0)
    for k, t in enumerate(np.linspace(t0, tf, n + 1)):
        x_procjena = prediktor.predictor_call(x[k], A, B, r, T, t)
        for i in range(broj_it):
            x_novaprocjena = korektor.korektor_call(x[k], x_procjena, A, B, T, t, r)
            x_procjena = x_novaprocjena
        x.append(x_procjena)
    return x


