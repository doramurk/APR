from math import inf
import random


class FloatKromosom():
    def __init__(self, dimenzije, dg, gg):
        self.dimenzije = dimenzije
        self.dg = dg
        self.gg = gg
        self.fitness = -inf
        self.varijable = []
        for i in range(dimenzije):
            self.varijable.append(random.uniform(self.dg, self.gg))

    def aritmeticko_krizanje(self, roditelj2):
        a = random.uniform(0, 1)
        dijete_varijable = []
        for var1, var2 in zip(self.varijable, roditelj2.varijable):
            dijete_varijable.append(var1 * a + (1 - a) * var2)
        dijete = FloatKromosom(self.dimenzije, self.dg, self.gg)
        dijete.varijable = dijete_varijable
        return dijete

    def heuristicko_krizanje(self, roditelj2):
        a = random.uniform(0, 1)
        dijete_varijable = []
        bolji_roditelj, losiji_roditelj = self.pronadi_boljeg(roditelj2)
        for var1, var2 in zip(losiji_roditelj.varijable, bolji_roditelj.varijable):
            d = a * (var2 - var1) + var2
            while d<self.dg or d>self.gg:
                a = random.uniform(0, 1)
                d = a * (var2 - var1) + var2
            dijete_varijable.append(d)
        dijete = FloatKromosom(self.dimenzije, self.dg, self.gg)
        dijete.varijable = dijete_varijable
        return dijete

    def pronadi_boljeg(self, roditelj2):
        if self.fitness > roditelj2.fitness:
            return self, roditelj2
        else:
            return roditelj2, self

    def mutacija(self):
        nove_varijable = []
        for var in self.varijable:
            novi = random.uniform(self.dg, self.gg)
            nove_varijable.append(novi)
        self.varijable = nove_varijable
        return self
