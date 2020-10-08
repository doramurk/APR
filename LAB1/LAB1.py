import numpy as np

epsilon = 10e-20

class Matrica:
    def __init__(self, broj_redaka=0, broj_stupaca=0):
        self.broj_redaka = broj_redaka
        self.broj_stupaca = broj_stupaca
        self.elementi = []
        for i in range(broj_redaka):
                self.elementi.append([None] * broj_stupaca)

    def __del__(self):
        del self

    def promijeniDimenzije(self, broj_redaka, broj_stupaca):
        A = self
        self.__init__(broj_redaka, broj_stupaca)
        for i in range(broj_redaka):
            for j in range(broj_stupaca):
                self.postaviElement(A.dohvatiElement(i, j), i, j)


    def operatorPridruzivanja(self, B):
        self.promijeniDimenzije(B.broj_redaka, B.broj_stupaca)
        for i in range(B.broj_redaka):
            for j in range(B.broj_stupaca):
                self.postaviElement(B.dohvatiElement(i, j), i, j)

    def citajMatricu(self, file_name):
        file = open("data/" + file_name, "r")
        lines = file.readlines()
        broj_redaka = len(lines)
        broj_stupaca = len(lines[0].split())
        self.promijeniDimenzije(broj_redaka, broj_stupaca)
        i = 0
        for line in lines:
            j = 0
            for e in line.split():
                self.postaviElement(float(e), i, j)
                j += 1
            i += 1
        file.close()

    def upisiMatricuUDatoteku(self, file_name):
        file = open("data/" +file_name, "w")
        for i in range(self.broj_redaka):
            for j in range(self.broj_stupaca):
                file.write(str(self.dohvatiElement(i, j)))
                file.write(" ")
            file.write("\n")
        file.close()

    def ispisiMatricuNaEkran(self):
        for i in range(self.broj_redaka):
            for j in range(self.broj_stupaca):
                print(self.dohvatiElement(i, j), end=" ")
            print("\n", end="")
        print("")

    def postaviElement(self, x, i, j):
        self.elementi[i][j] = x

    def dohvatiElement(self, i, j):
        return self.elementi[i][j]

    def zbrojiMatrice(self, B):
        if self.broj_stupaca == B.broj_stupaca and self.broj_redaka == B.broj_redaka:
            rez = Matrica(self.broj_redaka, self.broj_stupaca)
            for i in range(self.broj_redaka):
                for j in range(self.broj_stupaca):
                    rez.postaviElement(self.elementi[i][j] + B.elementi[i][j], i, j)
            return rez
        else:
            print("Matrice se ne mogu zbrojiti jer nemaju iste dimenzije!")

    def oduzmiMatrice(self, B):
        if self.broj_stupaca == B.broj_stupaca and self.broj_redaka == B.broj_redaka:
            rez = Matrica(self.broj_redaka, self.broj_stupaca)
            for i in range(self.broj_redaka):
                for j in range(self.broj_stupaca):
                    rez.postaviElement(self.dohvatiElement(i, j) - B.dohvatiElement(i, j), i, j)
            return rez
        else:
            print("Matrice se ne mogu oduzeti jer nemaju iste dimenzije!")

    def pomnoziMatrice(self, B):
        if self.broj_stupaca == B.broj_redaka:
            rez = Matrica(self.broj_redaka, B.broj_stupaca)
            for i in range(self.broj_redaka):
                for j in range(B.broj_stupaca):
                    sum = 0
                    for k in range(B.broj_redaka):
                        sum += self.dohvatiElement(i, k) * B.dohvatiElement(k, j)
                    rez.postaviElement(sum, i, j)
            return rez
        else:
            print("Matrice se ne mogu pomnoziti jer nemaju odgovarajuce dimenzije!")

    def transponirajMatricu(self):
        rez = Matrica(self.broj_redaka, self.broj_stupaca)
        for i in range(self.broj_redaka):
            for j in range(self.broj_stupaca):
                rez.postaviElement(self.elementi[i][j], j, i)
        return rez

    def zbrojiMatriceC(self, B):
        if self.broj_stupaca == B.broj_stupaca and self.broj_redaka == B.broj_redaka:
            for i in range(self.broj_redaka):
                for j in range(self.broj_stupaca):
                    self.postaviElement(self.dohvatiElement(i, j) + B.dohvatiElement(i, j), i, j)
        else:
            raise Exception("Matrice se ne mogu zbrojiti jer nemaju iste dimenzije!")

    def oduzmiMatriceC(self, B):
        if self.broj_stupaca == B.broj_stupaca and self.broj_redaka == B.broj_redaka:
            for i in range(self.broj_redaka):
                for j in range(self.broj_stupaca):
                    self.postaviElement(self.dohvatiElement(i, j) - B.dohvatiElement(i, j), i, j)
        else:
            print("Matrice se ne mogu oduzeti jer nemaju iste dimenzije!")

    def pomnoziMatricuSkalarom(self, s):
        rez = Matrica(self.broj_redaka, self.broj_stupaca)
        for i in range(self.broj_redaka):
            for j in range(self.broj_stupaca):
                rez.postaviElement(self.dohvatiElement(i, j) * s, i, j)
        return rez

    def usporediMatrice(self, B):
        if self.broj_stupaca == B.broj_stupaca and self.broj_redaka == B.broj_redaka:
            rez = True
            for i in range(self.broj_redaka):
                for j in range(self.broj_stupaca):
                    if not self.dohvatiElement(i, j) == B.dohvatiElement(i, j):
                        print("Matrice nisu identicne!")
                        return False
            print("Matrice su identicne!")
            return True
        else:
            print("Matrice nisu istih dimenzija!")
            return False

    def supstitucijaUnaprijed(self, b):
        if b.broj_stupaca == 1 and b.broj_redaka == self.broj_redaka:
            rez = Matrica(b.broj_redaka, 1)
            for i in range(b.broj_redaka):
                rez.postaviElement(b.dohvatiElement(i, 0), i, 0)
            for i in range(self.broj_stupaca - 1):
                for j in range(i + 1, self.broj_redaka):
                    rez.postaviElement(rez.dohvatiElement(j, 0) - (self.dohvatiElement(j, i) * b.dohvatiElement(i, 0)), j, 0)
            return rez
        else:
            print("Ulaz mora biti vektor duljine jednake dimenziji kvadratne matrice!")

    def supstitucijaUnazad(self, b):
        if b.broj_stupaca == 1 and b.broj_redaka == self.broj_redaka:
            rez = Matrica(b.broj_redaka, 1)
            for i in range(b.broj_redaka):
                rez.postaviElement(b.dohvatiElement(i, 0), i, 0)
            for i in range(self.broj_redaka - 1, -1, -1):
                if abs(self.dohvatiElement(i, i)) > epsilon:
                    rez.postaviElement(rez.dohvatiElement(i, 0) / self.dohvatiElement(i, i), i, 0)
                    for j in range(i):
                        rez.postaviElement(rez.dohvatiElement(j, 0) - (self.dohvatiElement(j, i) * rez.dohvatiElement(i, 0)), j, 0)
                else:
                    raise Exception("Stozerni element je skoro 0! Stozerni element = {}".format(self.dohvatiElement(i, i)))
            return rez
        else:
            print("Ulaz mora biti vektor duljine jednake dimenziji kvadratne matrice!")

    def LUdekompozicija(self):
        if self.broj_stupaca == self.broj_redaka:
            rez = Matrica(self.broj_redaka, self.broj_stupaca)
            for i in range(self.broj_redaka):
                for j in range(self.broj_stupaca):
                    rez.postaviElement(self.dohvatiElement(i, j), i, j)
            for i in range(self.broj_stupaca - 1):
                if abs(rez.dohvatiElement(i, i)) > epsilon:
                    for j in range(i + 1, self.broj_stupaca):
                        rez.postaviElement(rez.dohvatiElement(j, i) / rez.dohvatiElement(i, i), j, i)
                        for k in range(i + 1, self.broj_stupaca):
                            rez.postaviElement(rez.dohvatiElement(j, k) - (rez.dohvatiElement(j, i) * rez.dohvatiElement(i, k)), j, k)
                else:
                    raise Exception("Stozerni element je skoro 0! Stozerni element = {}".format(rez.dohvatiElement(i, i)))
        else:
            raise Exception("Matrica nije kvadratna i ne moze se izracunati LU!")
        return rez

    def LUPdekompozicija(self):
        if self.broj_stupaca == self.broj_redaka:
            rez = Matrica(self.broj_redaka, self.broj_stupaca)
            for i in range(self.broj_redaka):
                for j in range(self.broj_stupaca):
                    rez.postaviElement(self.dohvatiElement(i, j), i, j)
            rez1 = Matrica(self.broj_redaka, self.broj_stupaca)
            P = []
            br_permutacija = 0
            for i in range(self.broj_stupaca):
                P.append(i)
            for i in range(self.broj_stupaca - 1):
                rez1.operatorPridruzivanja(rez)
                pivot = 0
                for j in range(i+1, self.broj_stupaca):
                    if abs(rez.dohvatiElement(i, j)) > pivot:
                        pivot = rez.dohvatiElement(i, j)
                        L = j
                if abs(pivot) > epsilon:
                    for j in range(rez.broj_stupaca):
                        rez.postaviElement(rez1.dohvatiElement(i, j), L, j)
                        rez.postaviElement(rez1.dohvatiElement(L, j), i, j)
                    p1 = P[i]
                    P[i] = P[L]
                    P[L] = p1
                    br_permutacija += 1
                    for j in range(i + 1, self.broj_stupaca):
                        rez.postaviElement(rez.dohvatiElement(j, i) / rez.dohvatiElement(i, i), j, i)
                        for k in range(i + 1, rez.broj_redaka):
                            rez.postaviElement(rez.dohvatiElement(j, k) - (rez.dohvatiElement(j, i) * rez.dohvatiElement(i, k)), j, k)
                else:
                    raise Exception("Stozerni element je skoro 0! Stozerni element = {}".format(rez.dohvatiElement(i, i)))
        else:
            raise Exception("Matrica nije kvadratna i ne moze se izracunati LUP!")
        return rez, P, br_permutacija

    def inverz(self):
        if self.determinanta() > 10e-6:
            A_lup, P, br_permutacija = self.LUPdekompozicija()
            X_array = []
            X = Matrica(self.broj_redaka, self.broj_stupaca)
            b = Matrica(self.broj_redaka, self.broj_stupaca)
            for i in range(self.broj_redaka):
                for j in range(self.broj_stupaca):
                    b.postaviElement(0, i, j)
            for i in range(self.broj_redaka):
                b.postaviElement(1, i, i)
            permute = Matrica(self.broj_redaka, self.broj_stupaca)
            for i in range(self.broj_redaka):
                for j in range(self.broj_stupaca):
                    permute.postaviElement(0, i, j)
            for i, p in enumerate(P):
                permute.postaviElement(1, i, p)
            for i in range(A_lup.broj_redaka):
                y = A_lup.supstitucijaUnaprijed(permute.izdvojiStupac(i))
                x = A_lup.supstitucijaUnazad(y)
                X_array.append(x)
            for k, matrica in enumerate(X_array):
                for i in range(matrica.broj_redaka):
                    for j in range(matrica.broj_stupaca):
                        X.postaviElement(matrica.dohvatiElement(i, j), i, k)
            return X
        else:
            raise Exception("Nema inverza")

    def izdvojiStupac(self, i):
        rez = Matrica(self.broj_redaka, 1)
        for j in range(self.broj_redaka):
            rez.postaviElement(self.dohvatiElement(j, i), j, 0)
        return rez


    def determinanta(self):
        A_lup, P, br_permutacija = self.LUPdekompozicija()
        L = A_lup.vratiL()
        U = A_lup.vratiU()

        det_L = 1
        det_U = 1
        for i in range(U.broj_redaka):
            det_U *= U.dohvatiElement(i, i)
        det_P = (-1)**br_permutacija

        return det_L*det_P*det_U

    def vratiL(self):
        L = Matrica(self.broj_redaka, self.broj_stupaca)
        for i in range(self.broj_redaka):
            for j in range(self.broj_stupaca):
                if i == j:
                    L.postaviElement(1, i, j)
                if i < j:
                    L.postaviElement(0, i, j)
                if i > j:
                    L.postaviElement(self.dohvatiElement(i, j), i, j)
        return L

    def vratiU(self):
        U = Matrica(self.broj_redaka, self.broj_stupaca)
        for i in range(self.broj_redaka):
            for j in range(self.broj_stupaca):
                if i <= j:
                    U.postaviElement(self.dohvatiElement(i, j), i, j)
                if i > j:
                    U.postaviElement(0, i, j)
        return U

    def permute(self, P):
        rez = Matrica(self.broj_redaka, self.broj_stupaca)
        for i in range(self.broj_redaka):
            for j in range(self.broj_stupaca):
                rez.postaviElement(self.dohvatiElement(i, j), i, j)

        for i in range(self.broj_redaka):
            index = P[i]
            row = self.elementi[index]
            rez.elementi[i] = row
        return rez


