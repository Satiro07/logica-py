def remover_dups(lista):
    lista = lista[::-1]    
    for i, element in enumerate(lista):
        if lista.count(element) > 1:
            lista.remove(element)
    return lista[::-1]
lis = ['oculos', 'pe', 'mão',
         'oculos', 3, 0, 9,
         5, 3, 5]
print(remover_dups(lis))
#'correto'---^
