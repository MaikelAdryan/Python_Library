# Selenium

Instalando o selenium

```bash
pip install selenium
```

Importando do time:

* `sleep` -> Utilizado para fazer o python dar uma pausa passando os segundos.

Importando do selenium:

* `Firefox` -> Navegador escolhido para fazer a automação.
* `Options` -> Optições adicionais do navegador, utilizarei na função `hide_browser()` para poder ocultar o navegador quando chamada.
* `By` -> Utilizado para encontrar elementos por XPATH ou por CSS.

```python
from time import sleep

from selenium.webdriver import Firefox
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
```

Atribuindo a uma variável global a classe Options do Firefox.

```python
OPTIONS = Options()
```

Criando função para testar se o Firefox está funcionando.

```python
def test_firefox() -> None:
    """Função para testar se o firefox está funcionando.
    """
    browser = Firefox()
    input("Precione enter para fechar o navegador.")
    browser.close()


```

Criando função para chamar adicionar o argumento nos options do navegador e ocultalo, executando o navegador em segundo plano.

```python
def hide_browser() -> None:
    """Função utilizada para ocultar a janela do navegador, executando
    as ações em segundo plano.
    """
    OPTIONS.add_argument("--headless")


```

Função para pesquisar algo no google, passando as palavras a serem pesquisadas por parâmetro.

```python
def search_google(words: str, browser: Firefox) -> None:
    """Função que recebe uma string como argumento e o navegador,
    pesquisando as palavras no google.

    Args:
        words (str): Palavras a serem pesquisadas no google.
        browser (Firefox): Webdriver do selenium, navegador Firefox.
    """
    SITE_GOOGLE = "https://www.google.com/"
    XPATHS_SEARCH_BAR = "//*[@id='APjFqb']"
    browser.get(SITE_GOOGLE)
    sourch_bar = browser.find_element(By.XPATH, XPATHS_SEARCH_BAR)
    sourch_bar.click()
    sourch_bar.send_keys(words)
    sourch_bar.submit()



```

Função onde pega o preço do bitcoin com base no XPATH do elemento da janela de resultado da pesquisa `bitcoin` no google.

```python
def get_price_bitcoin(browser: Firefox) -> str:
    """Função para pegar o preço do bitcoin na página de resultado da
    pesquisa do google com base no XPATH do elemento, fica pesquisando o
    elemento até encontrar a cada 1 segundo.

    Args:
        browser (Firefox): Webdriver do selenium, navegador Firefox.

    Returns:
        str: Preço do bitcoin.

    >>> bitcoin_price = get_price_bitcoin()
    >>> print(bitcoin_price)
    ... 211.464,46
    """
    XPATH_PRICE = "/html/body/div[5]/div/div[12]/div[1]/div[2]/div[2]/div/div"\
                  "/div[1]/div/block-component/div/div[1]/div/div/div/div[1]/"\
                  "div/div/div/div/div/div/div/div/div[3]/div[2]/span[1]"
    while True:
        sleep(1)
        try:
            bitcoin_price = browser.find_element(By.XPATH, XPATH_PRICE).text
            return bitcoin_price
        except NoSuchElementException as e:
            print(f"Não achou, {e}")


```

Função onde pesquisa no google `bitcoin` e retorna o preço em string. Ex: `"209.631,54"`.

```python
def search_bitcoin_price_on_google() -> str:
    """Função que pesquisa o preço do bitcoin no google, e retorna o
    preço em formato de string.

    Returns:
        str: Preço do Bitcoin em tempo real.
    """
    browser = Firefox(options=OPTIONS)
    search_google(words="bitcoin", browser=browser)
    bitcoin_price = get_price_bitcoin(browser=browser)
    browser.close()
    return bitcoin_price


```

Exemplo de uso.

```python
if __name__ == "__main__":
    hide_browser()
    bitcoin_price = search_bitcoin_price_on_google()
    print(bitcoin_price)

```
