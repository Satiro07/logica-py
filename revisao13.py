def soma_primos(num):
    soma = 0
    for num in range(2, num+1):
        tot = 0
        for i in range(2, int(num**0.5)+1):
            if num % i == 0:
                tot += 1
                break
        if tot == 0:
            print(num)
            soma += num
    print(soma)
num = int(input('Digite um valor: '))
print(soma_primos(num))