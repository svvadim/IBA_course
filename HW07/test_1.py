from fixtyres import *


def test_opening(browser):
    assert browser.title == 'Pastebin.com - #1 paste tool since 2002!'
