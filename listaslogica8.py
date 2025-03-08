def menor_maior(lista):
    cont = 0
    while cont <= len(lista):
        menor = maior = 0
        for i in range(0, len(lista)):
            if i == 0:
                menor = lista[i]
                maior = lista[i]
            else:
                if lista[i] <= menor:
                    menor = lista[i]
                if lista[i] >= maior:
                    maior = lista[i]
        cont += 1
    return menor, maior
nuns = [0, -3, -100, 100, 2, 0, -4]
print(menor_maior(nuns))