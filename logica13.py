num = 100
soma = 0
for num in range(1, num+1):
    tot = 0
    for i in range(2, int(num**0.5)+1):
        if num % i == 0:
            tot += 1
            break
    if tot == 0:
        soma += num
        print(num)
print(soma)