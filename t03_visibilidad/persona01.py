class Persona:
    def __init__(self):
        self.nombre = "Martin He"
        self._edad = 87

p = Persona()
print(p.nombre, p._edad)
