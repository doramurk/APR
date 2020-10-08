from math import sqrt
e = 10e-6
k = 0.5*(sqrt(5) - 1)
h = 10e-2


'''###### ZLATNI REZ #######
Algoritam zlatnog reza

ulazne velicine:
- a, b: pocetne granice unimodalnog intervala
- e: preciznost

izlazne veličine:
-
'''


def citajInterval(ime):
    dat = open(ime, "r")
    e = float(dat.readline())
    line = dat.readline()
    a = float(line.split(",")[0])
    b = float(line.split(",")[1])
    return a, b, e


def citajTocku(ime):
    dat = open(ime, "r")
    e = float(dat.readline())
    pocetna = float(dat.readline())
    return pocetna, e


def zlatni_rez(f, citaj_tocku=False, a=None, b=None, e=10e-6, pocetna_tocka=None, h=1):
    if citaj_tocku == 'True':
        pocetna_tocka, e = citajTocku("zlatniRezTocka")
    if pocetna_tocka is not None:
        a, b = unimodalni(f, pocetna_tocka, h)
    if pocetna_tocka is None and a is None and b is None:
        a, b, e = citajInterval("zlatniRezInterval")
    c = b - k * (b - a)
    d = a + k * (b - a)
    fc = f(c)
    fd = f(d)
    #print("a={a}    c={c}   d={d}   b={b}".format(a=str(a), c=str(c), d=str(d), b=str(b)))
    #print("f(a)={a}    f(c)={c}   f(d)={d}   f(b)={b}".format(a=str(f(a)), c=str(fc), d=str(fd), b=str(f(b))))
    #print("_________________________________________________________________________________________")
    while((b - a) > e):
        if fc < fd:
            b = d
            d = c
            c = b - k * (b - a)
            fd = fc
            fc = f(c)
            #print("a={a}    c={c}   d={d}   b={b}".format(a=str(a), c=str(c), d=str(d), b=str(b)))
            #print("f(a)={a}    f(c)={c}   f(d)={d}   f(b)={b}".format(a=str(f(a)), c=str(fc), d=str(fd), b=str(f(b))))
            #print("_________________________________________________________________________________________")
        else:
            a = c
            c = d
            d = a + k * (b - a)
            fc = fd
            fd = f(d)
            #print("a={a}    c={c}   d={d}   b={b}".format(a=str(a), c=str(c), d=str(d), b=str(b)))
            #print("f(a)={a}    f(c)={c}   f(d)={d}   f(b)={b}".format(a=str(f(a)), c=str(fc), d=str(fd), b=str(f(b))))
            #print("_________________________________________________________________________________________")
    return (a + b) / 2  #ili nove vrijednosti a i b


'''###### UNIMODALNI ######
Postupak trazenja unimodalnog intervala

Ulazne velicine:
- tocka: pocetna tocka pretrazivanja
- h: pomak pretrazivanja
- f: ciljna funkcija

Izlazne vrijednosti:
- unimodalni interval [l, r]'''


def unimodalni(f, tocka, h=1):
    l = tocka - h
    r = tocka + h
    m = tocka
    step = 1

    fm = f(tocka)
    fl = f(l)
    fr = f(r)

    if fm < fr and fm < fl:
        return l, r
    elif fm > fr:
        while fm > fr:
            l = m
            m = r
            fm = fr
            step *= 2
            r = tocka + h * step
            fr = f(r)
        return l, r

    else:
        while fm > fl:
            r = m
            m = l
            fm = fl
            step *= 2
            l = tocka - h * step
            fl = f(l)
        return l, r
