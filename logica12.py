num = 15
tot = 0
for c in range(1, num+1):
    if num % c == 0:
        tot += 1
if tot == 2:
    print(f'o número {num} é primo')
else:
    print(f'o número {num} não é primo')