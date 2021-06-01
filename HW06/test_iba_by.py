import time
import unittest

from selenium import webdriver
from selenium.webdriver.common.keys import Keys


class IbaByTest(unittest.TestCase):
    def setUp(self):
        self.options = webdriver.FirefoxOptions()
        self.timeout = 2
        # Раскомментировать для режима headless
        # self.options.add_argument('-headless')
        self.driver = webdriver.Firefox(options=self.options)
        self.driver.maximize_window()

    def test_search(self):
        driver = self.driver
        driver.get('https://iba.by/')
        time.sleep(self.timeout)
        self.assertIn(driver.title, "IBA BY")
        search_button = driver.find_element_by_class_name('fSearch_open')
        self.assertEqual(search_button.is_enabled(), True)
        search_button.click()
        search_edit_text = driver.find_element_by_class_name("fSearch_input.js_filled")
        search_edit_text.send_keys("The meaning of life")
        search_edit_text.send_keys(Keys.RETURN)
        time.sleep(self.timeout)
        find_sum = driver.find_element_by_class_name('finds_sum')
        result = find_sum.text.split()
        self.assertIn(result[0], '0')
        search_edit_text = driver.find_element_by_class_name("fSearch_input.js_filled._filled")
        search_edit_text.clear()
        search_edit_text.send_keys("IBA")
        search_edit_text.send_keys(Keys.RETURN)
        time.sleep(self.timeout)
        find_sum = driver.find_element_by_class_name('finds_sum')
        result = find_sum.text.split()
        self.assertGreater(int(result[0]), 0)

    def test_social_network_urls(self):
        """Check social networks urls"""
        driver = self.driver
        driver.get('https://iba.by/')
        time.sleep(self.timeout)
        self.assertIn(driver.title, "IBA BY")
        urls_soc_net = driver.find_elements_by_css_selector("nav.mNets:nth-child(4) > a")
        self.assertGreater(len(urls_soc_net), 0)
        test_urls = ['https://www.facebook.com/IBAGroup',
                     'https://www.linkedin.com/showcase/iba-group-products/',
                     'https://twitter.com/iba_group',
                     'https://www.instagram.com/iba_group/',
                     'https://www.youtube.com/user/kanclerpromo'
                     ]
        for url in urls_soc_net:
            # print(url.get_attribute('href'))
            self.assertIn(url.get_attribute('href'), test_urls)

        urls_soc_net = driver.find_elements_by_css_selector("nav.mNets:nth-child(1) > a")
        self.assertGreater(len(urls_soc_net), 0)
        for url in urls_soc_net:
            # print(url.get_attribute('href'))
            self.assertIn(url.get_attribute('href'), test_urls)

    def tearDown(self):
        self.driver.close()


if __name__ == '__main__':
    unittest.main()
