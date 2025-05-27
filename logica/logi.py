
pontos = ',.;:!?'
frase = input('Digite uma frase: ').lower()
palavras = frase.split()
novas_palavras = []
for palavra in palavras:
    verificacao = False
    for i in range(len(palavra)):
        if palavra[i] in pontos:
            palavra.remove(palavra[i])
            novas_palavras.append(palavra)
            verificacao = True
    if verificacao == False:
        novas_palavras.append(palavra)
print(novas_palavras)