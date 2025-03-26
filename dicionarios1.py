
lista = []

while True:
    frases = ''
    cont = []
    geral = []
    dicionario = {}
    frase1 = 'n'
    while frase1 != 's':
        frase1 = input('Digite uma frase ou "s" para sair: ').strip()
        frase = frase1.split()
        frases = frase
        cont += frases
        print(frases)
    for palavra in frase:
        palavra_nome = palavra
        pala = frase.count(palavra)
        dicionario[palavra_nome] = pala
    geral.append(dicionario)
    lista.append(geral)
    break
print()
print(lista)