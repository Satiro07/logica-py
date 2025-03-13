def substituir(lista):
    c = 0
    for i in range(0, len(lista)):
        carac = len(lista) - c
        if lista:
            remo = lista[0:carac]
            lista.remove(remo[-1])
            lista.append('x')
        c += 1
    return lista

lista = [1, 5, 'abril', 'amanha', 33]
print(substituir(lista))