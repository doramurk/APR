import statistics

from Genetski import Genetski
from Funkcije import f1, f3, f6, f7
from BinarniKromosom import BinarniKromosom
from math import inf
import numpy as np
import matplotlib.pyplot as plt


def prvi():
    print("___________BINARNA_REPREZENTACIJA__________")
    #print("F1")
    #GA = Genetski(10000, 'binarni', 0.05, 0, -50, 150, f1, 2, '2', 3, 3)
    #GA.start()
    #print("\n\nF3")
    #GA = Genetski(10000, 'binarni', 0.1, 0, -50, 150, f3, 5, '2', 3, 3)
    #GA.start()
    #print("\n\nF6")
    #GA = Genetski(10000, 'binarni', 0.1, 0, -50, 150, f6, 2, '2', 3, 3)
    #GA.start()
    print("\n\nF7")
    GA = Genetski(10000, 'binarni', 0.5, 0, -50, 150, f7, 2, '1', 3, 3)
    GA.start()
    print("\n\n____________FLOAT_REPREZENTACIJA___________")
    #print("F1")
    #GA = Genetski(10000, 'float', 0.3, 0, -50, 150, f1, 2, '3', 3, 3)
    #GA.start()
    #print("\n\nF3")
    #GA = Genetski(10000, 'float', 0.1, 0, -50, 150, f3, 5, '3', 3, 3)
    #GA.start()
    #print("\n\nF6")
    #GA = Genetski(10000, 'float', 0.1, 0, -50, 150, f6, 2, '4', 3, 3)
    #GA.start()
    #print("\n\nF7")
    #GA = Genetski(10000, 'float', 0.1, 0, -50, 150, f7, 2, '4', 3, 3)
    #GA.start()


def drugi():
    for dimenzije in (1, 3, 6, 10):
        print("\n\nF6 - dimenzije = " + str(dimenzije))
        GA = Genetski(10000, 'float', 0.1, 0, -50, 150, f6, dimenzije, '3', 3, 3)
        GA.start()
        #print("\n\nF7 - dimenzije " + str(dimenzije))
        #GA = Genetski(10000, 'float', 0.1, 0, -50, 150, f7, dimenzije, '3', 3, 3)
        #GA.start()


def treci():
    pogodak_binarni = 0
    pogodak_float = 0

    rez_binarni = []
    rez_float = []

    for i in range(10):
        for dimenzije in (3, 6):
            print("\nBinarni f6, dimenzije " + str(dimenzije))
            GA = Genetski(10000, 'binarni', 0.1, 1e5, -50, 150, f6, dimenzije, '2', 3, 4)
            najbolja = GA.start()

            if -1*najbolja.fitness <= 1e-6:
                pogodak_binarni += 1
            rez_binarni.append(najbolja.fitness * -1)

    for i in range(10):
        for dimenzije in (3, 6):
            print("\nBinarni f6, dimenzije " + str(dimenzije))
            GA = Genetski(10000, 'float', 0.1, 1e5, -50, 150, f6, dimenzije, '3', 3, 4)
            najbolja = GA.start()

            if -1 * najbolja.fitness <= 1e-6:
                pogodak_float += 1
            rez_float.append(najbolja.fitness * -1)

    print("Broj pogodaka - binarni: " + str(pogodak_binarni))
    print("Broj pogodaka - float: " + str(pogodak_float))
    print("Medijan - binarni: " + str(statistics.median(rez_binarni)))
    print("Median - float: " + str(statistics.median(rez_float)))


def cetvrti():
    optimalna_velicina = None
    optimalna_mutacija = None
    trenutni_medijan = inf
    najbolja = BinarniKromosom(2, 1, -50, 150)
    rezultati_velicina = []
    rezultati_mutacija = []

    for velicina in (30, 50, 100, 200):
        vrijednosti = []
        for i in range(10):
            GA = Genetski(velicina, 'binarni', 0.1, 1e4, -50, 150, f6, 2, '2', 3, 4)
            trenutna_najbolja = GA.start()
            vrijednosti.append(trenutna_najbolja.fitness)
        medijan = statistics.median(vrijednosti)
        if abs(medijan) < abs(trenutni_medijan):
                trenutni_medijan = medijan
                optimalna_velicina = velicina
        rezultati_velicina.append(vrijednosti)

        fig1, ax1 = plt.subplots(1, 2)
        ax1[0].set_title('Optimalna velicina')
        ax1[0].boxplot(rezultati_velicina)
        plt.show()

        trenutni_medijan = inf
        for mutacija in (0.1, 0.3, 0.6, 0.9):
            vrijednosti = []
            for i in range(10):
                GA = Genetski(optimalna_velicina, 'binarni', mutacija, 1e4, -50, 150, f6, 2, '2', 3, 4)
                trenutna_najbolja = GA.start()
                vrijednosti.append(trenutna_najbolja.fitness)
            medijan = statistics.median(vrijednosti)
            if abs(medijan) < abs(trenutni_medijan):
                trenutni_medijan = medijan
                optimalna_mutacija = mutacija
        rezultati_mutacija.append(vrijednosti)

        fig1, ax1 = plt.subplots(1, 2)
        ax1[0].set_title('Optimalna velicina')
        ax1[0].boxplot(rezultati_velicina)
        ax1[1].set_title('Optimalna mutacija')
        ax1[1].boxplot(rezultati_mutacija)
        plt.show()


def peti():
    GA = Genetski(10000, 'binarni', 0.1, 1e5, -50, 150, f6, 2, '2', 3, 3)
    GA.start()
    print("_______________")
    GA = Genetski(10000, 'binarni', 0.1, 1e5, -50, 150, f6, 2, '2', 10, 3)
    GA.start()


#prvi()
#drugi()
#treci()
cetvrti()
#peti()
