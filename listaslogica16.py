def verificar(lista, a):
    
    c = 0
    r = 0
    tot = len(lista)
    for i in range(0, tot):
        if a != lista[i]:
            r += 1
        else:
            lista.remove(a)
        tot = len(lista)
        c += 1
    return lista



lista = [2, 5, 'abril', 'amanha',33, 1, 3, 4, 6, 6]
a = input('Digite um elemento: ')
print(verificar(lista, a))