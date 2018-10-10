from numpy import *
from matplotlib import pyplot

def read_matrix(n,m):
    matriz = zeros((n, m), dtype=int)
    productos = []
    for i in range(n):
        datos = input().split()
        producto = datos[0]
        numeros = datos[1:]
        for j in range(m):
            matriz[i, j] = int(numeros[j])
        productos.append(producto)
    return productos,matriz

n = int(input())
palabras = input().split()
m = len(palabras)
productos,matriz = read_matrix(n,m)
print(palabras)
print(matriz)
print(productos)
pyplot.bar(productos,matriz.sum(axis=1)/len(palabras))
pyplot.show()
pyplot.clf()
for i in range(n):
    pyplot.plot(palabras, matriz[i,:])
    pyplot.show()