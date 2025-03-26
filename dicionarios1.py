lista = []
while True:
    cont = []
    dicionario = {}
    frase1 = 'n'
    while frase1 != 's':
        frase1 = input('Digite uma frase ou "s" para sair: ').strip().lower()
        if frase1 == 's':
            break
        frase = frase1.split()
        cont += frase
    for palavra in cont:
        palavra_nome = palavra
        pala = cont.count(palavra)
        dicionario[palavra_nome] = pala
    lista.append(dicionario)
    break

for palavra in lista:
    for k, v in palavra.items():
        print(f'{k}: {v}')