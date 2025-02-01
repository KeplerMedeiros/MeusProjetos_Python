inventario = []
resposta = 'S'
while resposta == 'S':
    inventario.append(input('Equipamento: '))
    inventario.append(float(input('Valor: ')))
    inventario.append(int(input('Número Serial: ')))
    inventario.append(input('Departamento: '))
    resposta = input('Digite \'S\' para continuar: ').upper()

#O for é mais indicado para percorrer a lista e exibir tudo o que está armazenado nela
for elemento in inventario:
    print(elemento)