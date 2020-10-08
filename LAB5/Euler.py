import numpy as np


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


def euler(t0, tf, T, n, xt0, A, B, citaj=False, r=None):
    if citaj:
        A, B, xt0 = citaj_iz_datoteke()
    x = []
    x.append(xt0)

    dx = []
    if r:
        dx.append(np.dot(A, x[0]) + np.dot(B, r(t0)))
    else:
        dx.append(np.dot(A, x[0]))

    ts = np.linspace(t0, tf, n+1)
    for k, t in enumerate(ts):
        x.append(list(x[k] + T*dx[k]))
        if r:
            dx.append(np.dot(A, x[k+1]) + np.dot(B, r(t))) #r(t+T) ? jer dvaput racunam s t0?
        else:
            dx.append(np.dot(A, x[k+1]))
    return x


def predictor_call(x_k, A, B, r, T, t):
    if r:
        return x_k + T*(np.dot(A, x_k) + np.dot(B, r(t+T)))
    else:
        return x_k + T*(np.dot(A, x_k))
