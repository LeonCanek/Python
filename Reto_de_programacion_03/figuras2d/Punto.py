class Punto:
    def __init__(self, x = 0.0, y = 0.0):
        self._x = x
        self._y = y

    @property
    def x(self):
        return self._x

    @property
    def y(self):
        return self._y

    @x.setter
    def x(self, x):
        self._x = x

    @y.setter
    def y(self, y):
        self._y = y

    def __str__(self):
        return str(self._x) + "," + str(self._y)

    # def saludar(x):
    #     print("Holi Boli" , x)

#
# print(Punto(0, 0))
# print(Punto(4, -7.35))