while True:
    num = 10
    n1 = 1
    atual = 0
    for i in range(1, num+1):
        atuali = atual + n1
        print(atuali)
        n1 = atual
        atual = atuali     
    break