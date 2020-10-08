import numpy as np
''' ##### NELDERMEAD #####
Algoritam simpleks postupka po Nelderu i Meadu
// Ulazne velicine: X0, alfa, beta, gama, epsilon
'''

def min_max_idx(fsimpleks):
    max = fsimpleks[0]
    min = fsimpleks[0]
    h = 0
    l = 0

    for i, f in enumerate(fsimpleks):
        if f > max:
            max = f
            h = i
        if f < min:
            min = f
            l = i
    return h, l


def centroid(simpleksi, h):
    xc = [0] * len(simpleksi[0])
    for i in range(len(simpleksi[0])):
        suma = 0
        for j, simpleks in enumerate(simpleksi):
            if j != h:
                suma += simpleks[i]
        xc[i] += suma / (len(simpleksi) - 1)
    return xc


def refleksija(xc, xh, alfa):
    xr = [0] * len(xc)
    for i in range(len(xc)):
        xr[i] = (1 + alfa) * xc[i] - alfa * xh[i]
    return xr


def ekspanzija(xc, xr, gamma):
    xe = [0] * len(xc)
    for i in range(len(xc)):
        xe[i] = (1 - gamma) * xc[i] + gamma * xr[i]
    return xe


def kontrakcija(xc, xh, beta):
    xk = [0] * len(xc)
    for i in range(len(xc)):
        xk[i] = (1 - beta) * xc[i] + beta * xh[i]
    return xk


def f_xr_veci_od_svih_osim_f_xh(fxr, h, fsimpleks):
    for i, fsim in enumerate(fsimpleks):
        if i != h:
            if fxr < fsim:
                return False
    return True


def citaj(ime):
    x0 = []
    dat = open(ime, "r")
    korak = float(dat.readline())
    alfa = float(dat.readline())
    beta = float(dat.readline())
    gamma = float(dat.readline())
    sigma = float(dat.readline())
    e = float(dat.readline())
    line = dat.readline()
    for x in line.split(","):
        x0.append(float(x))
    return x0, korak, alfa, beta, gamma, sigma, e


def nelder_mead(f, citaj_tocku=False,  pocetna_tocka=None, korak=1, alfa=1, beta=0.5, gamma=2, sigma=0.5, e=10e-6):
    if pocetna_tocka is None and korak is None and alfa is None and beta is None and gamma is None and sigma is None and e is None:
        pocetna_tocka, korak, alfa, beta, gamma, sigma, e = citaj("Simpleks")
    if citaj_tocku == 'True':
        pocetna_tocka, korak, alfa, beta, gamma, sigma, e = citaj("Simpleks")

    simpleksi = []
    simpleksi.append(np.array(pocetna_tocka))
    for i in range(len(pocetna_tocka)):
        new_simpleks = pocetna_tocka.copy()
        new_simpleks[i] += korak
        simpleksi.append(new_simpleks)

    #print("    xc        f(xc)    ")

    while True:
        fsimpleks = []
        for simpleks in simpleksi:
            fsimpleks.append(f(simpleks))

        h, l = min_max_idx(fsimpleks)
        xh = simpleksi[h]
        xl = simpleksi[l]
        xc = centroid(simpleksi, h)
        fxc = f(xc)
        #print("a={a}    b={b}".format(a=str(xc), b=str(fxc)))
        xr = refleksija(xc, xh, alfa)

        fxr = f(xr)
        if fxr < fsimpleks[l]:
            xe = ekspanzija(xc, xr, gamma)
            if f(xe) < fsimpleks[l]:
                simpleksi[h] = xe
                xh = xe
                fsimpleks[h] = f(simpleksi[h])
            else:
                simpleksi[h] = xr
                xh = xr
                fsimpleks[h] = f(simpleksi[h])
        else:
            if f_xr_veci_od_svih_osim_f_xh(fxr, h, fsimpleks):
                if fxr < fsimpleks[h]:
                    simpleksi[h] = xr
                    xh = xr
                    fsimpleks[h] = f(simpleksi[h])
                xk = kontrakcija(xc, xh, beta)
                if f(xk) < fsimpleks[h]:
                    simpleksi[h] = xk
                    xh = xk
                    fsimpleks[h] = f(simpleksi[h])
                else:
                    #pomakni sve prema xl
                    for i, simpleks in enumerate(simpleksi):
                        for j in range(len(simpleks)):
                            if i != l:
                                simpleks[j] = (simpleks[j] + xl[j]) * sigma

                    for simpleks in simpleksi:
                        fsimpleks.append(f(simpleks))
            else:
                simpleksi[h] = xr
                xh = xr
                fsimpleks[h] = f(simpleksi[h])
        suma = 0
        for fsim in fsimpleks:
            suma += pow((fsim - fxc), 2)
        uvjet = pow(suma/len(simpleksi), 1./2)
        if uvjet <= e:
            return xc


