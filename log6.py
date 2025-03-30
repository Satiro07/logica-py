lista = []
numeros = 1
while numeros > 0:
    numeros = int(input('Digite um número ou 0 ou menos para sair: '))
    if numeros > 0:
        lista.append(numeros)
alvo = int(input('Digite um número alvo: '))
c = 0
while c < len(lista):
    verdade = False
    for i in range(0, len(lista)):
        if i == c:
            continue
        elif lista[c] + lista[i] == alvo:
            print(f'{lista[c]} + {lista[i]} = {lista[c]+lista[i]}')
            verdade = True
    c += 1
    if verdade == True:
        print(verdade)
        break