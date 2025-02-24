num = int(input('número: '))
soma = 0
for c in range(1, num+1):
    if c % 2 == 0:
        print(c)
        soma += c
print(soma)