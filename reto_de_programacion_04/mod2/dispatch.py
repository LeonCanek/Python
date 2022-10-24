from multipledispatch import dispatch

@dispatch()
def m():
    print("Sin argumentos")

@dispatch(float)
def m(x):
    print("Valor del argumento:", x)


m()
m(1.23)

#[1] M. Rocklin “multipledispatch 0.6.0”, pypi.org (Agosto 8, 2018) [En línea]. Disponible en: https://pypi.org/project/multipledispatch/. [Accedido: 23-10-2022]



