from numpy import *

def read_matrix(n,m):
    matriz = zeros((n, m), dtype=int)
    for i in range(n):
        numeros = input().split()
        for j in range(m):
            matriz[i, j] = int(numeros[j])
    return matriz

def frecuencia_relativa(matriz):
    return matriz/matriz.sum(axis=0)

n = int(input())
palabras = input().split()
m = len(palabras)
matriz = read_matrix(n,m)
print(frecuencia_relativa(matriz))