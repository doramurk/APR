import math


def f(X):
    return f3().call(X)


class f1():
    def __init__(self):
        self.count = 0

    def call(self, X):
        self.count += 1
        x1 = X[0]
        x2 = X[1]
        return 100 * pow((x2 - pow(x1, 2)), 2) + pow((1 - x1), 2)


class f2():
    def __init__(self):
        self.count = 0

    def call(self, X):
        self.count += 1
        x1 = X[0]
        x2 = X[1]
        return pow((x1 - 4), 2) + 4 * pow((x2 - 2), 2)


class f3():
    def __init__(self):
        self.count = 0

    def call(self, X):
        self.count += 1
        suma = 0
        try:
            for i, x in enumerate(X):
                suma += pow((x - i-1), 2)
        except:
            suma += pow(X, 2)
        return suma


class f3_1():
    def __init__(self):
        self.count = 0

    def call(self, X):
        self.count += 1
        suma = 0
        try:
            for i, x in enumerate(X):
                suma += pow((x - 3), 2)
        except:
            suma += pow(X - 3, 2)
        return suma


class f4():
    def __init__(self):
        self.count = 0

    def call(self, X):
        self.count += 1
        x1 = X[0]
        x2 = X[1]
        return abs((x1 - x2) * (x1 + x2)) + pow((pow(x1, 2) + pow(x2, 2)), 1. / 2)


class f6():
    def __init__(self):
        self.count = 0

    def call(self, X):
        self.count += 1
        suma = 0
        try:
            for x in X:
                suma += pow(x, 2)
        except:
            suma += pow(X, 2)
        return 0.5 + (pow(math.sin(pow(suma, 1./2)), 2) - 0.5) / pow((1 + 0.001 * suma), 2)
