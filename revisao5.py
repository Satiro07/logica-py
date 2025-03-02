def num_inverso(n):
    inv = 0
    while n:
        inv = inv * 10 + n % 10
        n //= 10
    return inv
n = int(input('Digite um valor: '))
print(num_inverso(n))

