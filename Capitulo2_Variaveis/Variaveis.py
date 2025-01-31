# nome = 'Kepler Medeiros'
# empresa = 'BB'
# qtde_funcionarios = 500
# mediaMensalidade = 856.50
# print(nome + ' trabalha na empresa ' + empresa) Strings são concatenadas com sinal +
# print('Possui', qtde_funcionarios, 'funcionários.') inteiros são concatenadas com ,
# print('A média da mensalidade é de R$ ' + str(mediaMensalidade)) transformando um float em string e usando + para concatenar

nome = input('Digite o nome do funcionário: ')
empresa = input('Digite o nome da empresa: ')
qtde_funcionarios = int(input('Digite a quantidade de funcionários: ')) # O input sempre gera uma string. O int transforma a string em int
mediaMensalidade = float(input('Digite a média da mensalidade: ')) # Usa-se o . para separar casas decimais
print(nome + ' trabalha na empresa ' + empresa)
print('Possui', qtde_funcionarios, 'funcionários.')
print('A média da mensalidade é de R$ ' + str(mediaMensalidade))
print('====================Verificação dos tipos de dados abaixo:====================')
print('O tipo de dado da variável [nome] é: ', type(nome))
print('O tipo de dado da variável [empresa] é: ', type(empresa))
print('O tipo de dado da variável [qtde_funcionarios] é: ', type(qtde_funcionarios))
print('O tipo de dado da variável [mediaMensalidade] é: ', type(mediaMensalidade))