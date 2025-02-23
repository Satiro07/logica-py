num = 5
total = 0
cont = 1
while cont <= num:
    if num % cont == 0:
        total += 1
    cont += 1
    
if total == 2:
    print(f'O número {num} é primo')
else:
    print(f'O número {num} não é primo')
