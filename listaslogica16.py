def verificar(lista):
    
    c = 0
    r = 0
    for i in range(0, len(lista)):
        if lista[i] == a:
            r += 1
            lista.remove(lista[c])
        c += 1
    return lista



lista = [2, 5, 'abril', 'amanha',33, 1, 3, 4, 6, 6]
a = input('Digite um elemento: ')
print(verificar(lista))