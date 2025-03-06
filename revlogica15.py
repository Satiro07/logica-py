num = 7
nume = 2
cont = 1
while nume:
    tot = 0
    for i in range(2, int(nume**0.5)+1):
        if nume % i == 0:
            tot += 1
            break
    if tot == 0 and cont <= num:
        print(nume)
        cont += 1
    nume += 1
