lista = [1,2,3,5,7,9]
for i in range(1, len(lista)):
    if lista[i-1] != lista[i]-1:
        print(f'{lista[i-1]+1}')