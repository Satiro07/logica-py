n = 5920
soma = 0
if n:
    num = n // 1000
    soma += num
    num = n % 1000
    if num :
        nume = num // 100
        soma += nume
        num = num % 100
        if num:
            nume = num // 10
            soma += nume
            num = num % 10
            if num:
                soma += num
print(soma)

