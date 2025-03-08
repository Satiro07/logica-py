def menor(lista):
    cont = 0
    while cont <= len(lista):
        menor = 0
        for i in range(0, len(lista)):
            if i == 0:
                menor = lista[i]
            else:
                if lista[i] <= menor:
                    menor = lista[i]
        cont += 1       
    return menor
nuns = [9, 8, 4, 6, 3, 5, 2, 3, 4, 7, 9]
c = 0
for i in range(0, len(nuns)):
    lei = len(nuns) - c
    if nuns:
        minimo = menor(nuns[0:lei])
        nuns.append(minimo)
        nuns.remove(minimo)
    c += 1
print(nuns)