def remover(lista):
    lista = lista[::-1]
    for element in range(0, len(lista)):
        if lista.count(element) > 1:
            lista.remove(element)
    return lista[::-1]
lista1 = [2, 5, 'abril', 'amanha', 33, 5, 1, 2, 3, 4, 5, 6]
print(lista1)
print(remover(lista1))