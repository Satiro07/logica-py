lista = [1, 5, 'abril', 'amanha', 33]

a = input('Digite um valor: ')
b = input('Digite um valor: ')

for i in range(0, len(lista)):
    
    if str(lista[i]) == a:
        lista[i] = b
    
print(lista)