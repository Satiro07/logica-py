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
for nota in geral:
    for k, v in nota.items():
        soma = sum(v)
        media = soma / len(v)
        print(f'{k} media: {media:.2f}')