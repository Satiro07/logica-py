def fibonacci(n):
    fib = []
    c = 0
    atual = 0
    at = 1
    while c < n:
        atuali = atual + at
        fib.append(atuali)
        at = atual
        atual = atuali
        c += 1
    return fib

n = int(input('Quantos números de fibonacci? '))
print(fibonacci(n))