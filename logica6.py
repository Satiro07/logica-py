num = 2
tot = 0
cont = 0
while cont <= num:
    if num % cont+1 == 0:
        tot += 1
    cont +=1
if tot == 2:
    print(f'O número {num} é primo')
else:
    print(f'O número {num} não é primo')