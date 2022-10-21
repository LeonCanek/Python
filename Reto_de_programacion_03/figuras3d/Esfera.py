from Reto_de_programacion_03.figuras2d.Punto import Punto
from Reto_de_programacion_03.figuras3d.Punto3D import Punto3D
from Reto_de_programacion_03.figuras2d.Circunferencia import Circunferencia

class Esfera(Circunferencia):
    def __init__(self, c, r):
        super().__init__(Punto(c.x, c.y), r)
        self.c = c

    def __str__(self):
        return "(" + self.c.__str__() + "):" + str(self.r)


# print(Esfera(Punto3D(0, 0, 0), 1.0))
# print(Esfera(Punto3D(0.1, 0.2, -0.3), 1.23))
