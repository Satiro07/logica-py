


lista = [2, 5, 'abril', 'abril', 33, 1, 3, 4, 6, 6]
a = input('Digite um elemento: ')


c = 0
tot = len(lista)

while c <= tot-1:
    if a == str(lista[c]):
        lista.remove(a)
        c -= 1
    tot = len(lista)
    c += 1
        
print(lista)