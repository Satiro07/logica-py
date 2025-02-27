num = 8565
nume = num
numero = num
soma = 0
while nume:
    nume = numero % 10
    soma += nume
    numero //= 10
print(soma)