def fatorial(num):
    mult = 1
    while num >= 1:
        mult *= num
        num -= 1
    return mult
numero = 9
print(fatorial(numero))