from numpy import *
from matplotlib import pyplot

def read_matrix(n,m):
    matriz = zeros((n, m), dtype=int)
    paises = []
    for i in range(n):
        datos = input().split()
        pais = datos[0]
        numeros = datos[1:]
        for j in range(m):
            matriz[i, j] = int(numeros[j])
        paises.append(pais)
    return paises,matriz

datos = ["G","E","P","GF","GC"]
paises,matriz = read_matrix(4,len(datos))
print(datos)
print(matriz)
print(paises)
puntos = 3*matriz[:,0]+matriz[:,1]
pyplot.bar(paises,puntos)
pyplot.show()
pyplot.clf()
diferencia = matriz[:,3]-matriz[:,4]
pyplot.plot(paises,diferencia)
pyplot.show()
pyplot.clf()