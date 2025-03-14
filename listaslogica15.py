def repetidos(lista):
    r = 0
    cont = 0
    tudo = len(lista)
    while cont < tudo:
        for i in range(1, len(lista)):
            if lista[0] == lista[i]: 
                r +=1
        lista.remove(lista[0])
        cont += 1
    if r >= 1:
        return True 
lista1 = [2, 5, 'abril', 'amanha',33, 1, 3, 4, 6, 6]
resp = repetidos(lista1)
if resp == True:
    print('tem elementos repetidos')
else:
    print('nao tem elementos repetidos')