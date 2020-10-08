import copy
import random


def max_idx(f, simpleksi):
    _fsimplex = []
    for x in simpleksi:
        _fsimplex.append(f(x))
    max = _fsimplex[0]
    max2 = _fsimplex[0]
    h, h2 = 0, 0
    for i, fx in enumerate(_fsimplex):
        if fx > max:
            h = i
    del _fsimplex[h]
    for j, fx in enumerate(_fsimplex):
        if fx > max2:
            h2 = j

    return h, h2


def centroid(simpleksi, h=None):
    xc = [0] * len(simpleksi[0])
    for i in range(len(simpleksi[0])):
        suma = 0
        for j, simpleks in enumerate(simpleksi):
            if j != h:
                suma += simpleks[i]
        if h is None:
            xc[i] += suma / (len(simpleksi))
        else:
            xc[i] += suma / (len(simpleksi) - 1)
    return xc


def refleksija(xc, xh, alfa):
    xr = [0] * len(xc)
    for i in range(len(xc)):
        xr[i] = (1 + alfa) * xc[i] - alfa * xh[i]
    return xr


def zadovoljava_implicitna(x0, implicitna):
    for impl in implicitna:
        if impl(x0) < 0:
            return False
    return True


def box(f, pocetna_tocka=None, implicitna=None, xd=-100, xg=100, e=10e-6, alpha=1.3):
    x0 = copy.deepcopy(pocetna_tocka)
    for x in x0:
        if x > xg or x < xd:
            print("Netocno zadana pocetna tocka.")
            return
    if not zadovoljava_implicitna(pocetna_tocka, implicitna):
        print("Netocno zadana pocetna tocka.")
        return
    xc = copy.deepcopy(x0)
    simpleksi = []
    simpleksi.append(xc)
    for t in range(2 * len(x0)):
        x = [0] * len(x0)
        for i in range(len(x0)):
            #r = random.random()
            r = random.uniform(0, 1)
            x[i] = xd + r * (xg - xd)
        while not zadovoljava_implicitna(x, implicitna):
            for i, xi in enumerate(x):
                x[i] = 0.5 * (xi + xc[i])
        simpleksi.append(x)
        xc = centroid(simpleksi)

    br_it = 0
    f_prije = f(xc)
    f_sad = f_prije

    while True:
        if br_it > 100:
            print("Postupak ne konvergira.")
            return xc
        if f_prije == f_sad:
            br_it += 1
        else:
            br_it = 0
        h, h2 = max_idx(f, simpleksi)
        xc = centroid(simpleksi, h)
        xr = refleksija(xc, simpleksi[h], alpha)
        for i in range(len(x0)):
            if xr[i] < xd:
                xr[i] = xd
            elif xr[i] > xg:
                xr[i] = xg
        while not zadovoljava_implicitna(xr, implicitna):
            for i, x in enumerate(xr):
                xr[i] = 0.5 * (xr[i] + xc[i])
        if f(xr) > f(simpleksi[h2]):
            for i, x in enumerate(xr):
                xr[i] = 0.5 * (xr[i] + xc[i])
        simpleksi[h] = xr

        suma = 0
        for sim in simpleksi:
            suma += pow((f(sim) - f(xc)), 2)
        uvjet = pow(suma/len(simpleksi), 1./2)
        if uvjet <= e:
            return xc
