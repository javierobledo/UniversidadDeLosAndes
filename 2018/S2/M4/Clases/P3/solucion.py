from numpy import *
from matplotlib import pyplot

#Desarrolle una funcion llamada multiplicacion_por_escalar
#que recibe como entrada una lista de listas de enteros
# y un escalar,  retornando la lista de listas multiplicada
# por el escalar

def multiplicacion_por_escalar(lista, escalar):
    nuevalista = []
    for elemento in lista:
        nuevalista.append(elemento*escalar)
    return nuevalista

#Desarrolle una funcion llamada multiplicacion_por_escalar_v2
#que recibe como entrada una matriz numpy de enteros y retorna
#la matriz multiplicada por un número entero

def multiplicacion_por_escalar_v2(matriz, escalar):
    return escalar*matriz

#Desarrolle una función llamada transpuesta(lista) que recibe como entrada
#una lista de listas y retorna la transpuesta.
def transpuesta(lista):
    nuevalista = []
    n = len(lista)
    m = len(lista[0])
    for j in range(m):
        nuevafila = []
        for i in range(n):
            nuevafila.append(lista[i][j])
        nuevalista.append(nuevafila)
    return nuevalista

#Desarrolle una función llamada transpuesta_v2(matriz) que recibe como entrada
#una matriz y retorna la transpuesta.
def transpuesta_v2(matriz):
    return matriz.transpose()

#Desarrolle una funcion llamada suma_matrices que recibe
#dos listas de listas de enteros y retorna una lista
#de listas con la suma matricial

def suma_matrices(lista1,lista2):
    nuevalista = []
    for i in range(len(lista1)):
        nuevalista.append(lista1[i]+lista2[i])
    return nuevalista

#Desarrolle una funcion llamada suma_matrices_v2 que recibe
#dos matrices numpy de enteros y retorna una matriz
#con la suma matricial

def suma_matrices_v2(matriz1,matriz2):
    return matriz1+matriz2


#Desarrolle una función que recibe como entrada un arreglo
#numpy y permita ver en pantalla un gráfico de línea asociado

def grafico(arreglo):
    pyplot.plot(arreglo)
    pyplot.show()


#Desarrolle una función llamado barras que reciba un diccionario
#cuya llave es el nombre de un alumno y valor la cantidad de clases
#que ha asistito. La función debe mostrar un gráfico de barras
#en donde en el eje x está el nombre de un alumno y las barras
#representen la asistencia

def grafico_barras(diccionario):
    pyplot.plot(diccionario.keys(), diccionario.values())
    pyplot.show()