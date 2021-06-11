from fixtures import *


# проверка блокировки текстов больше заданного объема
# на тексте объемом >1 млн знаков
def test_Dostoyevskiy(browser, ru):
    elem = browser.find_element_by_id("job_text_spell")
    # загружаем текст из файла - этот текст
    # только в одном тесте, поэтому без фикстуры
    file = open("Dostoyevskiy.txt", mode="r", encoding="utf-8")
    text = file.read()
    file.close()
    # скопируем текст в буфер обмена и вставим его
    pyperclip.copy(text)
    elem.send_keys(Keys.CONTROL + "v")
    elem = browser.find_element_by_css_selector(
        "#text_spell_check a:nth-child(1)"
    )
    elem.click()
    elem = browser.find_element_by_css_selector("#text_too_long")
    # проверяем, что сообщение появилось
    # (до появления у него style='display: none;')
    assert elem.get_attribute("style") == ""


# проверка отсутствия блокировки текстов меньше заданного объема
# на тексте объемом в 24693-1030=23663 знака
def test_Pushkin(browser, ru, Pushkin):
    elem = browser.find_element_by_css_selector("#text_too_long")
    # проверяем, что сообщение не появилось
    # (остался style='display: none;')
    assert elem.get_attribute("style") == "display: none;"
#py.test test_5.py
