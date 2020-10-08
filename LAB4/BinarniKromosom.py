from math import inf
import random


class BinarniKromosom():
    def __init__(self, dimenzije, broj_bitova, dg, gg):
        self.dimenzije = dimenzije
        self.broj_bitova = broj_bitova
        self.dg = dg
        self.gg = gg
        self.fitness = -inf
        self.varijable = []
        for i in range(dimenzije):
            self.varijable.append(random.getrandbits(broj_bitova))

    def krizanje_s_jednom_tockom_prekida(self, rod2):
        dijete11 = []
        dijete21 = []
        for var1, var2 in zip(self.varijable, rod2.varijable):
            b1 = "{0:b}".format(var1)
            b2 = "{0:b}".format(var2)
            b1 = '0'*(self.broj_bitova - len(b1)) + b1
            b2 = '0'*(self.broj_bitova - len(b2)) + b2

            k = random.randint(0, self.broj_bitova)

            d1 = b1[0:k] + b2[k:self.broj_bitova]
            d2 = b2[0:k] + b1[k:self.broj_bitova]

            d1 = int(d1, 2)
            d2 = int(d2, 2)

            dijete11.append(d1)
            dijete21.append(d2)
        dijete1 = BinarniKromosom(self.dimenzije, self.broj_bitova, self.dg, self.gg)
        dijete1.varijable = dijete11
        dijete2 = BinarniKromosom(self.dimenzije, self.broj_bitova, self.dg, self.gg)
        dijete2.varijable = dijete21

        return dijete1, dijete2

    def mutacija(self):
        index = random.randint(0, self.broj_bitova - 1)
        m = 2**index
        nove = []
        for var in self.varijable:
            nove.append(var ^ m)
        self.varijable = nove
        return self
