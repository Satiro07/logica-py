geral = []
while True:
    sistema = {}
    notas = []
    nome = input('Nome do aluno: (ou "s" para sair)')
    if nome == 's':
        break
    print('Escreva "-1" para sair')
    while nome != 's':
        nota = float(input('Nota do aluno: '))
        if int(nota) < 0:
            break
        notas.append(nota)
    sistema[nome] = notas
    geral.append(sistema)
    
print('Média dos alunos:')
for nota in geral:
    for k, v in nota.items():
        soma = sum(v)
        media = soma / len(v)
        print(f'{k}: {media:.2f}')
