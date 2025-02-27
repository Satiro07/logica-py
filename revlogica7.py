num = 158
nume = num
numero = num
tot = 0
soma = 0
while nume:
    nume //= 10
    tot += 1
while numero:
    numer = numero % 10
    mult = numer ** tot
    soma += mult
    numero //= 10
if num == soma:
    print(f'O número {num} é armstrong a soma deu {soma}')
else:
    print(f'O número {num} não é armstrong a soma deu {soma}')