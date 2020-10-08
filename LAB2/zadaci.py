from zlatniRez import zlatni_rez
from nelder import nelder_mead
from koordinatne1 import koordinatne
from HookeJevees import hooke_jevees
import funkcije
import numpy as np
import random
import sys


def prvi(citaj):
    f = funkcije.f3_1()
    fcall = f.call
    min = zlatni_rez(fcall, citaj,  pocetna_tocka=np.array([10.0]))
    #min = zlatni_rez(fcall)
    print("ZLATNI")
    print("minimum funkcije: {}\nbroj evaluacija: {}".format(min, f.count))
    #print(str(f.call(min)))

    f = funkcije.f3_1()
    fcall = f.call
    print("\nKOORDINATNE")
    min = koordinatne(fcall, citaj, x0=np.array([10.0]))
    #min = koordinatne(fcall)
    print("minimum funkcije: {}\nbroj evaluacija: {}".format(min, f.count))
    #print(str(f.call(min)))

    f = funkcije.f3_1()
    fcall = f.call
    print("\nNELDERMEAD")
    min = nelder_mead(fcall, citaj, pocetna_tocka=np.array([10.0]))
    #min = nelder_mead(fcall, pocetna_tocka=None, alfa=None, beta=None, gamma=None, sigma=None, e=None, korak=None)
    print("minimum funkcije: {}\nbroj evaluacija: {}".format(min, f.count))
    #print(str(f.call(min)))

    f = funkcije.f3_1()
    fcall = f.call
    print("\nHOOKEJEVEES")
    min = hooke_jevees(fcall, citaj, pocetna_tocka=np.array([10.0]))
    #min = hooke_jevees(fcall)
    print("minimum funkcije: {}\nbroj evaluacija: {}".format(min, f.count))


def drugi():
    #print("funkcija   |           koordinatne           |                    simpleks                    |                     hookeJevees                 |")
    #print("___________|_________________________________|________________________________________________|_________________________________________________|")
    for f, x0 in ((funkcije.f1(), np.array([-1.9, 2.0])), (funkcije.f2(), np.array([0.1, 0.3])),
                    (funkcije.f3(), np.array([0.0, 0.0, 0.0, 0.0, 0.0])), (funkcije.f4(), np.array([5.1, 1.1]))):
        #print("\n" + str(f).split(".")[1].split()[0] + "_________|", end="")
        print("\n" + str(f).split(".")[1].split()[0])

        f.count = 0
        fcall = f.call
        print("KOORDINATNE")
        min = koordinatne(fcall, x0=x0)
        print("minimum funkcije: {}\nbroj evaluacija: {}".format(min, f.count))
        #print(str(min) + "_/_" + str(f.count) + "___|", end="")
        # print(str(f.call(min)))
        f.count =0

        fcall = f.call
        print("NELDERMEAD")
        min = nelder_mead(fcall, pocetna_tocka=x0)
        print("minimum funkcije: {}\nbroj evaluacija: {}".format(min, f.count))
        #print(str(min) + "_/_" + str(f.count) + "__|", end="")
        # print(str(f.call(min)))
        f.count =0

        fcall = f.call
        print("HOOKEJEVEES")
        min = hooke_jevees(fcall, pocetna_tocka=x0)
        print("minimum funkcije: {}\nbroj evaluacija: {}".format(min, f.count))
        '''if str(f).split(".")[1].split()[0] == "f4":
            print(str(min) + "_/_" + str(f.count) + "_________|", end="")
        elif str(f).split(".")[1].split()[0] == "f2":
            print(str(min) + "_/_" + str(f.count) + "__________________|", end="")
        else:
            print(str(min) + "_/_" + str(f.count) + "_________________|", end="")
'''
        f.count =0
   #     print("\n___________|_________________________________|________________________________________________|_________________________________________________|")


def treci(citaj):
    f = funkcije.f4()
    fcall = f.call
    print("NELDERMEAD")
    min = nelder_mead(fcall, citaj, pocetna_tocka=np.array([5.0, 5.0]))
    print("minimum funkcije: {}\nbroj evaluacija: {}".format(min, f.count))
    # print(str(f.call(min)))

    f = funkcije.f4()
    fcall = f.call
    print("HOOKEJEVEES")
    min = hooke_jevees(fcall, citaj, pocetna_tocka=np.array([5.0, 5.0]))
    print("minimum funkcije: {}\nbroj evaluacija: {}".format(min, f.count))


def cetvrti(citaj):
    for korak in range(20):
        f = funkcije.f1()
        fcall = f.call
        print("NELDERMEAD")
        min = nelder_mead(fcall, citaj, pocetna_tocka=np.array([0.5, 0.5]), korak=korak + 1)
        print("minimum funkcije: {}\nbroj evaluacija: {}".format(min, f.count))

    print("\n\n")

    for korak in range(20):
        f = funkcije.f1()
        fcall = f.call
        print("NELDERMEAD")
        min = nelder_mead(fcall, citaj, pocetna_tocka=np.array([20.0, 20.0]), korak=korak+1)
        print("minimum funkcije: {}\nbroj evaluacija: {}".format(min, f.count))

    print("\n\n")
        # print(str(f.call(min)))


def peti():
    pronaden = 0
    for i in range(1000):
        x1 = random.randint(-50, 50)
        x2 = random.randint(-50, 50)

        f = funkcije.f6()
        min = hooke_jevees(f.call, pocetna_tocka=np.array([x1, x2]))
        vrijednost_funkcije = f.call(min)
        if vrijednost_funkcije < 10e-4:
            pronaden +=1
    print("Vjerojatnost={}".format(pronaden/1000))


if __name__ == '__main__':
    citaj = sys.argv[1]
    print("________________prvi zadatak______________________")
    prvi(citaj)
    print("_________________drugi zadatak_____________________")
    drugi()
    print("_________________treci zadatak____________________")
    treci(citaj)
    print("________________cetvrti zadatak___________________")
    cetvrti(citaj)
    print("________________peti zadatak______________________")
    peti()
