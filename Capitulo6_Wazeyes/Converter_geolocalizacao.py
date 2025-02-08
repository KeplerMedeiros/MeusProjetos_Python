import sys, os
sys.path.insert(0,os.path.abspath(os.curdir))

from geopy.geocoders import Nominatim
from Funcoes.Funcoes_JSON import ler_arquivo, gravar_arquivo

geolocator = Nominatim(user_agent = 'wazeyes') #nome do aplicativo
dicionario = ler_arquivo('entrada.json')
lista = dicionario['endereco']
endereco = lista[0] + ',' + lista[1] + ',' + lista[2] + ',' + lista[3]
location = geolocator.geocode(endereco)
saida = {'coordenadas': (location.latitude, location.longitude)}
gravar_arquivo(saida, 'saida.json')



# location = geolocator.geocode('100 5th Avenue')
# print(location.address)
# print((location.latitude, location.longitude))
