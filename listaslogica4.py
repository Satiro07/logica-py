lista = [1, 2, 6,
        12, 14, 1,
        2, 6, 17]
print(lista)
sem_dups = []
for i, num in enumerate(lista):
    if num not in sem_dups:
        sem_dups.append(num)
print(sem_dups)
