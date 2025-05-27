
pontos = ',.;:!?'
frase = input('Digite uma frase: ').lower()
palavras = frase.split()
novas_palavras = []
contagem = 0
for palavra in palavras:
    palavra_frag = palavra.split()
    cont = len(palavra_frag)
    palavra_certa = []
    for i in range(cont):
        if palavra_frag[i] not in pontos:
            palavra_certa.append(palavra_frag[i])
    novas_palavras.append(palavra_certa)
print(novas_palavras)