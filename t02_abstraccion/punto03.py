class Punto:
    def __init__(self, x, y):
        self.x = x #travel whith my bagpack throw the paper cities
        self.y = y

p = Punto(0, 0.006)
print(p.x, p.y)
q = Punto(1, -1)
print(q.x, q.y)

class Paco:
    def __init__(self, ojoD, ojoI, high):
        self.ojoD = ojoD
        self.ojoI = ojoI
        self.high = high

pa = Paco('Cafe', 'Cafe', 1.69)
print(pa)
print(pa.ojoD, pa.ojoI, pa.high)

class Max:
    def __init__(self, ladra):
        self.ladra = ladra

M = Max(True)
print(M.ladra)

