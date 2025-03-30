num = int(input('Digite um valor: '))
copia_num = copia = num
soma_f = 0
cont = 0
while True:
    soma = digs = c = 0
    while copia_num:
        copia_num //= 10
        digs += 1
    if digs > 1:
        while c < digs:
            digito = copia % 10
            soma += digito
            copia //=10
            c += 1
    else:
        if cont == 0:
            print(num)
        else:
            print(soma_f)
        break
    copia_num = copia = soma_f = soma
    cont += 1