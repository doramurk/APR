import Euler
import obrnuti
import trapezni
import rungeKutta
import predKor
import numpy as np
import math
import matplotlib.pyplot as plt

# PRVI
#t0 = 0.01
#tf = 10
#T = 0.01

# DRUGI
#t0 = 0.1
#tf = 1
#T = 0.1


def citaj_pocetne_uvjete(ime):
    file = open(ime, "r")
    lines = file.readlines()
    t0 = float(lines[0])
    tf = float(lines[1])
    T = float(lines[2])
    broj_iteracija_za_ispis = int(lines[3])

    n = int((tf - t0) / T)
    return t0, tf, T, n, broj_iteracija_za_ispis


def analiticki_1(t0, tf, n):
    ts = np.linspace(t0, tf, n+1)
    x = []
    # x.append([1, 1])

    for k, t in enumerate(ts):
        x.append([1 * math.cos(t) + 1 * math.sin(t), 1 * math.cos(t) - 1 * math.sin(t)])
    return x


def crtaj(t0, tf, n, x, title):
    x.pop(0)
    t = np.linspace(t0, tf, n+1)
    for i, redak in enumerate(np.transpose(x)):
        plt.plot(t, redak, label='x' + str(i+1))
    plt.legend()
    plt.title(title)
    plt.grid()
    plt.show()


def prvi(citaj):
    xt0 = [1, 1]
    A = [[0, 1], [-1, 0]]
    B = [[0, 0], [0, 0]]

    t0, tf, T, n, broj_iteracija_za_ispis = citaj_pocetne_uvjete("pocetni_uvjeti")

    analiticki = analiticki_1(t0, tf, n)

    print("Euler")
    x_euler = Euler.euler(t0, tf, T, n, xt0, A, B, citaj, None)
    for i in range(int(n / broj_iteracija_za_ispis) + 1):
        print(x_euler[i * broj_iteracija_za_ispis + 1])

    crtaj(t0, tf, n, x_euler, "euler")

    suma = 0
    for (analiticki_rez, dobiveni_rez) in zip(analiticki, x_euler):
        suma += abs(analiticki_rez[0] - dobiveni_rez[0]) + abs(analiticki_rez[1] - dobiveni_rez[1])
    print("Razlika Euler: " + str(suma))
    print("__________________________________________________________________________________")

    print("Obrnuti Euler")
    x_obrnuti = obrnuti.obrnuti(t0, tf, T, n, xt0, A, B, citaj, None)
    for i in range(int(n / broj_iteracija_za_ispis) + 1):
        print(x_obrnuti[i * broj_iteracija_za_ispis + 1])

    crtaj(t0, tf, n, x_obrnuti, "obrnuti euler")

    suma = 0
    for (analiticki_rez, dobiveni_rez) in zip(analiticki, x_obrnuti):
        suma += abs(analiticki_rez[0] - dobiveni_rez[0]) + abs(analiticki_rez[1] - dobiveni_rez[1])
    print("Razlika obrnuti Euler: " + str(suma))
    print("__________________________________________________________________________________")


    print("Trapezni")
    x_trapezni = trapezni.trapezni(t0, tf, T, n, xt0, A, B, citaj, None)
    for i in range(int(n / broj_iteracija_za_ispis) + 1):
        print(x_trapezni[i * broj_iteracija_za_ispis + 1])

    crtaj(t0, tf, n, x_trapezni, "trapezni")

    suma = 0
    for (analiticki_rez, dobiveni_rez) in zip(analiticki, x_trapezni):
        suma += abs(analiticki_rez[0] - dobiveni_rez[0]) + abs(analiticki_rez[1] - dobiveni_rez[1])
    print("Razlika Trapezni: " + str(suma))
    print("__________________________________________________________________________________")


    print("Runge-Kutta 4")
    x_rungeKutta = rungeKutta.rungeKutta(t0, tf, T, n, xt0, A, B, citaj)
    for i in range(int(n / broj_iteracija_za_ispis) + 1):
        print(x_rungeKutta[i * broj_iteracija_za_ispis + 1])

    crtaj(t0, tf, n, x_rungeKutta, "Runge-Kutta")

    suma = 0
    for (analiticki_rez, dobiveni_rez) in zip(analiticki, x_rungeKutta):
        suma += abs(analiticki_rez[0] - dobiveni_rez[0]) + abs(analiticki_rez[1] - dobiveni_rez[1])
    print("Razlika RungeKutta4: " + str(suma))
    print("__________________________________________________________________________________")


    print("PECE")
    x_pece = predKor.PECE(t0, tf, T, n, xt0, A, B, Euler, trapezni, 1, citaj)
    for i in range(int(n / broj_iteracija_za_ispis) + 1):
        print(x_pece[i*broj_iteracija_za_ispis + 1])

    crtaj(t0, tf, n, x_pece, "PECE")

    suma = 0
    for (analiticki_rez, dobiveni_rez) in zip(analiticki, x_pece):
        suma += abs(analiticki_rez[0] - dobiveni_rez[0]) + abs(analiticki_rez[1] - dobiveni_rez[1])
    print("Razlika PECE: " + str(suma))
    print("__________________________________________________________________________________")


    print("PECE2")
    x_pece2 = predKor.PECE(t0, tf, T, n, xt0, A, B, Euler, obrnuti, 2, citaj)
    for i in range(int(n / broj_iteracija_za_ispis) + 1):
        print(x_pece2[i*broj_iteracija_za_ispis + 1])

    crtaj(t0, tf, n, x_pece2, "PECE2")

    suma = 0
    for (analiticki_rez, dobiveni_rez) in zip(analiticki, x_pece2):
        suma += abs(analiticki_rez[0] - dobiveni_rez[0]) + abs(analiticki_rez[1] - dobiveni_rez[1])
    print("Razlika PECE2: " + str(suma))
    print("__________________________________________________________________________________")


