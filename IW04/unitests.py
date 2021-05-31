import time
import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys


class PythonOrgSearch(unittest.TestCase):
    def setUp(self):
        # запуск Firefox при начале каждого теста
        # self.driver = webdriver.Firefox()
        self.driver = webdriver.Chrome()

    def test_search_in_python_org(self):
        driver = self.driver
        # открытие в Firefox страницы http://www.python.org
        driver.get("http://www.python.org")
        # проверка наличия слова Python в заголовке страницы
        self.assertIn("Python", driver.title)
        # ждем 5 секунд
        time.sleep(5)
        # получение элемента страницы с именем q (строка поиска)
        # (откройте вручную в любом браузере сайт http://www.python.org,
        # нажмите правой кнопкой мыши по строке поиска,
        # выберите пункт "просмотреть код",
        # убедитесь, что у этого элемента name="q")
        elem = driver.find_element_by_name("q")
        # ждем 5 секунд
        time.sleep(5)
        # набор слова chupakabra в найденном элементе
        elem.send_keys("chupakabra")
        # ждем 5 секунд
        time.sleep(5)
        # нажатие кнопки Enter в найденном элементе
        elem.send_keys(Keys.RETURN)
        # ждем 5 секунд
        time.sleep(5)
        # проверка наличия строки "No results found."
        # на странице с результатами поиска
        self.assertIn("No results found.", driver.page_source)
        # ждем 5 секунд
        time.sleep(5)
        # получение элемента страницы с именем q
        # на обновленной странице
        elem = driver.find_element_by_name("q")
        # очищаем строку поиска
        elem.clear()
        # ждем 5 секунд
        time.sleep(5)
        # набор слова pycon в найденном элементе
        elem.send_keys("pycon")
        # ждем 5 секунд
        time.sleep(5)
        # нажатие кнопки Enter в найденном элементе
        elem.send_keys(Keys.RETURN)
        # ждем 5 секунд
        time.sleep(5)
        # проверка отсутствия строки "No results found."
        # на странице с результатами поиска
        self.assertNotIn("No results found.", driver.page_source)

    def test_login_logout(self):
        driver = self.driver
        # открытие в Firefox страницы http://www.python.org/psf-landing/
        # на которой есть кнопка Sign In
        driver.get("https://www.python.org/psf-landing/")
        # ждем 5 секунд
        time.sleep(5)
        # поиск ссылки с текстом "Sign In"
        elem = driver.find_element_by_link_text("Sign In")
        # нажатие на ссылку
        elem.click()
        # ждем 5 секунд
        time.sleep(5)
        # поиск текстового поля для ввода логина по XPath
        # (тег input с name='login')
        elem = driver.find_element_by_xpath("//input[@name='login']")
        # ввод логина
        elem.send_keys("LOGIN")
        # ждем 5 секунд
        time.sleep(5)
        # поиск текстового поля для ввода пароля по XPath
        # (тег input с name='password')
        elem = driver.find_element_by_xpath("//input[@name='password']")
        # ввод логина
        elem.send_keys("PASSWORD")
        # ждем 5 секунд
        time.sleep(5)
        # жмем ввод для отправки формы
        elem.send_keys(Keys.RETURN)
        # ждем 5 секунд
        time.sleep(5)
        # проверка наличия на странице строки "Your account"
        # после входа
        self.assertIn("Your account", driver.page_source)
        # ждем 5 секунд
        time.sleep(5)
        # вывод кода страницы для отладки, потом можно будет убрать
        print(driver.page_source)
        # поиск ссылки с текстом "Sign out"
        # elem = driver.find_element_by_link_text("Sign out")
        # # нажатие на ссылку
        # elem.click()
        # # ждем 5 секунд
        driver.get("https://www.python.org/accounts/logout/")
        time.sleep(5)
        # поиск кнопки на форме в главной области страницы
        # по CSS-селектору
        elem = driver.find_element_by_css_selector(
            'div.container section.main-content form button'
        )  # нажатие на кнопку
        elem.click()
        # ждем 5 секунд
        time.sleep(5)
        # проверка отсутствия на странице строки "Your account"
        # после выхода
        self.assertNotIn("Your account", driver.page_source)

    def test_about_breadcrumbs(self):
        driver = self.driver
        # открытие в Firefox страницы http://www.python.org
        driver.get("http://www.python.org")
        # получаем список ссылок в меню About по CSS-селектору
        elems = driver.find_elements_by_css_selector('#about ul li a')

        # перебираем полученные подпункты меню,
        # выписываем названия и ссылки в отдельные списки
        # потому что при переходе по ссылкам на другие страницы
        # связь со списком подпунктов будет потеряна
        href_list = []
        name_list = []
        for e in elems:
            href_list.append(e.get_attribute("href"))
            name_list.append(e.get_attribute('innerHTML'))

        # перебираем полученные ссылки
        for i in range(len(href_list) - 1):
            # переходим по ссылке
            driver.get(
                href_list[i]
            )
            # получаем строчку хлебных крошек
            elem = driver.find_element_by_css_selector('.breadcrumbs')
            # проверка наличия в хлебных крошках ссылки на пункт About
            self.assertIn("About", elem.get_attribute('innerHTML'))
            # проверка наличия в хлебных крошках
            # наличия названия текущего пункта
            self.assertIn(
                # название текущего пункта
                name_list[i],
                # строчка хлебных крошек
                elem.get_attribute('innerHTML')
            )
            # ждем 5 секунд
            time.sleep(3)

    def tearDown(self):
        # закрытие браузера при окончании каждого теста
        self.driver.close()


if __name__ == '__main__':
    unittest.main()
