with open('texto.txt', 'w') as arquivo:
    arquivo.write('Escrevendo em um arquivo via Python')

with open('texto.txt', 'a') as arquivo:
    arquivo.write('\nContinuando o texto')