def armstrong(num):
    numer = num
    soma = 0
    tot = 0
    while num:
        num = num // 10
        tot += 1
    while numer: 
        numero = numer
        numer %= 10
        mult = numer ** tot
        soma += mult
        numer = numero//10
    return soma
num = int(input('Digite um valor: '))
resp = armstrong(num)
if num == resp:
    print(f'O número {num} é armstrong a soma deu {resp}')
else:
    print(f'O número {num} não é armstrong a soma deu {resp}')