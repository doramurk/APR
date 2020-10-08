class funkcija_G():
    def __init__(self, ogranicenja, x0, t):
        self.ogranicenja = ogranicenja
        self.x0 = x0
        self.t = t
        self.br_it = 0

    def call(self, x):
        self.br_it += 1
        G = 0
        for gi in self.ogranicenja:
            if gi(x) < 0:
                G -= self.t * gi(x)
        return G
