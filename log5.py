def contador_palavras(frase):

    quantidade_palavras = frase.split()
    quantidade_palavras1 = len(quantidade_palavras)
    quantidade_letras_com_espaco = len(frase)
    juntar = ''
    x = juntar.join(quantidade_palavras)
    quantidade_letras_sem_espaco = len(x)
    return quantidade_palavras1, quantidade_letras_com_espaco, quantidade_letras_sem_espaco




frase = 'python é muito divertido'
print(contador_palavras(frase))