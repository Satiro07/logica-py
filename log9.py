lista = [2, 3, 5, 3, 2, 7, 6]
lista_sem_par = []
for i in range(0, len(lista)):
    cont = lista.count(lista[i])
    if cont == 1:
        lista_sem_par.append(lista[i])
print(lista_sem_par)