from math import *


def jm(a, b, c):
    jam = a + b - c
    sq = sqrt(jam)
    nes = 0.5 * sq
    return nes


def intCheck(x, y, z):
    a = int(x)
    b = int(y)
    c = int(z)
    v = []
    try:
        if x / a == 1 or x / a == 1.0:
            v.append(x)
    except:
        pass
    try:
        if y / b == 1 or y / b == 1.0:
            v.append(y)
    except:
        pass
    try:
        if z / c == 1 or z / c == 1.0:
            v.append(z)
    except:
        pass
    if v != []:
        return v
    else:
        return "there is no int answer :("

class Azla:
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

    def gam(self):
        return self.a + self.b + self.c

    def pmo(self):
        p = Azla.gam(self) / 2
        return (p)

    def smo(self):
        d = Azla.pmo(self) - self.a
        e = Azla.pmo(self) - self.b
        f = Azla.pmo(self) - self.c
        z = Azla.pmo(self) * d * e * f
        s = sqrt(z)
        return s


class Highest(Azla):
    def ha(self):
        h1 = Azla.smo(self) * 2
        ha = h1 / self.a
        return ha

    def hb(self):
        h2 = Azla.smo(self) * 2
        hb = h2 / self.b
        return hb

    def hc(self):
        h3 = Azla.smo(self) * 2
        hc = h3 / self.c
        return hc


class Miane(Azla):
    def ma(self):
        po = 2 * self.b ** 2
        pt = 2 * self.c ** 2
        ptr = self.a ** 2
        gz = jm(po, pt, ptr)
        return gz

    def mb(self):
        bo = 2 * self.a ** 2
        bt = 2 * self.c ** 2
        btr = self.b ** 2
        ban = jm(bo, bt, btr)
        return ban

    def mc(self):
        co = 2 * self.a ** 2
        ct = 2 * self.b ** 2
        ctr = self.c ** 2
        can = jm(co, ct, ctr)
        return can


class Nimsaz(Azla):
    def da(self):
        bc = self.b + self.c
        bcd = bc ** 2
        abd = self.a ** 2
        mena = bcd - abd
        zbc = self.b * self.c
        sorata = zbc * mena
        sqa = sqrt(sorata)
        lan1 = sqa / bc
        return lan1

    def db(self):
        ac = self.a + self.c
        acd = ac ** 2
        bbd = self.b ** 2
        menb = acd - bbd
        zac = self.a * self.c
        soratb = zac * menb
        sqb = sqrt(soratb)
        lan2 = sqb / ac
        return lan2

    def dc(self):
        ab = self.a + self.b
        abd = ab ** 2
        cbd = self.c ** 2
        menc = abd - cbd
        zab = self.a * self.b
        soratc = zab * menc
        sqc = sqrt(soratc)
        lan3 = sqc / ab
        return lan3


class Shmohiti(Azla):
    def r(self):
        zaz = self.a * self.b * self.c
        fbs = Azla.smo(self) * 4
        answ = zaz / fbs
        return answ


class Shmohati(Azla):
    def r(self):
        return Azla.smo(self) / Azla.pmo(self)


class Shdbsz(Azla):
    def ra(self):
        q = Azla.pmo(self) - self.a
        return Azla.smo(self) / q

    def rb(self):
        b = Azla.pmo(self) - self.b
        return Azla.smo(self) / b

    def rc(self):
        l = Azla.pmo(self) - self.c
        return Azla.smo(self) / l


# try:
#    az1 = int(input("zel aval ro vared kn: "))
#    az2 = int(input("zel dovom ro vared kn: "))
#    az3 = int(input("zel sevo ro vared kn: "))
# except Exception as err:
#    print("write like a human", err)

he = Shdbsz(8, 15, 17)
print(he.ra(), he.rb(), he.rc())

try:
    bla = Highest(8, 15, 17)
    print(bla)
    x = bla.ha()
    print(x)
    y = bla.hb()
    print(y)
    z = bla.hc()
    print(z)
    an = intCheck(x, y, z)
    print(an)
except Exception as err:
    print(err)
