while True:
    num = 5
    n1 = 1
    atual = 0
    for c in range(1, num+1):
        atuali = atual + n1
        print(atuali)
        n1 = atual
        atual = atuali
    break