def remover_duplicados(lista):
    sem_duplicados = []
    for c in range(0, len(lista)):
        if lista[c] not in sem_duplicados:
            sem_duplicados.append(lista[c])
    return sem_duplicados

lista = [1, 2, 3, 2, 4, 1, 5]
print(remover_duplicados(lista))