def izracunajX_LUP(A, b):
    A_lup, P, br_perm = A.LUPdekompozicija()
    permute = Matrica(A.broj_redaka, A.broj_stupaca)
    for i in range(A.broj_redaka):
        for j in range(A.broj_stupaca):
            permute.postaviElement(0, i, j)
    for i, p in enumerate(P):
        permute.postaviElement(1, i, p)
    b_p = permute.pomnoziMatrice(b)
    #b_p = b.permute(P)
    X_array = []
    X = Matrica(A_lup.broj_redaka, 1)
    y = A_lup.supstitucijaUnaprijed(b_p)
    x = A_lup.supstitucijaUnazad(y)
    X_array.append(x)
    for k, matrica in enumerate(X_array):
        for i in range(matrica.broj_redaka):
            for j in range(matrica.broj_stupaca):
                X.postaviElement(matrica.dohvatiElement(i, j), i, k)
    return X

def izracunajX_LU(A, b):
    A_lu = A.LUdekompozicija()
    X_array = []
    X = Matrica(A_lu.broj_redaka, 1)
    y = A_lu.supstitucijaUnaprijed(b)
    x = A_lu.supstitucijaUnazad(y)
    X_array.append(x)
    for k, matrica in enumerate(X_array):
        for i in range(matrica.broj_redaka):
            for j in range(matrica.broj_stupaca):
                X.postaviElement(matrica.dohvatiElement(i, j), i, k)
    return X


