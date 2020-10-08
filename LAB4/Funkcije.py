import math
from math import sin


class F():
    def __init__(self, f, dg, gg, broj_bitova):
        self.f = f
        self.dg = dg
        self.gg = gg
        self.broj_bitova = broj_bitova
        self.count = 0

    def float_fitnesss(self, kromosom):
        self.count = self.count + 1
        return -1 * self.f(kromosom.varijable)

    def bin_fitness(self, kromosom):
        self.count = self.count + 1
        float_varijable = []
        for var in kromosom.varijable:
            float_varijable.append(self.dg + (var / (2**self.broj_bitova - 1)) * (self.gg - self.dg))
        return -1 * self.f(float_varijable)


def f1(x):
    return pow(100 * (x[1] - x[0] ** 2), 2) + pow((1 - x[0]), 2)


def f3(x):
    sum = 0
    for i, xi in enumerate(x):
        sum += pow((xi - i + 1), 2)
    return sum


def f6(x):
    sum = 0
    for xi in x:
        sum += pow(xi, 2)
    return 0.5 + (pow(sin(math.sqrt(sum)), 2) - 0.5) / (pow((1 + 0.001 * sum), 2))


def f7(x):
    sum = 0
    for xi in x:
        sum += pow(xi, 2)

    return (pow(sum, 0.25)) * (1 + pow(sin(50 * pow(sum, 0.1)), 2))
