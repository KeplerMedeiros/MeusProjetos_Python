# nome = input('Digite o nome: ')
# idade = int(input('Digite a idade: '))
# if idade >= 65:
#     print('O paciente ' + nome + ' POSSUI atendimento prioritário!')
# else:
#     print('O paciente ' + nome + ' NÃO POSSUI atendimento prioritário!')

# nome = input("Digite o nome: ")
# idade = int(input("Digite a idade: "))
# doenca_infectocontagiosa = input("Suspeita de doença infectocontagiosa?").upper() #.upper() converte a entrada do usuário em letras maiúsculas
# if idade>=65:
#     print("O paciente " + nome + " POSSUI atendimento prioritário!")
# elif doenca_infectocontagiosa=="SIM":
#     print("O paciente " + nome + " deve ser direcionado para sala de espera reservada.")
# else:
#     print("O paciente " + nome + " NÃO possui atendimento prioritário e pode aguardar na sala comum!")

nome=input("Digite o nome: ")
idade=int(input("Digite a idade: "))
doenca_infectocontagiosa=input("Suspeita de doença infectocontagiosa?").upper()
if idade>=65 and doenca_infectocontagiosa=="SIM":
    print("O paciente será direcionado para sala AMARELA - COM prioridade")
elif idade < 65 and doenca_infectocontagiosa == "SIM":
    print("O paciente será direcionado para sala AMARELA - SEM prioridade")
elif idade >= 65 and doenca_infectocontagiosa == "NAO":
    print("O paciente será direcionado para sala BRANCA - COM prioridade")
elif idade < 65 and doenca_infectocontagiosa == "NAO":
    print("O paciente será direcionado para sala BRANCA - SEM prioridade")
else:
    print("Responda a suspeita de doença infectocontagiosa com SIM ou NAO")