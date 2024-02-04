# Requests

Instalando as biblíotecas.

```bash
pip install requests bs4
```

Importando as bíbliotecas

```python
import requests
from bs4 import BeautifulSoup as bs
```

Função para pegar o nome e o preço de ações pesquisando pelos tikers, utiliando a biblíoteca `requests` com o método `.get(url)`
passando a url o site do google finance completando com o tiker ex: `["TAEE11"]`
retornando toda a página referente a `TAEE11`.

```python
def get_price(tikers: list[str]) -> dict[str, float]:
    """az uma requisição a api para pegar o preço e o nome das ações
    passando os tikers como argumento.

    >>> prices = get_price(["TAEE11"])
    >>> print(prices)
    ... {"Taesa S.A.": 36.53}

    Args:
        tikers (list[str]): Lista de tikers para serem pesquisados.

    Returns:
        dict[str, float]: Dicionário contendo o nome e o preço atual dos
        tikers.

    """
    prices = {}
    for tiker in tikers:
        url = f"https://www.google.com/finance/quote/{tiker}:BVMF?hl=pt"
        r = requests.get(url)
        if r.status_code == 200:
            name, price = extract_name_and_price(bs(r.text, "html.parser"))
            prices[name] = price
    return prices


```

Função que recebe a página html e retorna um dicionário contendo os nomes e as cotações com tipos `str` e `float`.

```python
def extract_name_and_price(html: bs) -> list[str, float]:
    """Extrai o nome e o preço dos tikers do html passado como parâmetro
    pesquisando pela tag `<div>` e sua `class`.

    ```html
    <div role="heading" aria-level="1" class="zzDege">Taesa S.A.</div>
    <div class="YMlKec fxKbKc">R$&nbsp;36,53</div>
    ```

    Args:
        html (bs): Classe beautifulsoup.

    Returns:
        list[str, float]: Lista contendo o nome e o preço do tiker.
    """
    CLASSES = {"name": "zzDege", "price": "YMlKec fxKbKc"}
    name = html.find(name="div", class_=CLASSES["name"]).text
    price = html.find(name="div", class_=CLASSES["price"]).text
    return [name, float(price.replace("R$\xa0", "").replace(",", "."))]


```

Exemplo de uso, chamei a função `get_price()` passando os tikers `["TAEE11", "ELET6", "VALE3"]` e printando:

```python
if __name__ == "__main__":
    TIKERS = ["TAEE11", "ELET6", "VALE3"]
    prices = get_price(TIKERS)
    print(prices)

```

> {'Taesa S.A.': 36.53, 'Eletrobras': 45.44, 'Vale S.A.': 66.08}
