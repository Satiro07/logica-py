def somar_numeros():
    soma = 0
    while True:
        num = int(input('Digite um valor: '))
        if num == 0:
            break
        soma += num
    print(soma)
somar_numeros()