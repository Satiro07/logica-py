def sequencia_fibonacci():
    n = 10
    atual = 0
    n1 = 1
    cont = 1
    while cont <= n:
        atuali = atual + n1
        print(atuali)
        n1 = atual
        atual = atuali
        cont += 1
sequencia_fibonacci()