import math
import zlatniRez
import copy


def euklidska_norma(g):
    suma = 0
    for x in g:
        suma += x**2
    return math.sqrt(suma)


def F(f, X, g, lam):
    x = X.copy()
    for idx, xi in enumerate(x):
        x[idx] += lam * g[idx]
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


def gradijentniSpust(f, gradient, pocetna_tocka=None, e=10e-6, zlatni=False, citaj='False'):
    if citaj == 'True':
        pocetna_tocka, e, zlatni = citaj_parametre("gradijentniSpustConf")
    gradient_x = gradient(pocetna_tocka)
    br_it = 0
    x = copy.deepcopy(pocetna_tocka)
    f_sad = f(x)
    f_prije = f_sad
    while euklidska_norma(gradient_x) > e:
        if br_it > 100:
            print("Postupak ne konvergira.")
            break
        #if f_sad == f_prije:
        if abs(f_sad - f_prije) < e:
            br_it += 1
        else:
            br_it = 0
        if zlatni:
            min_lam = zlatniRez.zlatni_rez(lambda lambd: F(f, x, gradient_x, lambd), pocetna_tocka=0)
            for i, xi in enumerate(x):
                x[i] = xi + min_lam * gradient_x[i]
        else:
            for i, xi in enumerate(x):
                x[i] = xi - gradient_x[i]

        f_prije = f_sad
        f_sad = f(x)
        gradient_x = gradient(x)
    return x

