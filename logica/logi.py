
pontos = ',.;:!?'
frase = input('Digite uma frase: ').lower()
palavras = frase.split()
novas_palavras = []
for palavra in palavras:
    verificacao = False
    palavra_completa = palavra
    for i in range(len(palavra)):
        if palavra[i] in pontos:
            palavra_completa.remove(palavra_completa[i])
            novas_palavras.append(palavra_completa)
            verificacao = True
    if verificacao == False:
        novas_palavras.append(palavra_completa)
print(novas_palavras)