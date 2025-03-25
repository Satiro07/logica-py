lista = []
frase = input('Digite uma frase: ').strip().split()
cont = 0
for palavra in frase:
    cont += 1

print(f'A frase {frase.join("-")} tem {cont} palavras')