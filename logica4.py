while True:
    num = int(input('número: '))
    if num == 0:
        break
    cont = 1
    while cont <= num:
        if num % cont == 0:
            print(cont)
        cont += 1
        
    
