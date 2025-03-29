def contar_vogais(texto):
    vogais = 'aeiouáéíóúãâêîôûõàèìòù'
    contador = 0
    for palavra in texto:
        for letra in palavra:
            if letra in vogais:
                cont = letra.count(letra)
                contador += cont
    return contador

frase = input('Digite algo: ').lower().split()
resp = contar_vogais(frase)
print(resp)
