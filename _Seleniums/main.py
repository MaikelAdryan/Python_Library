"""
"""

from time import sleep

from selenium.webdriver import Firefox
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException

show_browser = True
OPTIONS = Options()
if not show_browser:
    OPTIONS.add_argument("--headless")


def test_firefox() -> bool:
    """Função para testar se o firefox está funcionando.
    """
    browser = Firefox(options=OPTIONS)
    browser.close()


def search_google(words: str, browser: Firefox) -> None:
    """Função que recebe uma string como argumento e o navegador,
    pesquisando as palavras no google.

    Args:
        words (str): Palavras a serem pesquisadas no google.
        browser (Firefox): webdriver do selenium navegador Firefox.
    """
    SITE_GOOGLE = "https://www.google.com/"
    XPATHS = {"search bar": "//*[@id='APjFqb']"}
    browser.get(SITE_GOOGLE)
    sourch_bar = browser.find_element(By.XPATH, XPATHS["search bar"])
    sourch_bar.click()
    sourch_bar.send_keys(words)
    sourch_bar.submit()


def get_price_bitcoin(browser: Firefox) -> str:
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
    browser = Firefox(options=OPTIONS)
    search_google(words="bitcoin", browser=browser)
    bitcoin_price = get_price_bitcoin(browser=browser)
    print(bitcoin_price)
    input()
    browser.close()


if __name__ == "__main__":
    search_bitcoin_price_on_google()
