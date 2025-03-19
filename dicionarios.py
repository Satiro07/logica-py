sistema = {}
notas = []
for i in range(0, 2):
    sistema['nome'] = input('Nome do aluno: ')
    c = 0
    notas.clear()
    while c < 3:
        nota = float(input('Nota do aluno: '))
        notas.append(nota)
        c += 1
        sistema['nota'] = notas
    
    
print(sistema)