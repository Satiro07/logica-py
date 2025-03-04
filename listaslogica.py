nuns = [1, 2, 3, 4, 5,
        6, 7, 8, 9, 10,
        11, 12, 13, 14, 15,
        16, 17, 18, 19, 20]
pares = []
for i in range(1, len(nuns)+1):
    if i % 2 == 0:
        pares.append(i)
print(pares)