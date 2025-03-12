def primos(num):
    primos = []
    for num in range(2, num+1):
        tot = 0
        for i in range(2, int(num**0.5)+1):
            if num % i == 0:
                tot += 1
                break
        if tot == 0:
            primos.append(num)
    return primos
num = 10
print(primos(num))