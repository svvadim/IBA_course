from fixtures import *


# проверка попадания на страницу с нужным заголовком
def test_opening(browser):
    # находим на странице заголовок 1-ого уровня (h1)
    elem = browser.find_element_by_tag_name("h1")
    # проверяем текст заголовка
    assert elem.text.find("Проверка орфографии онлайн") >= 0
#py.test test_2.py
