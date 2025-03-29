from random import randint
def gerador_senha(num):
    senha = []
    caracters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZÇabcdefghijklmnopqrstuvwxyzç1234567890!@#$%&'
    for i in range(0, num):
        escolha_caracter = randint(0, 67)
        senha.append(caracters[escolha_caracter])
    senha_final = ''
    x = senha_final.join(senha)
    return x

quantidade_de_caracteres = int(input('Quantidade de caracteres você quer para sua senha? '))
resp = gerador_senha(quantidade_de_caracteres)
if quantidade_de_caracteres > 0:
    print(f'Senha gerada: {resp}')
else:
    print('Quantidade de caracteres tem que ser maior que 0')