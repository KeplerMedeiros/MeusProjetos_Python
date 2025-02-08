from IdentificacaoDeFuncoes import *

minhaLista = []
print('\nPreenchendo')
preencherInventario(minhaLista)
print('\nExibindo')
exibirInventario(minhaLista)

print('\nPesquisando')
localizarPorNome(minhaLista)
print('\nAlterando')
depreciarPorNome(minhaLista, 20)

print('\nExcluindo')
print(excluirPorSerial(minhaLista))
exibirInventario(minhaLista)

print('\nResumindo')
resumirValores(minhaLista)