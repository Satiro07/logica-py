lista = [4, 4, 4, 4, 4, 4, 5, 5, 5, 5, 5, 5]
venc = []
num = 0
t = False
for i in range(0, len(lista)): 
    cont = lista.count(lista[i])
    if num == lista[i]:
        continue
    elif cont >= len(lista)/2:
        venc.append(lista[i])
        num = lista[i]
        t = True
if t == False:
    print(f'Não há vencedor')
elif len(venc) == 1:
    print(f'Vencedor: {venc}')
else:
    print(f'Empate entre os números {venc}')