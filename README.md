# Python_Library

## Arquivos de exemplos de bibliotecas do Python

* [requests -> awesomeapi CEP](./get_address_by_cep.py)

Link da API -> [https://docs.awesomeapi.com.br/api-cep](https://docs.awesomeapi.com.br/api-cep)

----
Instale a biblioteca requests pelo seu terminal

```bash
pip install requests
```

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

* [deep_translator -> Google Tradutor](./deep-translator.py)

----
Instale a biblioteca deep_translator pelo seu terminal

```bash
pip install deep_translator
```

----

```python
from deep_translator import GoogleTranslator

PT, EN = 'pt', 'en'

GOOGLE = GoogleTranslator(source=PT, target=EN)

NAME, AGE = 'Adryan Maikel da Cunha Kuhne', 21
TEXT = f'Olá Mundo! Meu nome é {NAME}, e tenho {AGE} anos de idade.'

translator = GOOGLE.translate(TEXT)
print(translator)

```

* [PySimpleGUI -> Criar janelas com python](./PySimpleGUI_basic.py)

----
Instale a biblioteca PySimpleGUI pelo seu terminal

```bash
pip install PySimpleGUI
```

----

```python
import PySimpleGUI as sg

sg.theme('Python')

LAYOUT = [
  [sg.Input('Hello World!', key='input')],
  [sg.Button('CLIQUE')]
]

WINDOW = sg.Window('Título', LAYOUT)

while True:
  events, values = WINDOW.read()
  
  if events == 'CLIQUE':
    sg.popup(f"{values['input']}")
  
  if events == sg.WINDOW_CLOSED:
    break

WINDOW.close()

```

* [tqdm -> Barra de progresso](./progress_bar.py)

----
Instale a biblioteca tqdm pelo seu terminal

```bash
pip install tqdm
```

----

```python
from tqdm import tqdm
from time import sleep

def method_one():
  for i in tqdm(range(10)):
    sleep(1)


def method_two():
  list = [1, 2, 3, 4, 5, 10]
  for item in tqdm(list):
    sleep(1)


def method_three():
  steps = 100
  with tqdm(total=steps) as progress_bar:
    for i in range(steps):
      sleep(0.1)
      progress_bar.update(1)


```
