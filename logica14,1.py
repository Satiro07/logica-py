num = 10
for i in range(1, num+1):
    fat = 1
    print(f'Fatorial de {i}')
    for c in range(i, 0, -1):
        print(c,end=' ')
        fat *= c
        c-=1
    print(f'\nfatorial de {i} é {fat}')
    print()