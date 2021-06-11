from fixtures import *
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.expected_conditions import presence_of_element_located


# проверка обработки текста в 24693-1030=23663 знака
# по подсчетам символов и строк в Notepad++
def test_Pushkin(browser, ru, Pushkin):
    wait = WebDriverWait(browser, 20)
    first_result = wait.until(
        presence_of_element_located((
            By.CSS_SELECTOR, "#text_check_results[style='']")))
    elem = browser.find_element_by_css_selector(".seo_table")
    td = elem.find_element_by_xpath("tbody/tr[2]/td[2]")
    assert td.get_attribute("innerHTML") == "23663"
#py.test test_4.py
