def palindromo(num):
    inv = 0
    nume = num
    while nume:    
        inv = inv * 10 + nume % 10
        nume //= 10
    return inv
num = int(input('Digite um valor: '))
resp = palindromo(num)
if resp == num:
    print(f'O número {num} é palindromo {resp}')
else:
    print(f'O número {num} não é palindromo {resp}')