n = 99
n_test = n
nnnn = n
nn = n
tot = 0
dez = 1
while nnnn:
    n_test = nnnn % 10
    nnnn //= 10
    dez *= 10
while tot != 3:
    print(nn)
    nn = nn * dez + n
    tot += 1