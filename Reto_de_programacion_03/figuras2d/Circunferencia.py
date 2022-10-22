from Reto_de_programacion_03 import Punto
class Circunferencia:
    def __init__(self, c=Punto(), r=1.0):
        self._c = c
        self._r = r

    @property
    def c(self):
        return self._c

    @property
    def x(self):
        return self._c.x

    @property
    def y(self):
        return self._c.y

    @property
    def r(self):
        return self._r

    @c.setter
    def c(self, c):
        self._c = c

    @r.setter
    def r(self, r):
        self._r = r

    def __str__(self):
        return "(" + str(self.x) + "," + str(self.y) + "):" + str(self.r)

# p=Punto()
# print(p.x)
# p=Circunferencia()
# print(p._Circunferencia__c)


# print(p.__c)
# print(p._Punto__c)


