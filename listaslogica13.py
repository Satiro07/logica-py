lista1 = [2, 5, 'abril', 'amanha', 33]
lista = lista1

lista2 = [1, 2, 3, 4, 5]
lista22 = lista2
lista12 = lista2
for i in range(5):
    
    lista12[i] = lista1[i]
for i in range(5):
    lista1[i] = lista12[i]
    lista2[i] = lista12[i]
    
    
print(lista1)
print(lista)
print(lista2)
print(lista22)