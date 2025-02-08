# import json
# inventario={}
# opcao=int(input("Digite: "
#                 "\n<1> para registrar ativo"
#                 "\n<2> para exibir ativos armazenados: "))
# while opcao>0 and opcao<3:
#     if opcao==1:
#         resp = "S"
#         while resp == "S":
#             inventario[input("Digite o número patrimonial: ")] = [
#                 input("Digite a data da última atualização: "),
#                 input("Digite a descrição: "),
#                 input("Digite o departamento: ")]
#             resp = input("Digite <S> para continuar.").upper()
#         with open("inventario_json.json", "w") as arq_json:
#             json.dump(inventario, arq_json)
#         print("JSON gerado!!!!")
#     elif opcao==2:
#         with open("inventario_json.json", "r") as arq_json:
#             resultado = json.load(arq_json)
#             for chave, dado in resultado.items():
#                 print("Data.........: ", dado[0])
#                 print("Descrição....: ", dado[1])
#                 print("Departamento.: ", dado[2])
#     opcao = int(input("Digite: "
#                   "\n<1> para registrar ativo"
#                   "\n<2> para exibir ativos armazenados: "))  

# Comando para executar chamada de módulos:    
import sys, os
sys.path.insert(0,os.path.abspath(os.curdir))

from Funcoes.Funcoes_JSON import *
inventario = ler_arquivo("inventario_json.json")
opcao=chamarMenu()
while opcao>0 and opcao<3:
    if opcao==1:
        print(registrar(inventario, "inventario_json.json"))
    elif opcao==2:
        exibir("inventario_json.json")
    opcao = chamarMenu()