import zlatniRez
import numpy as np

def F(f, X, i, lambd):
    x = X.copy()
    x[i] = x[i] + lambd
    return f(x)


def citaj(ime):
    x0= []
    dat = open(ime, "r")
    e = float(dat.readline())
    line = dat.readline()
    for x in line.split(","):
        x0.append(float(x))
    return x0, e


def koordinatne(f, citaj_tocku=False, x0=None, e=10e-6):
    if x0 is None or citaj_tocku:
        x_procitan, e = citaj("koordinatneConf")
        x = np.array(x_procitan)
    else:
        x = x0.copy()
    nastavi = True
    while nastavi:
        xs = x.copy()
        for i in range(len(x)):
            #minlam = float(zlatniRez.zlatni_rez(f, pocetna_tocka=x0[i], h=10e-3) - float(x0[i]))
            min_lam = zlatniRez.zlatni_rez(lambda lambd: F(f, x, i, lambd), pocetna_tocka=x[i])
            #print(minlam)
            #x0[i] = float(float(x0[i]) + min_lam)
            x[i] = float(float(x[i]) + min_lam)
            #x = x0
            for i in range(len(x)):
                if abs(x[i] - xs[i]) > e:
                    nastavi = True
                else:
                    nastavi = False
    return x
