class Punto:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        return str(self.x) + "," + str(self.y)


print(Punto(0, 0))
print(Punto(4, -7.35))


class Punto3D(Punto):
    def __init__(self, x, y, z):
        super().__init__(x, y)
        self.z = z

    def __str__(self):
        return str(self.x) + "," + str(self.y) + "," + str(self.z)


print(Punto3D(0, 0, 0))
print(Punto3D(4, -7.36, 0.14))


class Circunferencia:
    def __init__(self, c, r):
        self.c = c
        self.r = r

    def __str__(self):
        return "(" + self.c.__str__() + "):" + str(self.r)


print(Circunferencia(Punto(0, 0), 1.0))
print(Circunferencia(Punto(1.01, 4.3), 6.2))


class Esfera(Circunferencia):
    def __init__(self, c, r):
        super().__init__(Punto(c.x, c.y), r)
        self.c = c

    def __str__(self):
        return "(" + self.c.__str__() + "):" + str(self.r)


print(Esfera(Punto3D(0, 0, 0), 1.0))
print(Esfera(Punto3D(0.1, 0.2, -0.3), 1.23))
