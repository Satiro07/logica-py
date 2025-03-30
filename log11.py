num = int(input('Digite um número: '))
raiz = num ** 0.5
if num < 0:
    print(False)
elif int(raiz) ** 2 == num:
    print(True)
else:
    print(False)
