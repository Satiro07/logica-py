


lista = [2, 5, 'abril', 'amanha',33, 1, 3, 4, 6, 6]
a = input('Digite um elemento: ')

tot = len(lista)
r = 0
for i in range(0, tot):
    if a != lista[i]:
        r += 1
    else:
        lista.remove(a)
    tot = len(lista)
        
print(lista)