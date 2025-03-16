def verificar(lista, a):
    c = 0
    while c <= len(lista)-1:
        if str(a) == str(lista[c]):
            lista.remove(lista[c])
        else:
            c += 1
    return lista


lista = [2, 5, 7, 'abril', 33, 1, 3,'abril', 4, 7, 7]
a = input('Digite um elemento: ')
print(verificar(lista, a))