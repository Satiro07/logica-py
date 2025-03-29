def primo(n):
    primos = []
    contador = 0
    i = 2
    while True:
        c = 0
        for num in range(1, i+1):
            if i % num == 0:
                c += 1
        if c == 2:
            primos.append(i)
            contador += 1
        if len(primos) == n:
            break
        i += 1
    return primos
n = int(input('Quantos números primos? '))
print(primo(n))
