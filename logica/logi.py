
pontos = ',.;:!?'
frase = input('Digite uma frase: ').lower()
palavras = frase.split()
novas_palavras = []
contagem = 0
for palavra in palavras:
    cont = len(palavra)
    palavra_certa = []
    for i in range(cont):
        print(palavra[i])
        if palavra[i] not in pontos:
            palavra_certa.append(palavra[i])
    novas_palavras.append(palavra_certa)
print(novas_palavras)