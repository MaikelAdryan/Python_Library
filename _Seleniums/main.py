"""
    Utilizarei o selenium para executar uma automação simples onde irá
entrar no site do google e pesquisar por bitcoin, encontrar o elemento
contendo o preço e retorna-lo em formato de string.
"""

from time import sleep

from selenium.webdriver import Firefox
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException

OPTIONS = Options()


def test_firefox() -> bool:
    """Função para testar se o firefox está funcionando.
    """
    browser = Firefox()
    input("Precione enter para fechar o navegador.")
    browser.close()


def hide_browser() -> None:
    """Função utilizada para ocultar a janela do navegador, executando
    as ações em segundo plano.
    """
    OPTIONS.add_argument("--headless")


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


if __name__ == "__main__":
    hide_browser()
    bitcoin_price = search_bitcoin_price_on_google()
    print(bitcoin_price)
