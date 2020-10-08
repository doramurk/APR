import copy
from HookeJevees import hooke_jevees
import math
import funkcije_ogranicene
import funkcija_G


def nezadovoljena_implicitna_nejednadzbe(x0, implicitna):
    g = []
    for impl in implicitna:
        if impl(x0) < 0:
            g.append(impl)
    return g


def pronadi_unutarnju(g, x0, t, e):
    G = funkcija_G.funkcija_G(g, x0, t)
    while True:
        x0_prije = G.x0
        x0_sad = hooke_jevees(f=G.call, pocetna_tocka=x0_prije)
        G.t *= 10
        G.x0 = copy.deepcopy(x0_sad)

        for x1, x2 in zip(x0_sad, x0_prije):
            if abs(x1 - x2) > e:
                continue
            return x0_sad


def transformiraj(f, pocetna_tocka, implicitna_nejednadzbe, implicitna_jednadzbe=None, t=1, e=10e-6):
    x0 = copy.deepcopy(pocetna_tocka)
    g = nezadovoljena_implicitna_nejednadzbe(x0, implicitna_nejednadzbe)
    if len(g) != 0:
        #x0_unutarnja = pronadi_unutarnju(g, x0, t, e)
        x0_unutarnja = pronadi_unutarnju(implicitna_nejednadzbe, x0, t, e)
    else:
        x0_unutarnja = x0
    U = funkcije_ogranicene.funkcija_ogranicena(f, x0_unutarnja, t, implicitna_nejednadzbe, implicitna_jednadzbe)

    while True:
        x0_prije = U.x0
        x0_sad = hooke_jevees(U.call, pocetna_tocka=x0_prije)
        U.t *= 10
        U.x0 = copy.deepcopy(x0_sad)

        for x1, x2 in zip(x0_sad, x0_prije):
            if abs(x1 - x2) > e:
                continue
            return x0_sad
