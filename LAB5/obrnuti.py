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


def obrnuti(t0, tf, T, n, xt0, A, B, citaj=False, r=None):
    if citaj:
        A, B, xt0 = citaj_iz_datoteke()

    x = []
    x.append(xt0)

    P = np.linalg.inv(np.eye(2) - np.dot(A, T))
    Q = np.dot(np.dot(P, T), B)

    ts = np.linspace(t0, tf, n+1)
    for k, t in enumerate(ts):
        if r:
            x.append(list(np.dot(P, x[k]) + np.dot(Q, r(t+T))))
        else:
            x.append(list(np.dot(P, x[k])))
    return x


def korektor_call(x_k, x_k1, A, B, T, t, r):
    if r:
        return x_k + T * (np.dot(A, x_k1) + np.dot(B, r(t + T)))
    else:
        return x_k + T * (np.dot(A, x_k1))
