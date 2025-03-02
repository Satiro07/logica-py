def multiplos(n):
    for i in range(1, n+1):
        if n % i == 0:
            print(i)
n = int(input('Digite um valor: '))
print(multiplos(n))