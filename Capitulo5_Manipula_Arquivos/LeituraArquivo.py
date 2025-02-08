with open('texto.txt', 'r') as arquivo:
    conteudo = arquivo.readlines()
print('Tipo de dado de variável', type(conteudo))
print('\nConteúdo do arquivo: \n', conteudo)