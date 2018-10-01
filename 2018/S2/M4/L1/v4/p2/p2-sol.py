def leer_votos(n):
    diccionario = {}
    for i in range(n):
        n = input()
        if n not in diccionario:
            diccionario[n] = 1
        else:
            diccionario[n] += 1
    return diccionario

n = int(input())
diccionario = leer_votos(n)
lista = list(diccionario.items())
lista.sort(key=lambda tup:tup[1],reverse=True)
for elemento in lista:
    print(elemento[0],elemento[1])