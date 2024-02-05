"""
    Utilizarei a biblíoteca `requests` para coletar dados de empresas no
site do google finance.

    > https://www.google.com/finance/

    Utilizarei também a biblioteca beautifulsoup para encontrar na 
página html retornada pela requisição o preço e o nome da empresa,
adicionando em um dicionário python.
"""

import requests
from bs4 import BeautifulSoup as bs


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


def get_price(tikers: list[str]) -> list[dict[str, float]]:
    """Faz uma requisição a api para pegar o preço e o nome das ações
    passando os tikers como argumento.

    Args:
        tikers (list[str]): Lista de tikers para serem pesquisados.

    Returns:
        list[dict[str, float]]: Json contendo o tiker, o nome e o preço
    da lista de tikers.

    >>> prices = get_price(["TAEE11"])
    >>> print(prices)
    ... [{'tiker': 'TAEE11', 'name': 'Taesa S.A.', 'price': 36.53}]
    """
    prices = []
    for tiker in tikers:
        shares = {}
        shares["tiker"] = tiker
        url = f"https://www.google.com/finance/quote/{tiker}:BVMF?hl=pt"
        r = requests.get(url)
        if r.status_code == 200:
            name, price = extract_name_and_price(bs(r.text, "html.parser"))
            shares["name"] = name
            shares["price"] = price
        prices.append(shares)
    return prices


if __name__ == "__main__":
    TIKERS = ["TAEE11", "ELET6", "VALE3"]
    prices = get_price(TIKERS)
    print(prices)
