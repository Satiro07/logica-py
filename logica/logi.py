
pontos = ',.;:!?'
frase = input('Digite uma frase: ').lower()
palavras = frase.split()
novas_palavras = []
contagem = 0
for palavra in palavras:
    cont = len(palavra)
    palavra_certa = []
    for i in range(cont):
        if len(palavra) > 1:
            if palavra[i] not in pontos:
                palavra_certa.append(palavra[i])
        else:
            break
    correto = ''
    for letra in palavra_certa:
        correto += letra
    if correto != '':
        novas_palavras.append(correto)
palavras_palindromo = []
for palavra in novas_palavras:
    if palavra == palavra[::-1]:
        palavras_palindromo.append(palavra)

if palavras_palindromo:
    print('palavras palindromas')
    print(palavras_palindromo)
else:
    print('A frase nao possui palavras palindromas')