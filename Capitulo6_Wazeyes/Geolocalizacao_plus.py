from geopy.geocoders import Nominatim

geolocator = Nominatim(user_agent="wazeyes")

endereco=input("Digite um endereco com número e cidade. "
               "\nExemplo: avenida paulista, 100 São Paulo:\n")
resultado = str(geolocator.geocode(endereco)).split(",")

if resultado[0]!='None':
    print("Endereço completo.: ", resultado)
    print("Bairro............: ", resultado[2])
    print("Cidade............: ", resultado[4])
    print("Regiao............: ", resultado[8])