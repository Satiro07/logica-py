geral = []
while True:
    sistema = {}
    notas = []
    nome = input('Nome do aluno: ')
    c = 0
    while c < 3:
        nota = float(input('Nota do aluno: '))
        notas.append(nota)
        c += 1
    sistema[nome] = notas
    geral.append(sistema)
    add_aluno = input('Adicionar outro aluno? [s/n] ').lower()
    if add_aluno == 'n':
        break

aluno_maior_media = ''
media_maior = 0
for nota in geral:
    for k, v in nota.items():
        soma = sum(v)
        media = soma / len(v)
        print(f'Nome do aluno: {k}, Média: {media:.2f}')
        if media >= media_maior:
            media_maior = media
            aluno_maior_media = k
print(f'O aluno com a maior média foi {aluno_maior_media} = {media_maior:.2f}')