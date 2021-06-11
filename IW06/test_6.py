from fixtures import *
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.expected_conditions import presence_of_element_located

# проверка возможности обработки большого текста на английском
# по частям, размером меньше 100 000 символов - разобьем пьесу на акты
# и подсчитаем суммарную статистику
def test_Shakespeare(browser):
    # выбираем английский язык - только в одном тесте,
    # поэтому не в фикстуре:
    # находим выпадающий список с выбором языка
    elem = browser.find_element_by_name("id_lang")
    # получаем список пунктов в выпадающем списке
    options = elem.find_elements_by_tag_name("option")
    # находим пункт с английским языком и жмем его
    for option in options:
        if option.text.find("English") >= 0:
            option.click()
    # загружаем строки текста из файла
    file = open("Shakespeare.txt", mode="r", encoding="utf-8")
    lines = file.readlines()
    file.close()
    # объединяем строки в акты:
    # накапливаемый текст акта
    cur_act = ""
    # список строк с текстом отдельных актов
    acts = []
    for l in lines:
        # найдена строка начала нового акта
        if l.upper().find("ACT") == 0:
            # вставляем накопленный текст в список актов
            acts += [cur_act]
            # начинаем накапливать новый текст
            cur_act = l
        # обычная строка дописывается к тексту акта
        else:
            cur_act += l
    # вставляем накопленный в конце анализа строк текст в список актов
    acts += [cur_act]
    # поочередно отправляем тексты актов на анализ
    # сохраняем статистику по количеству символов
    sum = 0
    for text in acts:
        elem = browser.find_element_by_id("job_text_spell")
        # скопируем текст в буфер обмена и вставим его
        pyperclip.copy(text)
        elem.send_keys(Keys.CONTROL + "a")
        elem.send_keys(Keys.CONTROL + "v")
        elem = browser.find_element_by_css_selector(
            "#text_spell_check a:nth-child(1)"
        )
        elem.click()
        wait = WebDriverWait(browser, 20)
        first_result = wait.until(
            presence_of_element_located((
                By.CSS_SELECTOR,
                "#text_check_results[style=''].seo_table"))
        )

        elem = browser.find_element_by_css_selector(".seo_table")
        td = elem.find_element_by_xpath("tbody/tr[2]/td[2]")
        # считаем сумму символов во всех актах
        sum += int(td.get_attribute("innerHTML"))
        # нажимаем кнопку "Проверить новый текст"
        elem = browser.find_element_by_css_selector(
            "#text_check_results .botmenu a:nth-child(1)"
        )
        elem.click()
    # считаем, что если посчитанная сервисом сумма символов отличается
    # (модуль разности) от посчитанного вручную в Notepad++ количества
    # символов 187268 меньше чем на 1% (1873), то сервис работает норм
    assert abs(sum - 187268) < 1873
#py.test test_6.py

# E       selenium.common.exceptions.TimeoutException: Message:
