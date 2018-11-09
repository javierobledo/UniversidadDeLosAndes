def sum_rec(lista):
    if len(lista) == 0:
        return 0
    return lista[0]+sum_rec(lista[1:])