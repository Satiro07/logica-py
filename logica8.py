num = 50
ini = 1
cont = 1
while cont <= num:
    tot = 0
    for i in range(2, int(num**0.5)+1):
        if num % i == 0:
            tot += 1 
            break
    cont += 1
    if tot == 0:
        print(num)


        

