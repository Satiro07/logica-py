geral = []
sistema = {}

for i in range(0, 2):
    notas = []
    sistema['nome'] = input('Nome do aluno: ')
    c = 0
    while c < 3:
        nota = float(input('Nota do aluno: '))
        notas.append(nota)
        c += 1
    sistema['nome'] = notas
    geral.append*sistema
print(geral)