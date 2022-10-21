class Punto:
    def __init__(self, x = 0.0, y = 0.0):
        self.x = x
        self.y = y

    def __str__(self):
        return "(" + str(self.x) + " , " + str(self.y) + ")"

p = Punto()
print(p.x, p.y)
q = Punto(5, 2.1)
print(q.x, q.y)
r = Punto(7)
print(r)
