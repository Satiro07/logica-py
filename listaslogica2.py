palavras = ['cubo', 'cachorro', 'lápis',
            'caderno', 'gato']
novas = []
while palavras:
    palavra = palavras[-1]
    novas.append(palavra)
    palavras.pop()
print(novas)
