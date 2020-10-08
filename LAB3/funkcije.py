class f1():
    def __init__(self):
        self.count = 0
        self.gradCount = 0
        self.hessCount = 0

    def call(self, X):
        self.count += 1
        x1 = X[0]
        x2 = X[1]
        return 100 * pow((x2 - pow(x1, 2)), 2) + pow((1 - x1), 2)

    def gradient(self, X):
        self.gradCount += 1
        x1 = X[0]
        x2 = X[1]
        dx1 = 2 * 100 * (x2 - pow(x1, 2)) * (-2 * x1) + 2 * (1 - x1) * (-1)
        dx2 = 2 * 100 * (x2 - pow(x1, 2))

        return [dx1, dx2]

    def hesseova(self, X):
        self.hessCount += 1
        x1 = X[0]
        x2 = X[1]
        dx1dx1 = -400 * x2 + 400 * 3 * pow(x1, 2) + 2
        dx1dx2 = -400 * x1
        dx2dx1 = -400 * x1
        dx2dx2 = 200

        return [[dx1dx1, dx1dx2], [dx2dx1, dx2dx2]]


class f2():
    def __init__(self):
        self.count = 0
        self.gradCount = 0
        self.hessCount = 0

    def call(self, X):
        self.count += 1
        x1 = X[0]
        x2 = X[1]
        return pow((x1 - 4), 2) + 4 * pow((x2 - 2), 2)

    def gradient(self, X):
        self.gradCount += 1
        x1 = X[0]
        x2 = X[1]
        dx1 = 2 * (x1 - 4)
        dx2 = 2 * 4 * (x2 - 2)

        return [dx1, dx2]

    def hesseova(self, X):
        self.hessCount += 1
        dx1dx1 = 2
        dx1dx2 = 0
        dx2dx1 = 0
        dx2dx2 = 8
        return [[dx1dx1, dx1dx2], [dx2dx1, dx2dx2]]


class f3():
    def __init__(self, ):
        self.count = 0
        self.gradCount = 0
        self.hessCount = 0

    def call(self, X):
        self.count += 1
        x1 = X[0]
        x2 = X[1]
        return pow((x1 - 2), 2) + pow((x2 + 3), 2)

    def gradient(self, X):
        self.gradCount += 1
        x1 = X[0]
        x2 = X[1]
        dx1 = 2 * (x1 - 2)
        dx2 = 2 * (x2 + 3)

        return [dx1, dx2]

    def hesseova(self, X):
        self.hessCount += 1
        dx1dx1 = 2
        dx1dx2 = 0
        dx2dx1 = 0
        dx2dx2 = 2
        return [[dx1dx1, dx1dx2], [dx2dx1, dx2dx2]]


class f4():
    def __init__(self):
        self.count = 0
        self.gradCount = 0
        self.hessCount = 0

    def call(self, X):
        self.count += 1
        x1 = X[0]
        x2 = X[1]
        return pow((x1 - 3), 2) + pow(x2, 2)

    def gradient(self, X):
        self.gradCount += 1
        x1 = X[0]
        x2 = X[1]
        dx1 = 2 * (x1 - 3)
        dx2 = 2 * x2

        return [dx1, dx2]

    def hesseova(self, X):
        self.hessCount += 1
        dx1dx1 = 2
        dx1dx2 = 0
        dx2dx1 = 0
        dx2dx2 = 2
        return [[dx1dx1, dx1dx2], [dx2dx1, dx2dx2]]
