def sequencia_fibonacci(num):
    while True:
        n1 = 1
        atual = 0
        for i in range(1, num+1):
            atuali = n1 + atual
            print(atuali)
            n1 = atual
            atual = atuali
        break
num = int(input('Digite um valor: '))
print(sequencia_fibonacci(num))