def soma_digitos(num):
    soma = 0
    while num:
        n = num
        n %= 10
        soma += n
        num //= 10
    return soma
num = int(input('Digite um valor: '))
print(soma_digitos(num))