def prvi():
    A = Matrica()
    A.citajMatricu("prviA.txt")
    B = Matrica()
    B.citajMatricu("prviB.txt")

    A.operatorPridruzivanja(A.pomnoziMatricuSkalarom(10e-200))
    B.operatorPridruzivanja(B.pomnoziMatricuSkalarom(10e-200))

    A.usporediMatrice(B)

def drugi():
    A = Matrica()
    A.citajMatricu("drugiA.txt")
    b = Matrica()
    b.citajMatricu("drugib.txt")

    try:
        X = izracunajX_LU(A, b)
        print("Rješenje LU:")
        X.ispisiMatricuNaEkran()

        X = izracunajX_LUP(A, b)
        print("Rješenje LUP:")
        X.ispisiMatricuNaEkran()
    except:
        X = izracunajX_LUP(A, b)
        print("Rješenje LUP:")
        X.ispisiMatricuNaEkran()


def treci():
    A = Matrica()
    A.citajMatricu(file_name="treciA.txt")

    #b = Matrica()
    #b.citajMatricu("trecib.txt")

    A_lu = A.LUdekompozicija()
    print("LU")
    A_lu.ispisiMatricuNaEkran()

    A_lup, P, br = A.LUPdekompozicija()
    print("LUP")
    A_lup.ispisiMatricuNaEkran()

    '''try:
        X = izracunajX_LU(A, b)
        print("LU Rješenje:")
        X.ispisiMatricuNaEkran()
    except:
        X = izracunajX_LUP(A, b)
        print("LUP Rješenje:")
        X.ispisiMatricuNaEkran()'''

