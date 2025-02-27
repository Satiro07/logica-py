while True:
    cont = 1
    num = int(input('Número: '))
    while cont <= num:
        if num % cont == 0:
            print(cont)
        cont += 1
    if num == 0:
        break