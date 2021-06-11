import pytest
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait

import pyperclip

URL = 'https://pastebin.com/'

@pytest.fixture()
def data():
    file = open('data.csv', 'r')
    data = file.readline().split(';')
    file.close()
    return data

@pytest.fixture()
def browser(data):
    profile= webdriver.FirefoxProfile (data[2])
    driver = webdriver.Firefox(profile)
    page = driver.get(URL)
    WebDriverWait (browser, 200)
    yield driver
    driver.close()

@pytest.fixture()
def clipboard_txt():
    file = open('text.txt', 'r')
    lines = file.read()
    file.close()
    pyperclip.copy(lines)

    return lines
