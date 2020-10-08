import copy
import LUP
import math
import zlatniRez


def euklidska_norma(g):
    suma = 0
    for x in g:
        suma += x**2
    return math.sqrt(suma)


def F(f, X0, dx, lam):
    x = X0.copy()
    for idx, xi in enumerate(x):
        x[idx] += lam * dx[idx]
    return f(x)


def citaj_parametre(ime):
    dat = open(ime, "r")
    e = float(dat.readline())
    line = dat.readline()
    x1 = float(line.split()[0])
    x2 = float(line.split()[1])
    line = dat.readline()
    if line == "True":
        zlatni = True
    else:
        zlatni = False
    return [x1, x2], e, zlatni


def newtonRaphson(f, gradient, hesseova, pocetna_tocka, citaj=False, zlatni=False, e=10e-6):
    if citaj == 'True':
        x0, e, zlatni = citaj_parametre("gradijentniSpustConf")
    x0 = copy.deepcopy(pocetna_tocka)
    br_it = 0
    f_sad = f(x0)
    f_prije = f_sad

    dx = [1] * len(x0)

    gradient_x = gradient(x0)
    hesseova_x = hesseova(x0)

    dx = LUP.izracunajX_LUP(hesseova_x, gradient_x)

    while euklidska_norma(dx) > e:
        if br_it > 100:
            print("divergira!")
            break
        if f_sad == f_prije:
            br_it += 1
        else:
            br_it = 0
        if zlatni:
            min_lam = zlatniRez.zlatni_rez(lambda lambd: F(f, x0, dx, lambd), pocetna_tocka=0)
            for i, xi in enumerate(x0):
                x0[i] = xi + min_lam * dx[i]
        else:
            for i, xi in enumerate(x0):
                x0[i] = xi - dx[i]

        f_prije = f_sad
        f_sad = f(x0)

        gradient_x = gradient(x0)
        hesseova_x = hesseova(x0)

        dx = LUP.izracunajX_LUP(hesseova_x, gradient_x)
    return x0
