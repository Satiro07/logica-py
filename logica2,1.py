num = 21
soma = 0
while num > 0:
    inv = num % 10
    soma += inv
    num //= 10
print(soma)