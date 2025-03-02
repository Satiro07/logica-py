def mostrar_n(n):
    tot = 0
    nn = n
    nnn = n
    dez = 1
    while nn:
        n1 = nn
        n1 %= 10
        nn //= 10
        n1 = nn
        dez *= 10
    while tot < 3:
        print(nnn)
        nnn = nnn * dez + n
        tot += 1
        
n = int(input('Digite: '))
print(mostrar_n(n))