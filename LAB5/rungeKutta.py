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


def rungeKutta(t0, tf, T, n, xt0, A, B, citaj=False, r=None):
    if citaj:
        A, B, xt0 = citaj_iz_datoteke()

    x = []
    x.append(xt0)

    ts = np.linspace(t0, tf, n + 1)
    for k, t in enumerate(ts):
        if r:
            m1 = np.dot(A, x[k]) + np.dot(B, r(t))
            m2 = np.dot(A, x[k] + T/2 * m1) + np.dot(B, r(t + T/2))
            m3 = np.dot(A, x[k] + T/2 * m2) + np.dot(B, r(t + T/2))
            m4 =  np.dot(A, x[k] + T * m3) + np.dot(B, r(t + T))
        else:
            m1 = np.dot(A, x[k])
            m2 = np.dot(A, x[k] + T/2 * m1)
            m3 = np.dot(A, x[k] + T/2 * m2)
            m4 =  np.dot(A, x[k] + T * m3)

        x. append(x[k] + T/6 * (m1 + 2*m2 + 2*m3 + m4))

    return x
