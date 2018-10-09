from numpy import *
from matplotlib import pyplot

def procesar_datos(datos):
    dicc = {}
    nombre, info = datos.split(":")
    notas = info.split(",")
    for nota in notas:
        nota, evaluacion = nota.split()
        dicc[evaluacion] = float(nota)
    return nombre, dicc

def todas_las_evaluaciones(lista):
    llaves = []
    for dicc in lista:
        for evaluacion in dicc:
            if evaluacion not in llaves:
                llaves.append(evaluacion)
    llaves.sort()
    return llaves

def barras(labels,valores):
    pyplot.bar(labels,valores)
    pyplot.show()


informacion = []
nombres = []
n = 0
while True:
    data = input()
    if data == "FIN":
        break
    nombre, info = procesar_datos(data)
    nombres.append(nombre)
    informacion.append(info)
    n += 1
evaluaciones = todas_las_evaluaciones(informacion)
print(evaluaciones)
matriz = zeros((n,len(evaluaciones)),dtype=float)
for i in range(n):
    for j in range(len(evaluaciones)):
        diccionario = informacion[i]
        evaluacion = evaluaciones[j]
        if evaluacion not in diccionario:
            matriz[i, j] = 1.0
        else:
            matriz[i, j] = diccionario[evaluacion]
print(matriz)
print(nombres)
promedio_por_evaluaciones=matriz.sum(axis=0)/len(nombres)
promedio_por_alumnos=matriz.sum(axis=1)/len(evaluaciones)
barras(evaluaciones,promedio_por_evaluaciones)
barras(nombres,promedio_por_alumnos)
