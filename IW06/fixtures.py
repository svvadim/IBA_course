import pytest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.proxy import Proxy
from selenium.webdriver.common.proxy import ProxyType
import pyperclip

# вспомогательная функция для выполнения перед тестом - фикстура (fixture)
@pytest.fixture()
def some_data():
    # просто возвращаем число
    return 42


@pytest.fixture()
def browser():
    # запуск Firefox при начале каждого теста (до yield)
    driver = webdriver.Firefox()
    # открытие страницы при начале каждого теста
    page = driver.get('https://advego.com/text/')
    # передача драйвера для использования в тесте
    yield driver
    # закрытие браузера после теста (после yield)
    driver.close()

# фикстура для выбора русского языка после запуска браузера
# (название фикстуры browser передано в параметре)
@pytest.fixture()
def ru(browser):
    # находим выпадающий список с выбором языка
    elem = browser.find_element_by_name("id_lang")
    # получаем список пунктов в выпадающем списке
    options = elem.find_elements_by_tag_name("option")
    # находим пункт с русским языком и жмем его
    for option in options:
        if option.text.find("Русский") >= 0:
            option.click()


# фикстура для отправки сказки Пушкина
# из файла на анализ после выбора русского языка

@pytest.fixture()
def Pushkin(browser, ru):
    elem = browser.find_element_by_id("job_text_spell")
    # загружаем текст из файла
    file = open("Pushkin.txt", mode="r", encoding="utf-8")
    text = file.read()
    file.close()
    # набирать большой текст send_keys не может
    # elem.send_keys(text)
    # скопируем текст в буфер обмена и вставим его
    pyperclip.copy(text)
    elem.send_keys(Keys.CONTROL + "v")
    elem = browser.find_element_by_css_selector(
        "#text_spell_check a:nth-child(1)"
    )
    elem.click()

