# Na primeira linha, estamos criando o dicionário de
# dados. Repare que, em vez de utilizarmos os colchetes (como fizemos com as
# listas), usamos as chaves “{}”, essa é a representação de um dicionário de dados.
usuarios = {}
usuarios = {
    'Chaves': ['Chaves Silva', '17/06/2017', 'Recep_01'], 
    'Quico': ['Enrico Flores', '03/06/2017', 'Raiox_02']
# Caso houver dois objetos com a mesma chave, o segundo objetoirá sobrescrever o primeiro.
}

# Adicionando elementos:
usuarios['Florinda'] = ['Florinda Flores', '26/11/2017', 'Recep_01']

# Retornar os dados de um objeto da lista:
print(usuarios)
print('##########==========###########')
print('Dados: ', usuarios.get('Chaves'))
