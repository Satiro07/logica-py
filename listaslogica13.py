lista1 = [2, 5, 'abril', 'amanha', 33, 5]
lista= []
lista2 = [1, 2, 3, 4, 5, 6]
for i in range(0, len(lista1)):
    lista = lista1[i]
    lista1[i] = lista2[i]
    lista2[i] = lista
print(lista1)
print(lista2)