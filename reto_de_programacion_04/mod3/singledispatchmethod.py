from functools import singledispatchmethod
from tokenize import String


class Klass:
    @singledispatchmethod
    def m(self, arg):
        print("Argumento:", arg)

    @m.register(int)
    def _m(self, arg: int):
        print("Argumento entero:", arg)

    @m.register(type(String))
    def _m(self, arg):
        print("Argumento cadena:", arg)


k = Klass()
k.m(42)
k.m("Hola mundo cruel")
k.m([1, 2, 3])


#[2] Python “:mod:`functools` --- Higher-order functions and operations on callable objects”, python.org [En línea]. Disponible en: https://github.com/python/cpython/blob/3.10/Doc/library/functools.rst#id5 [Accedido: 23-10-2022]
