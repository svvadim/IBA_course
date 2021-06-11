from fixtyres import *


def test_login(browser,data):
    element = browser.find_element_by_class_name('sign-in')
    element.click()
    element = browser.find_element_by_id('loginform-username')
    element.send_keys(data[0])
    element = browser.find_element_by_id('loginform-password')
    element.send_keys(data[1])
    element = browser.find_element_by_class_name('-big')
    element.click()
    element = browser.find_element_by_class_name ('header__user-name')
    assert element.get_attribute('innerText') == data[0]
