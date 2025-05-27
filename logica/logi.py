
pontos = ',.;:!?'
frase = input('Digite uma frase: ').lower()
palavras = frase.split()
novas_palavras = []
for palavra in palavras:
    pala = palavra.split()
    print(pala)
print(frase)