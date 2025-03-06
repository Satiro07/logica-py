nuns = [9, 8, 4, 6, 3, 5, 1, 2, 3, 4, 7, 9]
c = 0
for i in range(0, len(nuns)):
    lei = len(nuns) - c
    if nuns:
        minimo = min(nuns[0:lei])
        nuns.append(minimo)
        nuns.remove(minimo)
    c += 1
print(nuns)
