from numpy import *

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

def frecuencia_relativa(matriz):
    return matriz/matriz.sum(axis=0)

n = int(input())
palabras = input().split()
m = len(palabras)
productos,matriz = read_matrix(n,m)
print(palabras)
print(matriz)
print(productos)