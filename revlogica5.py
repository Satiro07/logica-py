num = 2561
inv = 0
while num:
    inv = inv * 10 + num % 10
    num//= 10
print(inv)