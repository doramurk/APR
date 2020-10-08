from BinarniKromosom import BinarniKromosom
from PomicniKromosom import FloatKromosom
from math import ceil, log10, floor
import Funkcije
import random


class Genetski():
    def __init__(self, velicina_populacije, prikaz_rjesenja, vjerojatnost_mutacije, max_broj_evaulacija, dg, gg, f,
                 dimenzije, krizanje, broj_jedinki_u_turniru=3, preciznost=0):
        self.velicina_populacije = velicina_populacije
        self.prikaz_rjesenja = prikaz_rjesenja
        self.vjerojatnost_mutacije = vjerojatnost_mutacije
        self.max_broj_evaluacija = max_broj_evaulacija
        self.dg = dg
        self.gg = gg
        self.broj_jedinki_u_turniru = broj_jedinki_u_turniru
        self.dimenzije = dimenzije
        self.broj_bitova = int(ceil(log10(floor(1 + (gg - dg) * 10**preciznost)) / log10(2)))
        self.f = Funkcije.F(f, self.dg, self.gg, self.broj_bitova)
        self.vrsta_krizanja = krizanje
        self.napravi_mutaciju = ceil(1 / (1 - (1 - vjerojatnost_mutacije)**self.broj_bitova))
        self.counter_mutacija = 0
        self.najbolja_jedinka = BinarniKromosom(self.dimenzije, self.broj_bitova, self.dg, self.gg)

    def start(self):
        populacija = self.stvori_populaciju(self.velicina_populacije)

        while True:
            odabrane_jedinke = self.odaberi_jedinke(populacija)
            dvije_bolje, najgora = self.izbaci_najgoru(odabrane_jedinke)
            nova_jedinka = self.krizanje(dvije_bolje)
            """mutacija = random.uniform(0, 1) < self.vjerojatnost_mutacije
            if mutacija:
                nova_jedinka.mutacija()"""
            nova_jedinka = self.mutiraj(nova_jedinka)
            if self.prikaz_rjesenja == "binarni":
                nova_jedinka.fitness = self.f.bin_fitness(nova_jedinka)
            else:
                nova_jedinka.fitness = self.f.float_fitnesss(nova_jedinka)
            if self.najbolja_jedinka.fitness < nova_jedinka.fitness:
                self.najbolja_jedinka = nova_jedinka
                self.isprintaj_trenutno_stanje()
            populacija.remove(najgora)
            populacija.append(nova_jedinka)
            if self.max_broj_evaluacija != 0:
                if self.f.count >= self.max_broj_evaluacija:
                    break
            else:
                if abs(-1 * self.najbolja_jedinka.fitness) <= 1e-6:
                    break
        return self.najbolja_jedinka

    def stvori_populaciju(self, velicina_populacije):
        populacija = []
        for i in range(velicina_populacije):
            if self.prikaz_rjesenja == 'binarni':
                kromosom = BinarniKromosom(self.dimenzije, self.broj_bitova, self.dg, self.gg)
                kromosom.fitness = self.f.bin_fitness(kromosom)
            else:
                kromosom = FloatKromosom(self.dimenzije, self.dg, self.gg)
                kromosom.fitness = self.f.float_fitnesss(kromosom)
            populacija.append(kromosom)
            if kromosom.fitness > self.najbolja_jedinka.fitness:
                self.najbolja_jedinka = kromosom
        self.isprintaj_trenutno_stanje()
        return populacija

    def odaberi_jedinke(self, populacija):
        odabrane = []
        for i in range(self.broj_jedinki_u_turniru):
            j = random.randint(0, self.velicina_populacije - 1)
            while populacija[j] in odabrane:
                j = random.randint(0, self.velicina_populacije - 1)
            odabrane.append(populacija[j])
        return odabrane

    def izbaci_najgoru(self, jedinke):
        najgora = jedinke[0].fitness
        j = 0
        for i, jedinka in enumerate(jedinke):
            if jedinka.fitness < najgora:
                najgora = jedinka.fitness
                j = i
        najgora = jedinke[j]
        jedinke.remove(jedinke[j])
        return jedinke, najgora

    def krizanje(self, roditelji):
        roditelj1 = roditelji[0]
        roditelj2 = roditelji[1]

        if self.vrsta_krizanja == '1':      # 1 tocka prekida
            dijete1, dijete2 = roditelj1.krizanje_s_jednom_tockom_prekida(roditelj2)
            dijete1.fitness = self.f.bin_fitness(dijete1)
            dijete2.fitness = self.f.bin_fitness(dijete2)
            if dijete1.fitness > dijete2.fitness:
                return dijete1
            else:
                return dijete2

        elif self.vrsta_krizanja == '2':    # uniformno
            dijete = self.uniformno_krizanje(roditelj1, roditelj2)
            return dijete

        elif self.vrsta_krizanja == '3':    # aritmeticko
            dijete = roditelj1.aritmeticko_krizanje(roditelj2)
            return dijete

        elif self.vrsta_krizanja == '4':    # heuristicko
            dijete = roditelj1.heuristicko_krizanje(roditelj2)
            return dijete

    def uniformno_krizanje(self, roditelj1, roditelj2):
        dijete_varijable = []
        random = BinarniKromosom(roditelj1.dimenzije, roditelj1.broj_bitova, roditelj1.dg, roditelj1.gg)
        for var1, var2, var3 in zip(roditelj1.varijable, roditelj2.varijable, random.varijable):
            dijete_varijable.append(var1 & var2 | var3 & (var1 ^ var2))
        random.varijable = dijete_varijable
        return random

    def nadi_najbolju_jedinku(self, populacija):
        najbolja = populacija[0].fitness
        j = 0
        for i, jedinka in enumerate(populacija):
            if jedinka.fitness < najbolja:
                najbolja = jedinka.fitness
                j = i
        return populacija[j]

    def mutiraj(self, kromosom):
        self.counter_mutacija += 1
        if self.counter_mutacija == self.napravi_mutaciju:
            self.counter_mutacija = 0
            kromosom = kromosom.mutacija()
        return kromosom

    def isprintaj_trenutno_stanje(self):
        print("Broj iteracija: " + str(self.f.count))
        if self.prikaz_rjesenja == 'binarni':
            print("Trenutna najbolja jedinka: ", end='')
            lista = []
            for var in self.najbolja_jedinka.varijable:
                lista.append(self.dg + (var / (2**self.broj_bitova - 1)) * (self.gg - self.dg))
            print(lista)
        else:
            print("Trenutna najbolja jedinka: " + str(self.najbolja_jedinka.varijable))
        print("Vrijednost funkcije: " + str(-1*self.najbolja_jedinka.fitness))
