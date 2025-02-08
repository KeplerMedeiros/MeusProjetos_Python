import sys, os
sys.path.insert(0,os.path.abspath(os.curdir))

# Utilizando a funçao do módulo Funcoes.py
from Funcoes.Funcoes_Dicionarios import *

usuarios = {}
opcao = perguntar()

# opcao = input('O que deseja realizar?\n'+
#               '<I> - Para inserir um usuário\n'+
#               '<P> - Para pesquisar um usuário\n'+
#               '<E> - Para excluir um usuário\n'+
#               '<L> - Para listar um usuário: ').upper()
while opcao == 'I' or opcao == 'P' or opcao == 'E' or opcao == 'L':
    if opcao == 'I':
        inserir(usuarios)
    if opcao == 'P':
        pesquisar(usuarios, input('Qual login deseja pesquisar? '))
    if opcao == 'E':
        excluir(usuarios, input('Qual login deseja excluir? '))
    if opcao == 'L':
        listar(usuarios)
    opcao = perguntar()
        # chave = input('Digite o login: ').upper()
        # nome = input('Digite o nome: ').upper()
        # data = input('Digite a última data de acesso: ')
        # estacao = input('Qual a última estação acessada: ')
        # usuarios[chave] = [nome, data, estacao]

        # chave=input("Digite o login: ").upper()
        # usuarios[chave]=[input("Digite o nome: ").upper(),
        #                  input("Digite a última data de acesso: "),
        #                  input("Qual a última estação acessada: ").upper()]
    # opcao = input("O que deseja realizar?\n" +
    #               "<I> - Para Inserir um usuário\n" +
    #               "<P> - Para Pesquisar um usuário\n" +
    #               "<E> - Para Excluir um usuário\n" +
    #               "<L> - Para Listar um usuário: ").upper()


