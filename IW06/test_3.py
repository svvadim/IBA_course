from fixtures import *
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.expected_conditions import presence_of_element_located


# проверка распознавания грамотных слов
def test_ru(browser, ru):
    # находим поле ввода текста
    elem = browser.find_element_by_id("job_text_spell")
    # вводим заголовок страницы
    elem.send_keys("Проверка орфографии онлайн")
    # находим и жмем кнопку "Проверить"
    elem = browser.find_element_by_css_selector(
        "#text_spell_check a:nth-child(1)"
    )
    elem.click()
    # ожидаем появления результатов
    # (результаты на странице есть постоянно, но их
    # не видно из-за style='display:none', видны
    # становятся, когда style='')
    wait = WebDriverWait(browser, 20)
    first_result = wait.until(
        presence_of_element_located((
            By.CSS_SELECTOR, "#text_check_results[style='']")))
    # находим таблицу с результатами
    elem = browser.find_element_by_css_selector(".seo_table")
    # находим ячейку с числом грамматических ошибок
    td = elem.find_element_by_xpath("tbody/tr[9]/td[2]")
    # надеемся, что в заголовке сервиса по проверке орфографии ошибок нет
    assert td.get_attribute("innerHTML") == "0"
#py.test test_3.py


# E       AssertionError: assert '1' == '0'
# E         - 0
# E         + 1
