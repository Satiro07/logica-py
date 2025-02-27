num = 101
nume = num
pali = 0
while nume > 0:
    pali = pali * 10 + nume % 10
    nume //= 10
if pali == num:
    print(f'O número {num} é palíndromo')
else:
    print(f'O número {num} não é palíndromo')