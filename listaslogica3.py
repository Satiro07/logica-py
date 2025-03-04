palavra = str(input('Palavra: ')).lower()
alfabeto = ['a', 'b', 'c', 'd',
            'e', 'f', 'g', 'h',
            'i', 'j', 'k', 'l',
            'm', 'n', 'o', 'p',
            'q', 'r', 's', 't',
            'u', 'v', 'w', 'x',
            'y', 'z']
pares = []
for i, letras in enumerate(alfabeto):
    if letras in palavra:
        print(f'{letras}: {palavra.count(letras)}')
        # pares.append(letras)
        # pares.append(palavra.count(letras))
# cont = 0
# while cont <= len(pares):
#     print(f'{pares[cont]}: {pares[cont+1]}')
#     cont += 2
#     if cont == len(pares):
#         break

