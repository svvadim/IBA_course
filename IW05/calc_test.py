import time
import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys


class MyTest(unittest.TestCase):
    def test_something(self):
        self.assertEqual(True, False)

    def setUp(self):
        # запуск Firefox при начале каждого теста
        self.driver = webdriver.Firefox()
        # открытие страницы при начале каждого теста
        self.driver.get('https://kalk.pro/finish/wallpaper/')
        self.driver.find_element_by_xpath("//html").click()
        # ждем 10 сек до появления окна подтверждения согласия с COOKIE
        time.sleep(10)
        # находим крестик в появившемся окне
        elem = self.driver.find_element_by_css_selector(".js--onclick-cookiePolicyAgree")
        # жмем на крестик
        elem.click()

    def test_calc(self):
        driver = self.driver
        # открываем калькулятор
        elem = driver.find_element_by_css_selector(".js--onclick-callCalc")
        elem.click()
        # ждем, пока калькулятор откроется
        time.sleep(3)

        elem = driver.find_element_by_name('1')
        elem.click()
        elem = driver.find_element_by_name('+')
        elem.click()
        elem = driver.find_element_by_name('1')
        elem.click()
        elem = driver.find_element_by_name('Result')
        elem.click()
        elem = driver.find_element_by_class_name("display-indicator-ceils")
        self.assertEqual(elem.text, '2')

        elem = driver.find_element_by_name('*')
        elem.click()
        elem = driver.find_element_by_name('2')
        elem.click()
        elem = driver.find_element_by_name('Result')
        elem.click()
        elem = driver.find_element_by_class_name("display-indicator-ceils")
        self.assertEqual(elem.text, '4')

        elem = driver.find_element_by_name('-')
        elem.click()
        elem = driver.find_element_by_name('1')
        elem.click()
        elem = driver.find_element_by_name('Result')
        elem.click()
        elem = driver.find_element_by_class_name("display-indicator-ceils")
        self.assertEqual(elem.text, '3')

        elem = driver.find_element_by_name('/')
        elem.click()
        elem = driver.find_element_by_name('3')
        elem.click()
        elem = driver.find_element_by_name('Result')
        elem.click()
        elem = driver.find_element_by_class_name("display-indicator-ceils")
        self.assertEqual(elem.text, '1')

        elem = driver.find_element_by_name('/')
        elem.click()
        elem = driver.find_element_by_name('0')
        elem.click()
        elem = driver.find_element_by_name('Result')
        elem.click()
        elem = driver.find_element_by_class_name("display-indicator-ceils")
        self.assertEqual(elem.text, 'Infinity')


if __name__ == '__main__':
    unittest.main()
