'''
#### HOOKE JEVEES POSTUPAK ####
x0 - pocetna tocka
xB - bazna tocka
xP - pocetna tocka pretrazivanja
xN - tocka dobivena pretrazivanjem
'''

def citaj(ime):
    x0 = []
    dat = open(ime, "r")
    line = dat.readline()
    for x in line.split(","):
        x0.append(float(x))
    dx = float(dat.readline())
    e = float(dat.readline())
    return x0, dx, e


def hooke_jevees(f, citaj_tocku=False, pocetna_tocka=None, dx=0.5, e=10e-6):
    if pocetna_tocka is None or citaj_tocku == 'True':
        pocetna_tocka, dx, e = citaj("HookeJevees")
    xp = pocetna_tocka.copy()
    xb = pocetna_tocka.copy()
    while(dx > e):
        xn = istrazi(f, xp, dx)
        #print("bazna tocka={}  pocetna tocka pretrazivanja={}  tocka dobivena pretrazivanjem={}".format(xb, xp, xn))
        #print("f(xb)={}  f(xp)={}  f(xn)={}".format(f(xb), f(xp), f(xn)))
        if f(xn) < f(xb):           #prihvacamo baznu tocku
            for i in range(len(xp)):
                xp[i] = 2 * xn[i] - xb[i]
            xb = xn.copy()
        else:
            dx = 0.5*dx
            xp = xb.copy()

    return xb


def istrazi(f, xp, dx):
    x = xp.copy()
    for i in range(len(x)):
        p = f(x)
        x[i] = float(float(x[i]) + dx)            #povecamo za dx
        n = f(x)
        if n > p:                   #ne valja pozitivni pomak
            x[i] = x[i] - 2 * dx    #smanjimo za dx (negativni pomak)
            n = f(x)
            if n > p:               #ne valja ni negativni
                x[i] = x[i] + dx    #vratimo na staro
    return x
