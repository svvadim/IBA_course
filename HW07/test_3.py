from selenium.webdriver.common.keys import Keys
from fixtyres import *


def test_post_text(browser, clipboard_txt):
    element = browser.find_element_by_class_name('header__btn   ')
    element.click()
    element = browser.find_element_by_id('postform-text')
    element.send_keys(Keys.CONTROL + 'v')
    element = browser.find_element_by_id('postform-name')
    element.send_keys('Electric Yerevan Serj Tankian')
    element = browser.find_element_by_class_name('-big')
    element.click()
    element = browser.find_element_by_class_name('-post-view')
    assert element.get_attribute('innerText') == 'NOTE: Your guest paste has been posted.' \
                                                 ' If you sign up for a free account,' \
                                                 ' you can edit and delete your pastes!'
