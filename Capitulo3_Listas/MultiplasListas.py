equipamentos = []
valores = []
seriais = []
departamentos = []

resposta = 'S'
while resposta == 'S':
    equipamentos.append(input('Equipamento: ').upper())
    valores.append(float(input('Valor: ')))
    seriais.append(int(input('Número Serial: ')))
    departamentos.append(input('Departamento: ').upper()    )   
    resposta = input('Digite \'S\' para continuar: ').upper()

# for equipamento in equipamentos:
#     print('Equipamento: ', equipamento)
# for valor in valores:
#     print('Valor: ', valor)
# for serial in seriais:
#     print('Número Serial: ', serial)
# for departamento in departamentos:
#     print('Departamento ', departamento)

#para trabalhar de acordo com o índice e não com base nos elementos diretamente
for indice in range (0, len(equipamentos)):
    print('\nEquipamento..: ', (indice+1))
    print('Nome...........: ', equipamentos[indice])
    print('Valor..........: ', valores[indice])
    print('Serial.........: ', seriais[indice])
    print('Departamento...: ', departamentos[indice])

busca = input('\nDigite o nome do equipamento que deseja buscar: ').upper()
for indice in range (0, len(equipamentos)):
    if busca == equipamentos[indice]:
        print('Valor..: ', valores[indice])
        print('Serial.: ', seriais[indice])

serial = int(input('\nDigite o serial do equipamento que será excluído: '))
for indice in range (0, len(departamentos)):
    if seriais[indice] != serial:
        print(input('Digite um serial válido: '))
    elif seriais[indice] == serial:
        del departamentos[indice]
        del equipamentos[indice]
        del seriais[indice]
        del valores[indice]
        break

depreciacao = input('\nDigite o nome do equipamento que será depreciado: ').upper()
for indice in range (0, len(equipamentos)):
    if depreciacao == equipamentos[indice]:
        print('Valor antigo: ', valores[indice])
        valores[indice] = valores[indice] * 0.9
        print('Novo valor: ', valores[indice])
