palavra = str(input('Palavra: ')).lower()
alfabeto = ['a', 'b', 'c', 'd',
            'e', 'f', 'g', 'h',
            'i', 'j', 'k', 'l',
            'm', 'n', 'o', 'p',
            'q', 'r', 's', 't',
            'u', 'v', 'w', 'x',
            'y', 'z']
for i, letras in enumerate(alfabeto):
    if letras in palavra:
        print(f'{letras}: {palavra.count(letras)}')