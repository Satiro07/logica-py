def fatorial(num):
    cont = 1
    fat = 1
    while num >= 1:
        fat *= num
        print(num)
        num -= 1
    print(fat)
num = int(input('Digite um valor: '))
print(fatorial(num))
