def remover_dups(lista):
    sem_dups = []
    for i, element in enumerate(lista):
        if element not in sem_dups:
            sem_dups.append(element)
    return sem_dups
lista = ['oculos', 'pe', 'mão',
         'oculos', 3, 0, 9,
         5, 3, 5]
print(remover_dups(lista))
