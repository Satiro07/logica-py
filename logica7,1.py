num = 1535454
nume = num
numero = nume
tot = 0
soma = 0
while numero > 0:
    inv = numero % 10
    tot +=1
    numero //= 10
while num > 0:
    inv = num % 10
    mult = inv ** tot
    soma += mult
    num //= 10
if nume == soma:
    print(f'O número {nume} é armstrong a soma deu {soma}')
else:
    print(f'O número {nume} não é armstrong a soma deu {soma}')