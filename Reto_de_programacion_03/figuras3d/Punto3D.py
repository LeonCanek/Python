from Reto_de_programacion_03.figuras2d.Punto import Punto
class Punto3D(Punto):
    def __init__(self, x, y, z):
        super().__init__(x, y)
        self._z = z

    @property
    def z(self):
        return self._z

    @z.setter
    def z(self, z):
        self._z = z

    def __str__(self):
        return str(self.x) + "," + str(self.y) + "," + str(self.z)


