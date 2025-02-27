num = 10146
nume = num
inv = 0
while nume:
    inv = inv * 10 + nume % 10
    nume //= 10
if inv == num:
    print(f'o número {num} é palindromo')
else:
    print(f'o número {num} não é palindromo')