def cetvrti():
    A = Matrica()
    A.citajMatricu("cetvrtiA.txt")

    b = Matrica()
    b.citajMatricu("cetvrtib.txt")

    try:
        X = izracunajX_LU(A, b)
        print("LU Rješenje:")
        X.ispisiMatricuNaEkran()

        X = izracunajX_LUP(A, b)
        print("LUP Rješenje:")
        X.ispisiMatricuNaEkran()
    except:
        X = izracunajX_LUP(A, b)
        print("LUP Rješenje:")
        X.ispisiMatricuNaEkran()

def peti():
    A = Matrica()
    A.citajMatricu("petiA.txt")

    b = Matrica()
    b.citajMatricu("petib.txt")

    try:
        X = izracunajX_LU(A, b)
        print("LU Rješenje:")
        X.ispisiMatricuNaEkran()
    except:
        X = izracunajX_LUP(A, b)
        print("LUP Rješenje:")
        X.ispisiMatricuNaEkran()

def sesti():
    A = Matrica()
    A.citajMatricu("sestiA.txt")

    b = Matrica()
    b.citajMatricu("sestib.txt")

    try:
        X = izracunajX_LU(A, b)
        print("LU Rješenje:")
        X.ispisiMatricuNaEkran()
    except:
        X = izracunajX_LUP(A, b)
        print("LUP Rješenje:")
        X.ispisiMatricuNaEkran()

def sedmi():
    A = Matrica()
    A.citajMatricu("sedmi.txt")

    try:
        inv = A.inverz()
        if inv:
            inv.ispisiMatricuNaEkran()
    except:
        print("Ne postoji inverz")

def osmi():
    A = Matrica()
    A.citajMatricu("osmi.txt")

    inv = A.inverz()
    if inv:
        inv.ispisiMatricuNaEkran()

def deveti():
    A = Matrica()
    A.citajMatricu("deveti.txt")

    det = A.determinanta()
    print(det)

def deseti():
    A = Matrica()
    A.citajMatricu("deseti.txt")

    det = A.determinanta()
    print(det)

if __name__ == '__main__':
    print("\nPRVI")
    prvi()
    print("\nDRUGI")
    drugi()
    print("\nTRECI")
    treci()
    print("\nCETVRTI")
    cetvrti()
    print("\nPETI")
    peti()
    print("\nSESTI")
    sesti()
    print("\nSEDMI")
    sedmi()
    print("\nOSMI")
    osmi()
    print("\nDEVETI")
    deveti()
    print("\nDESETI")
    deseti()
