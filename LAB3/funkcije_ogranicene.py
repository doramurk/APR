import math


class funkcija_ogranicena:
    def __init__(self, f, x0, t, implicitna_nejednadzbe=None, implicitna_jednadzbe=None):
        self.f = f
        self.x0 = x0
        self.implicitna_nejednadzbe = implicitna_nejednadzbe
        self.implicitna_jednadzbe = implicitna_jednadzbe
        self.t = t
        self.br_it = 0

    def call(self, x):
        self.br_it += 1
        jednadzbe = 0
        if self.implicitna_jednadzbe is not None:
            for impl in self.implicitna_jednadzbe:
                jednadzbe += self.t * impl(x)**2

        nejednadzbe = 0
        for impl in self.implicitna_nejednadzbe:
            if impl(x) <= 0:
                return float("inf")
            else:
                nejednadzbe += math.log(impl(x))

        nejednadzbe *= -(1 / self.t)
        return self.f(x) + nejednadzbe + jednadzbe
