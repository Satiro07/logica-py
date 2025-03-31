lista = [100, 4, 200, 1, 3, 2]
seq_f = []
minimo = min(lista)
for i in range(0, len(lista)-1):
    seq = []
    c = 0
    numero = lista[i]
    t = False
    while c < len(lista):
        numero = lista[i]
        if numero == lista[c]-1 or numero == lista[c]+1:
            seq.append(lista[c])
            t = True
        if t == True:
            numero = lista[c]
        else:
            
        c += 1
    if len(seq) > len(seq_f):
        seq_f = seq
print(sorted(seq_f))
print()