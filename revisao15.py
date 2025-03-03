def mostrar_n_primos(num):
    cont = 0
    nume = 2
    while nume:
        tot = 0
        for i in range(2, int(nume**0.5)+1):
            if nume % i == 0:
                tot += 1
                break
        if tot == 0 and num > cont:
            print(nume)
            cont += 1
        nume += 1
        
num = int(input('Digite um valor: '))
print(mostrar_n_primos(num))