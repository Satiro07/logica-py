num = 100
soma = 0
for num in range(2, num+1):
    tot = 0
    for i in range(2, int(num**0.5)+1):
        if num % i == 0:
            tot += 1
    if tot == 0:
        print(num)
        soma += num
        
print(soma)