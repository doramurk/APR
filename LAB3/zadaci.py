import funkcije
import gradijentniSpust
import NewtonRaphson
import box
import ogranicenja
from transformacijaNaMjesovitiNacin import transformiraj
import sys


def prvi(citaj):
    f = funkcije.f3()
    min = gradijentniSpust.gradijentniSpust(f.call, f.gradient, [0.0, 0.0], zlatni=False)
    print("Minimum metodom najbrzeg spusta bez određivanja optimalnog iznosa koraka za f3 u: {}".format(min))
    print("Broj iteracija algoritma: {}".format(f.count))
    print("Broj iteracija gradijenta: {}".format(f.gradCount))
    print("Vrijednost funkcije: {}".format(f.call(min)))
    f.count = 0
    f.gradCount = 0
    min = gradijentniSpust.gradijentniSpust(f.call, f.gradient, [0.0, 0.0], citaj=citaj, zlatni=True)
    print("Minimum metodom najbrzeg spusta uz određivanje optimalnog iznosa koraka za f3 u: {}".format(min))
    print("Broj iteracija: {}".format(f.count))
    print("Broj iteracija gradijenta: {}".format(f.gradCount))
    print("Vrijednost funkcije: {}".format(f.call(min)))


def drugi(citaj):
    f1 = funkcije.f1()
    f2 = funkcije.f2()

    min1grad = gradijentniSpust.gradijentniSpust(f1.call, f1.gradient, [-1.9, 2.0], zlatni=True)
    print("Minimum metodom najbrzeg spusta uz određivanje optimalnog iznosa koraka za f1 u: {}".format(min1grad))
    print("Broj iteracija algoritma: {}".format(f1.count))
    print("Broj iteracija gradijenta: {}".format(f1.gradCount))
    print("Broj iteracija hesseove matrice: {}".format(f1.hessCount))
    print("Vrijednost funkcije: {}".format(f1.call(min1grad)))
    f1.count = 0
    f1.gradCount = 0
    f1.hessCount = 0

    min2grad = gradijentniSpust.gradijentniSpust(f2.call, f2.gradient, [0.1, 0.3], zlatni=True)
    print("Minimum metodom najbrzeg spusta uz određivanje optimalnog iznosa koraka za f2 u: {}".format(min2grad))
    print("Broj iteracija algoritma: {}".format(f2.count))
    print("Broj iteracija gradijenta: {}".format(f2.gradCount))
    print("Broj iteracija hesseove matrice: {}".format(f2.hessCount))
    print("Vrijednost funkcije: {}".format(f2.call(min2grad)))
    f2.count = 0
    f2.gradCount = 0
    f2.hessCount = 0

    min1new = NewtonRaphson.newtonRaphson(f1.call, f1.gradient, f1.hesseova, [-1.9, 2.0], zlatni=True)
    print("Minimum metodom NewtonRaphson uz određivanje optimalnog iznosa koraka za f1 u: {}".format(min1new))
    print("Broj iteracija algoritma: {}".format(f1.count))
    print("Broj iteracija gradijenta: {}".format(f1.gradCount))
    print("Broj iteracija hesseove matrice: {}".format(f1.hessCount))
    print("Vrijednost funkcije: {}".format(f1.call(min1new)))
    f1.count = 0
    f1.gradCount = 0
    f1.hessCount = 0

    min2new = NewtonRaphson.newtonRaphson(f2.call, f2.gradient, f2.hesseova, [0.1, 0.3], zlatni=True)
    print("Minimum metodom NewtonRaphson uz određivanje optimalnog iznosa koraka za f2 u: {}".format(min2grad))
    print("Broj iteracija algoritma: {}".format(f2.count))
    print("Broj iteracija gradijenta: {}".format(f2.gradCount))
    print("Broj iteracija hesseove matrice: {}".format(f2.hessCount))
    print("Vrijednost funkcije: {}".format(f2.call(min2new)))
    f2.count = 0
    f2.gradCount = 0
    f2.hessCount = 0


def treci(citaj):
    f1 = funkcije.f1()
    f2 = funkcije.f2()

    min_box = box.box(f1.call, pocetna_tocka=[-1.9, 2.0], implicitna=[ogranicenja.ogr1, ogranicenja.ogr2])
    print("Minimum boxovom metodom za f1 u: {}".format(min_box))
    print("Broj iteracija algoritma: {}".format(f1.count))
    print("Vrijednost funkcije: {}".format(f1.call(min_box)))
    f1.count = 0

    min_box_2 = box.box(f2.call, pocetna_tocka=[0.1, 0.3], implicitna=[ogranicenja.ogr1, ogranicenja.ogr2])
    print("Minimum boxovom metodom za f2 u: {}".format(min_box_2))
    print("Broj iteracija algoritma: {}".format(f2.count))
    print("Vrijednost funkcije: {}".format(f2.call(min_box_2)))
    f2.count = 0


def cetvrti(citaj):
    f1 = funkcije.f1()
    f2 = funkcije.f2()

    min_box = transformiraj(f1.call, pocetna_tocka=[-1.9, 2.0], t=1, implicitna_nejednadzbe=[ogranicenja.ogr1, ogranicenja.ogr2])
    print("Minimum tranformiranog problema za f1 u: {}".format(min_box))
    print("Broj iteracija algoritma: {}".format(f1.count))
    print("Vrijednost funkcije: {}".format(f1.call(min_box)))
    f1.count = 0

    min_box_2 = transformiraj(f2.call, pocetna_tocka=[0.1, 0.3], implicitna_nejednadzbe=[ogranicenja.ogr1, ogranicenja.ogr2])
    print("Minimum transformiranog problema za f2 u: {}".format(min_box_2))
    print("Broj iteracija algoritma: {}".format(f2.count))
    print("Vrijednost funkcije: {}".format(f2.call(min_box_2)))
    f2.count = 0


def peti(citaj):
    f = funkcije.f4()

    min = transformiraj(f.call, pocetna_tocka=[5, 5], implicitna_nejednadzbe=[ogranicenja.ogr3, ogranicenja.ogr4], implicitna_jednadzbe=[ogranicenja.ogr5])
    print("Minimum tranformiranog problema za f4 u: {}".format(min))
    print("Broj iteracija algoritma: {}".format(f.count))
    print("Vrijednost funkcije: {}".format(f.call(min)))
    f.count = 0


if __name__ == '__main__':
    citaj = sys.argv[1]
    #prvi(citaj)
    #print("\n")
    #drugi(citaj)
    #print("\n")
    treci(citaj)
    #print("\n")
    #cetvrti(citaj)
    #print("\n")
    #peti(citaj)
