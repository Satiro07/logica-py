# 2. Palíndromo Binário (Nível Intermediário)
# Um número é considerado um palíndromo binário se, quando convertido para binário, a leitura é a mesma da esquerda para a direita e da direita para a esquerda.

# Exemplo:

# 9 em binário é 1001, que é um palíndromo.

# Entrada: Um número inteiro positivo 
# 𝑁
# N (1 ≤ N ≤ 1000)
# Saída: "SIM" se o número for um palíndromo binário, ou "NAO" caso contrário.

# 📌 O que o programa deve imprimir para a entrada 17?

numero = 5
resto = numero
binario = 0
cont = 1
while resto % 2 != 0:
    binario = (resto % 2) * cont
    resto = resto // 2
    cont *= 10
print(binario)