def num_primo(n):
    tot = 0
    for i in range(2, int(n**0.5)+1):
        if n % i == 0:
            tot += 1
    return tot
n = int(input('Digite um valor: '))
resp = num_primo(n)
if resp == 0:
    print(f'O número {n} é primo')
else:
    print(f'O número {n} não é primo')


