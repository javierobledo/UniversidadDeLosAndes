n = int(input())
diccionario = leer_votos(n)
lista = list(diccionario.items())
lista.sort(key=lambda tup:tup[1],reverse=True)
for elemento in lista:
    print(elemento[0],elemento[1])