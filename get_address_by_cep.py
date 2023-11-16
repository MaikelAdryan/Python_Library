# API -> https://docs.awesomeapi.com.br/api-cep
import requests

CEP = '91250105'
URL = f'https://cep.awesomeapi.com.br/json/{CEP}'

RESPONSE = requests.get(URL)
JSON = RESPONSE.json()
ADDRESS = JSON['address']

print(ADDRESS)