def drugi(citaj):
    xt0 = [1, -2]
    A = [[0, 1], [-200, -102]]
    B = [[0, 0], [0, 0]]

    t0, tf, T, n, broj_iteracija_za_ispis = citaj_pocetne_uvjete("pocetni_uvjeti_2")

    print("Euler")
    x_euler = Euler.euler(t0, tf, T, n, xt0, A, B, citaj, None)
    for i in range(int(n/broj_iteracija_za_ispis) + 1):
        print(x_euler[i*broj_iteracija_za_ispis + 1])

    crtaj(t0, tf, n, x_euler, "euler")
    print("__________________________________________________________________________________")

    print("Obrnuti Euler")
    x_obrnuti = obrnuti.obrnuti(t0, tf, T, n, xt0, A, B, citaj)
    for i in range(int(n / broj_iteracija_za_ispis) + 1):
        print(x_obrnuti[i * broj_iteracija_za_ispis + 1])

    crtaj(t0, tf, n, x_obrnuti, "obrnuti euler")
    print("__________________________________________________________________________________")

    print("Trapezni")
    x_trapezni = trapezni.trapezni(t0, tf, T, n, xt0, A, B, citaj)
    for i in range(int(n / broj_iteracija_za_ispis) + 1):
        print(x_trapezni[i * broj_iteracija_za_ispis + 1])

    crtaj(t0, tf, n, x_trapezni, "trapezni")

    print("__________________________________________________________________________________")

    print("Runge-Kutta 4")
    x_rungeKutta = rungeKutta.rungeKutta(t0, tf, T, n, xt0, A, B, citaj)
    for i in range(int(n / broj_iteracija_za_ispis) + 1):
        print(x_rungeKutta[i * broj_iteracija_za_ispis + 1])

    crtaj(t0, tf, n, x_rungeKutta, "Runge-Kutta")

    print("__________________________________________________________________________________")

    print("PECE")
    x_pece = predKor.PECE(t0, tf, T, n, xt0, A, B, Euler, trapezni, 1, citaj)
    for i in range(int(n / broj_iteracija_za_ispis) + 1):
        print(x_pece[i * broj_iteracija_za_ispis + 1])

    crtaj(t0, tf, n, x_pece, "PECE")

    print("__________________________________________________________________________________")

    print("PECE2")
    x_pece2 = predKor.PECE(t0, tf, T, n, xt0, A, B, Euler, obrnuti, 2, citaj)
    for i in range(int(n / broj_iteracija_za_ispis) + 1):
        print(x_pece2[i * broj_iteracija_za_ispis + 1])

    crtaj(t0, tf, n, x_pece2, "PECE2")

    print("__________________________________________________________________________________")


