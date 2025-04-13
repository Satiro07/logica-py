num = int(input('Digite um valor: '))
copia_num = copia = num
soma_f = cont =  0
while True:
    soma = digs = c = 0
    while copia_num:
        copia_num //= 10
        digs += 1
    if digs > 1:
        for c in range(0, digs):
            digito = copia % 10
            soma += digito
            copia //=10
    else:
        if cont == 0:
            print(num)
        else:
            print(soma_f)
        break
    copia_num = copia = soma_f = soma
    cont += 1