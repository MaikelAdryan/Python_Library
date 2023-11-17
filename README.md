# Python_Library

## Arquivos de exemplos de bibliotecas do Python

* [requests -> awesomeapi CEP](./get_address_by_cep.py)

Instale a biblioteca requests pelo seu terminal

```bash
pip install requests
```

----
Link da API -> [https://docs.awesomeapi.com.br/api-cep](https://docs.awesomeapi.com.br/api-cep)

----

```python
import requests

CEP = '91250105'
URL = f'https://cep.awesomeapi.com.br/json/{CEP}'

RESPONSE = requests.get(URL)
JSON = RESPONSE.json()
ADDRESS = JSON['address']

print(ADDRESS)

```

* [`Pegar um endereço passando CEP`](./get_address_by_cep.py)

* []()
* []()
