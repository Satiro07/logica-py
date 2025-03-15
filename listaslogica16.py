def verificar(lista, a):
    c = 0
    while c <= len(lista)-1:
        if str(a) == str(lista[c]):
            lista.remove(lista[c])
        else:
            c += 1
    return lista


lista = [7, 7, 0]
a = input('Digite um elemento: ')
print(verificar(lista, a))