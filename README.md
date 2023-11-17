# Python_Library

## Arquivos de exemplos de bibliotecas do Python

* <a href='./get_address_by_cep.py'>requests -> awesomeapi CEP</a>

Instale a biblioteca requests pelo seu terminal
```bash
pip install requests
```
----

```python
# API -> https://docs.awesomeapi.com.br/api-cep
import requests

CEP = '91250105'
URL = f'https://cep.awesomeapi.com.br/json/{CEP}'

RESPONSE = requests.get(URL)
JSON = RESPONSE.json()
ADDRESS = JSON['address']

print(ADDRESS)

```

* <a href='get_address_by_cep.py'>Pegar um endereço passando CEP</a>
* <a href='get_address_by_cep.py'>Pegar um endereço passando CEP</a>
* <a href='get_address_by_cep.py'>Pegar um endereço passando CEP</a>