def treci(citaj):
    xt0 = [1, 3]
    A = [[0, -2], [1, -3]]
    B = [[2, 0], [0, 3]]
    r = lambda x: np.array([1, 1])

    t0, tf, T, n, broj_iteracija_za_ispis = citaj_pocetne_uvjete("pocetni_uvjeti_3")

    print("Euler")
    x_euler = Euler.euler(t0, tf, T, n, xt0, A, B, citaj, r)
    for i in range(int(n / broj_iteracija_za_ispis) + 1):
        print(x_euler[i * broj_iteracija_za_ispis + 1])
    print(x_euler[n])

    crtaj(t0, tf, n, x_euler, "euler")

    print("__________________________________________________________________________________")

    print("Obrnuti Euler")
    x_obrnuti = obrnuti.obrnuti(t0, tf, T, n, xt0, A, B, citaj, r=r)
    for i in range(int(n / broj_iteracija_za_ispis) + 1):
        print(x_obrnuti[i * broj_iteracija_za_ispis + 1])
    print(x_obrnuti[n])

    crtaj(t0, tf, n, x_obrnuti, "obrnuti euler")

    print("__________________________________________________________________________________")

    print("Trapezni")
    x_trapezni = trapezni.trapezni(t0, tf, T, n, xt0, A, B, citaj, r=r)
    for i in range(int(n / broj_iteracija_za_ispis) + 1):
        print(x_trapezni[i * broj_iteracija_za_ispis + 1])
    print(x_trapezni[n])

    crtaj(t0, tf, n, x_trapezni, "trapezni")

    print("__________________________________________________________________________________")

    print("Runge-Kutta 4")
    x_rungeKutta = rungeKutta.rungeKutta(t0, tf, T, n, xt0, A, B, citaj, r=r)
    for i in range(int(n / broj_iteracija_za_ispis) + 1):
        print(x_rungeKutta[i * broj_iteracija_za_ispis + 1])
    print(x_rungeKutta[n])

    crtaj(t0, tf, n, x_rungeKutta, "Runge-Kutta")

    print("__________________________________________________________________________________")

    print("PECE")
    x_pece = predKor.PECE(t0, tf, T, n, xt0, A, B, Euler, trapezni, 1, citaj, r=r)
    for i in range(int(n / broj_iteracija_za_ispis) + 1):
        print(x_pece[i * broj_iteracija_za_ispis + 1])
    print(x_pece[n])

    crtaj(t0, tf, n, x_pece, "PECE")

    print("__________________________________________________________________________________")

    print("PECE2")
    x_pece2 = predKor.PECE(t0, tf, T, n, xt0, A, B, Euler, obrnuti, 2, citaj, r=r)
    for i in range(int(n / broj_iteracija_za_ispis) + 1):
        print(x_pece2[i * broj_iteracija_za_ispis + 1])
    print(x_pece2[n])

    crtaj(t0, tf, n, x_pece2, "PECE2")

    print("__________________________________________________________________________________")


def cetvrti(citaj):
    xt0 = [-1, 3]
    A = [[1, -5], [1, -7]]
    B = [[5, 0], [0, 3]]
    r = lambda x: np.array([x, x])

    t0, tf, T, n, broj_iteracija_za_ispis = citaj_pocetne_uvjete("pocetni_uvjeti_4")

    print("Euler")
    x_euler = Euler.euler(t0, tf, T, n, xt0, A, B, citaj, r)
    for i in range(int(n / broj_iteracija_za_ispis) + 1):
        print(x_euler[i * broj_iteracija_za_ispis + 1])

    crtaj(t0, tf, n, x_euler, "euler")

    print("__________________________________________________________________________________")

    print("Obrnuti Euler")
    x_obrnuti = obrnuti.obrnuti(t0, tf, T, n, xt0, A, B, citaj, r=r)
    for i in range(int(n / broj_iteracija_za_ispis) + 1):
        print(x_obrnuti[i * broj_iteracija_za_ispis - 1])

    crtaj(t0, tf, n, x_obrnuti, "obrnuti euler")

    print("__________________________________________________________________________________")

    print("Trapezni")
    x_trapezni = trapezni.trapezni(t0, tf, T, n, xt0, A, B, citaj, r=r)
    for i in range(int(n / broj_iteracija_za_ispis) + 1):
        print(x_trapezni[i * broj_iteracija_za_ispis])

    crtaj(t0, tf, n, x_trapezni, "trapezni")

    print("__________________________________________________________________________________")

    print("Runge-Kutta 4")
    x_rungeKutta = rungeKutta.rungeKutta(t0, tf, T, n, xt0, A, B, citaj, r=r)
    for i in range(int(n / broj_iteracija_za_ispis) + 1):
        print(x_rungeKutta[i * broj_iteracija_za_ispis])

    crtaj(t0, tf, n, x_rungeKutta, "Runge-Kutta")

    print("__________________________________________________________________________________")

    print("PECE")
    x_pece = predKor.PECE(t0, tf, T, n, xt0, A, B, Euler, trapezni, 1, citaj, r=r)
    for i in range(int(n / broj_iteracija_za_ispis) + 1):
        print(x_pece[i * broj_iteracija_za_ispis])

    crtaj(t0, tf, n, x_pece, "PECE")

    print("__________________________________________________________________________________")

    print("PECE2")
    x_pece2 = predKor.PECE(t0, tf, T, n, xt0, A, B, Euler, obrnuti, 2, citaj, r=r)
    for i in range(int(n / broj_iteracija_za_ispis) + 1):
        print(x_pece2[i * broj_iteracija_za_ispis - 1])

    crtaj(t0, tf, n, x_pece2, "PECE2")

    print("__________________________________________________________________________________")


#prvi(False)
#drugi(False)
treci(False)
#cetvrti(False)